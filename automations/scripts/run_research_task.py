#!/usr/bin/env python3
"""Run one research automation and save a Markdown report."""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from openai import OpenAI


TASKS = {
    "cvpr-ntire": {
        "name": "每日 CVPR NTIRE 重要新闻概要",
        "prompt": "automations/prompts/cvpr-ntire.md",
    },
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing file: {path}") from exc


def build_input(task_id: str, task_name: str, prompt: str, run_date: str) -> str:
    return f"""你是一个严谨的中文研究自动化助手。

任务 ID：{task_id}
任务名称：{task_name}
运行日期：{run_date}
时区：Asia/Shanghai

请使用公开可访问来源进行联网调研。优先引用官方网站、会议页面、挑战赛页面、论文/榜单/公告页，避免无来源传闻。结论中要区分官方确认、社区消息和你的推断。输出必须是中文 Markdown。

任务说明：
{prompt}
"""


def run_task(task_id: str, output_root: Path, model: str, reasoning_effort: str) -> Path:
    if task_id not in TASKS:
        known = ", ".join(sorted(TASKS))
        raise SystemExit(f"Unknown task '{task_id}'. Known tasks: {known}")

    task = TASKS[task_id]
    prompt = read_text(Path(task["prompt"]))
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    run_date = now.strftime("%Y-%m-%d")

    client = OpenAI()
    response = client.responses.create(
        model=model,
        reasoning={"effort": reasoning_effort},
        tools=[
            {
                "type": "web_search",
                "search_context_size": "medium",
                "user_location": {
                    "type": "approximate",
                    "country": "CN",
                    "timezone": "Asia/Shanghai",
                },
            }
        ],
        tool_choice="auto",
        include=["web_search_call.action.sources"],
        input=build_input(task_id, task["name"], prompt, run_date),
    )

    report_dir = output_root / run_date
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / f"{task_id}.md"
    metadata = (
        f"---\n"
        f"task_id: {task_id}\n"
        f"task_name: {task['name']}\n"
        f"run_at: {now.isoformat()}\n"
        f"model: {model}\n"
        f"---\n\n"
    )
    report_path.write_text(metadata + response.output_text.strip() + "\n", encoding="utf-8")
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task_id", help="Task id, e.g. cvpr-ntire")
    parser.add_argument("--output-root", default="automations/reports")
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-5.2"))
    parser.add_argument(
        "--reasoning-effort",
        default=os.environ.get("OPENAI_REASONING_EFFORT", "medium"),
        choices=["low", "medium", "high"],
    )
    args = parser.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required")

    report_path = run_task(
        task_id=args.task_id,
        output_root=Path(args.output_root),
        model=args.model,
        reasoning_effort=args.reasoning_effort,
    )
    print(f"Wrote {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
