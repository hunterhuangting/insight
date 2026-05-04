# Cloud Automation Pilot

This directory contains a GitHub Actions pilot for moving one local Codex automation to a cloud runner.

## Pilot Task

- Task: `cvpr-ntire`
- Local automation name: `每日CVPR NTIRE重要新闻概要`
- Schedule: 08:00 Asia/Shanghai
- GitHub Actions cron: `0 0 * * *`
- Output: `automations/reports/YYYY-MM-DD/cvpr-ntire.md`

## Setup

1. Create a GitHub repository and put these files in it.
2. In the repository settings, add an Actions secret named `OPENROUTER_API_KEY`.
3. Optional: change `OPENROUTER_MODEL` in `.github/workflows/cvpr-ntire.yml`. The default is `openrouter/auto`.
4. Go to Actions and run `CVPR NTIRE Daily Research` manually once with `workflow_dispatch`.
5. Confirm the generated report appears under `automations/reports/`.

## Local Dry Run

```bash
python -m pip install --upgrade openai
OPENROUTER_API_KEY=... python automations/scripts/run_research_task.py cvpr-ntire
```

## Notes

- The runner uses OpenRouter's OpenAI-compatible Chat Completions API with the `openrouter:web_search` tool so it can fetch current public sources.
- Reports are uploaded as workflow artifacts and also committed back to the repository.
- This pilot does not modify your existing local Codex automations.
