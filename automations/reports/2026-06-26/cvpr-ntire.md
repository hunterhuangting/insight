---
task_id: cvpr-ntire
task_name: 每日 CVPR NTIRE 重要新闻概要
run_at: 2026-06-26T12:07:08.554672+08:00
model: openrouter/auto
provider: openrouter
---

# 每日 CVPR / NTIRE 重要新闻概要  
**任务 ID：** cvpr-ntire  
**运行日期：** 2026-06-26  
**时区：** Asia/Shanghai  

## 1. 今日是否有重要信息

**结论：有重要信息需要记录，但未发现 2026-06-26 当天由 CVPR/NTIRE 官方发布的新截止日期、规则变更或挑战赛改动。**

本次检索到的主要更新集中在 **CVPR 2026 会后官方总结、公开视频/注册用户视频入口、CVF Open Access 上线的 NTIRE 2026 Workshop 论文与挑战赛结果报告**。这些信息虽多为 6 月上旬至 6 月下旬会后发布/整理，但对研究复盘、参赛结果引用、业务技术选型仍然重要。

信息可信度分级：

- **官方确认：** CVPR 官网新闻、CVPR 2026 页面、CVF Open Access、NTIRE 官方页面。
- **社区/预印本消息：** arXiv 上的 NTIRE 挑战赛报告预印本、Codalab/Google Groups 等历史 CFP 信息。
- **我的推断：** 对研究趋势、业务影响、后续跟进事项的判断。

---

## 2. 重要新闻要点

## CVPR

### 2.1 CVPR 2026 官方闭幕总结发布：规模创纪录

**状态：官方确认**

CVPR 官方闭幕新闻称，CVPR 2026 已于 **2026 年 6 月 7 日**在丹佛 Colorado Convention Center 闭幕，会议吸引了：

- **12,200 名注册参会者**
- 来自 **84 个国家/地区**
- **16,092 篇论文投稿**，较 2025 年增长 24%
- **4,089 篇论文被接收展示**
- **153 个 workshops**
- **19 个 tutorials**
- **28 个 conference demonstrations**

官方同时公布了获奖论文和获奖 demo。  
来源：<https://cvpr.thecvf.com/Conferences/2026/News/Closing>

### 2.2 CVPR 2026 最佳论文与荣誉提名

**状态：官方确认**

CVPR 官方公布的主要论文奖项包括：

- **Best Paper：** *Efficiently Reconstructing Dynamic Scenes One D4RT at a Time*
- **Best Student Paper：** *Native and Compact Structured Latents for 3D Generation*
- **Best Paper Honorable Mention：**
  - *NitroGen: An Open Foundation Model for Generalist Gaming Agents*
  - *SAM 3D: 3Dfy Anything in Images*
- **Best Student Paper Honorable Mention：**
  - *ChordEdit: One-Step Low-Energy Transport for Image Editing*

这些获奖主题集中在 **动态 4D 场景重建、3D 生成、通用游戏智能体、SAM 系列 3D 化、图像编辑能量传输** 等方向。  
来源：<https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers>

### 2.3 CVPR 2026 视频页面已提供会议录像入口

**状态：官方确认**

CVPR 2026 视频页面显示，会议的 keynotes、oral sessions、tutorials、workshops 等视频会陆续发布。页面说明：

- 主会期间若干会议室提供直播；
- 直播录像通常约 48 小时内发布；
- workshop 和 tutorial 录像在会后一周内陆续发布；
- 访问权限与实体/虚拟注册有关。

目前页面已列出 keynote、oral sessions 等条目。  
来源：<https://cvpr.thecvf.com/Conferences/2026/Videos>

### 2.4 CVPR 2027 地点与日期需继续核对

**状态：官方确认 + 需跟进**

CVPR 官方闭幕稿提到 **CVPR 2027 将在 Seattle Convention Center, Seattle, Washington 举办**。页面中可见 **19–26 June 2027** 的会议周期信息，同时正文中也出现过 **20–24 June** 的表述。较合理的解释是：前者可能对应完整会议周，后者可能对应主会日期，但仍建议后续以 CVPR 2027 官方站点为准。

来源：<https://cvpr.thecvf.com/Conferences/2026/News/Closing>

---

## NTIRE

### 2.5 NTIRE 2026 Workshop 页面与 CVF Open Access 论文集已可访问

**状态：官方确认**

NTIRE 2026 官方页面显示，本届 NTIRE 是 **CVPR 2026 关联 workshop**，Workshop Day 为：

- **2026 年 6 月 4 日**
- 地点：Colorado Convention Center, Denver
- 房间：Room 207

NTIRE 页面说明，被接收论文将收录于 **CVPR Workshops proceedings**，并由 CVF Open Access / IEEE Xplore 发布。当前 CVF Open Access 已有 NTIRE 2026 Workshop 专页，包含多个挑战赛报告与方法论文。

NTIRE 官方页：<https://www.cvlai.net/ntire/2026/>  
CVF Open Access NTIRE 2026：<https://openaccess.thecvf.com/CVPR2026_workshops/NTIRE>

### 2.6 NTIRE 2026 Image Shadow Removal 挑战赛冠军方法公开

**状态：官方确认**

CVF Open Access 上线论文：

> *Winner of CVPR2026 NTIRE Challenge on Image Shadow Removal: Semantic and Geometric Guidance for Shadow Removal via Cascaded Refinement*

该方法针对 NTIRE 2026 WSRD+ Shadow Removal Challenge，采用三阶段级联 refinement，结合：

- RGB 外观信息
- 冻结的 DINOv2 语义特征
- 单目深度与 surface normals 几何信息
- checkpoint ensembling

官方隐藏测试集结果：

- **PSNR：26.680**
- **SSIM：0.8740**
- **LPIPS：0.0578**
- **FID：26.135**
- 排名第一，赢得 NTIRE 2026 Image Shadow Removal Challenge。

来源：<https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Beltrame_Winner_of_CVPR2026_NTIRE_Challenge_on_Image_Shadow_Removal_Semantic_CVPRW_2026_paper.html>

### 2.7 NTIRE 2026 Ambient Lighting Normalization 结果报告上线

**状态：官方确认**

CVF Open Access 上线论文：

> *Learning-Based Ambient Lighting Normalization: NTIRE 2026 Challenge Results and Findings*

报告称该挑战面向 **复杂光照下的图像外观一致化**，包括 white lighting 与 multicolor lighting 等设置。关键信息：

- 超过 **150 名参与者**
- 两个 track 共 **24 个 final submissions**
- 评估包含 restoration fidelity、perceptual quality，并结合用户研究
- 高性能方法主要依赖深度学习、端到端模型和 iterative refinement 策略

来源：<https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Vasluianu_Learning-Based_Ambient_Lighting_Normalization_NTIRE_2026_Challenge_Results_and_Findings_CVPRW_2026_paper.html>

### 2.8 NTIRE 2026 RAIM Track 2：动态场景多曝光融合结果公开

**状态：官方确认**

CVF Open Access 上线论文：

> *NTIRE 2026 The 3rd Restore Any Image Model (RAIM) Challenge: Multi-Exposure Image Fusion in Dynamic Scenes (Track2)*

该挑战关注动态场景 HDR / 多曝光融合，数据设置包括：

- **100 个训练序列**，每个序列 7 个曝光等级
- **100 个测试序列**，每个序列 5 个曝光等级
- 面向相机抖动、场景运动、曝光变化、ghosting 等真实问题
- 吸引 **114 支参与团队**
- 收到 **987 次提交**
- Leaderboard score 由 PSNR、SSIM、LPIPS 等组成，并考虑感知质量、效率和可复现性

论文提到数据集和代码仓库：<https://github.com/qulishen/RAIM-HDR>  
论文来源：<https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Qu_NTIRE_2026_The_3rd_Restore_Any_Image_Model_RAIM_Challenge_CVPRW_2026_paper.html>

### 2.9 NTIRE 2026 Low Light Image Enhancement 挑战赛报告上线

**状态：官方确认**

CVF Open Access 上线论文：

> *Low Light Image Enhancement Challenge at NTIRE 2026*

报告称：

- Track 1 注册参与者 **195 人**
- Track 2 注册参与者 **153 人**
- 最终 **22 支队伍**提交有效结果
- 任务聚焦低照度、低对比度、噪声条件下的图像增强与联合去噪

来源：<https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Ciubotariu_Low_Light_Image_Enhancement_Challenge_at_NTIRE_2026_CVPRW_2026_paper.html>

### 2.10 NTIRE 2026 Image Denoising 挑战赛预印本结果

**状态：社区/预印本消息，需与 CVF Open Access 或最终论文交叉核验**

arXiv 上的报告：

> *The Third Challenge on Image Denoising at NTIRE 2026: Methods and Results*

报告称该任务聚焦 **AWGN σ=50 高噪声图像去噪**，不限制参数量或计算开销，主要以 PSNR 排名。关键信息：

- **116 名注册参与者**
- **20 支 finalist teams**
- 第一名：**BuptMM，PSNR 29.90 dB**
- 第二名：**I2WM&JNU，PSNR 29.89 dB**
- 第三名：**MIIE，PSNR 29.873 dB**
- 第四名：**Titans，PSNR 29.871 dB**
- 前四名差距小于 **0.03 dB**

来源：<https://arxiv.org/html/2606.16031>

---

## 3. 对研究 / 参赛 / 业务可能的影响

### 3.1 对研究方向的影响

**推断**

CVPR 2026 获奖论文与 NTIRE 2026 挑战赛结果共同显示以下趋势：

1. **3D / 4D 视觉继续升温**  
   最佳论文和学生最佳论文分别涉及动态 4D 场景重建与 3D 生成，说明 3D 表示、动态场景建模、空间智能仍是核心方向。

2. **图像复原任务从单一指标走向综合质量评价**  
   NTIRE 多个挑战同时使用 PSNR、SSIM、LPIPS、FID、用户研究、效率和可复现性等指标。仅追求 PSNR 的方法可能不足以满足实际业务场景。

3. **大模型特征与传统 restoration pipeline 融合更常见**  
   例如 Shadow Removal 冠军方法使用 DINOv2 语义特征和几何 cue，表明基础视觉模型特征正在成为图像复原任务的重要先验。

4. **Ensemble 和多阶段 refinement 仍是竞赛强策略**  
   多个 NTIRE 任务中，级联 refinement、checkpoint ensembling、iterative correction 等方法仍然有效。但这些策略在业务部署中需要重新评估延迟、显存、能耗和维护成本。

### 3.2 对参赛团队的影响

**推断**

- 已参加 NTIRE 2026 的团队应尽快核对 CVF Open Access 上的最终论文、排名、引用信息和补充材料。
- 准备参加后续 NTIRE / AIM / CVPR Workshops 的团队，可以将今年的 challenge report 作为 baseline 和规则设计参考。
- 如果计划复现，今年应优先关注带有公开代码仓库的任务，例如 RAIM-HDR、Image Denoising 等。

### 3.3 对业务落地的影响

**推断**

NTIRE 2026 的任务与多类业务场景直接相关：

| 任务方向 | 潜在业务场景 |
|---|---|
| Shadow Removal | 电商图像、地图街景、移动端摄影、遥感影像预处理 |
| Ambient Lighting Normalization | 商品图像标准化、相册增强、数字资产归一化 |
| Low Light Enhancement | 手机夜景、安防监控、车载视觉、工业检测 |
| Multi-Exposure Fusion / HDR | 摄影 ISP、AR/VR 内容采集、移动影像 pipeline |
| Denoising | 医学影像、安防、低光视频、移动端图像增强 |
| Efficient Super-Resolution | 端侧超分、视频增强、内容分发压缩后修复 |

业务采用时需重点检查：

- 是否使用 ensemble；
- 是否依赖额外训练数据；
- 推理速度、显存和 FLOPs；
- 代码许可证；
- 训练数据是否可商用；
- 在非 benchmark 数据上的泛化能力。

---

## 4. 需要继续跟进的日期或事项

1. **CVPR 2026 视频持续更新**
   - 继续检查 CVPR Videos 页面，确认 workshops/tutorials/keynotes/orals 是否全部上线。
   - 来源：<https://cvpr.thecvf.com/Conferences/2026/Videos>

2. **CVPR 2026 Open Access / IEEE Xplore 最终版本**
   - CVF Open Access 已提供 workshop 论文版本；正式 IEEE Xplore 元数据可能仍需后续确认。
   - 来源：<https://openaccess.thecvf.com/CVPR2026_workshops/NTIRE>

3. **CVPR 2027 日期与 CFP**
   - 需关注 CVPR 2027 官方页面，确认完整会议周、主会、workshop/tutorial 日期。
   - 当前 CVPR 2026 闭幕稿显示 Seattle Convention Center 信息，但日期表述需后续核对。
   - 来源：<https://cvpr.thecvf.com/Conferences/2026/News/Closing>

4. **NTIRE 2026 各挑战赛代码与 leaderboard 归档**
   - 重点跟进 RAIM-HDR、Image Denoising、Shadow Removal、Low Light Enhancement 等任务的代码仓库、补充材料、数据许可。
   - NTIRE 官方页：<https://www.cvlai.net/ntire/2026/>

5. **NTIRE 2026 challenge reports 是否有修订**
   - 个别 challenge report 可能在 arXiv 或 Open Access 上继续更新补充材料、代码链接或更正排名。
   - 建议持续核对 CVF Open Access 与 arXiv 版本差异。

---

## 5. 来源链接

### CVPR 官方来源

- CVPR 2026 官网主页  
  <https://cvpr.thecvf.com/Conferences/2026>

- CVPR 2026 News 页面  
  <https://cvpr.thecvf.com/Conferences/2026/News>

- CVPR 2026 闭幕新闻  
  <https://cvpr.thecvf.com/Conferences/2026/News/Closing>

- CVPR 2026 Best Papers 新闻  
  <https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers>

- CVPR 2026 Videos 页面  
  <https://cvpr.thecvf.com/Conferences/2026/Videos>

### NTIRE / CVF Open Access 官方来源

- NTIRE 2026 官方页面  
  <https://www.cvlai.net/ntire/2026/>

- CVF Open Access：CVPR 2026 Workshops / NTIRE  
  <https://openaccess.thecvf.com/CVPR2026_workshops/NTIRE>

- NTIRE 2026 Shadow Removal 冠军论文  
  <https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Beltrame_Winner_of_CVPR2026_NTIRE_Challenge_on_Image_Shadow_Removal_Semantic_CVPRW_2026_paper.html>

- NTIRE 2026 Ambient Lighting Normalization 结果报告  
  <https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Vasluianu_Learning-Based_Ambient_Lighting_Normalization_NTIRE_2026_Challenge_Results_and_Findings_CVPRW_2026_paper.html>

- NTIRE 2026 RAIM Track 2 多曝光融合报告  
  <https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Qu_NTIRE_2026_The_3rd_Restore_Any_Image_Model_RAIM_Challenge_CVPRW_2026_paper.html>

- NTIRE 2026 Low Light Image Enhancement 报告  
  <https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Ciubotariu_Low_Light_Image_Enhancement_Challenge_at_NTIRE_2026_CVPRW_2026_paper.html>

### 社区 / 预印本来源

- NTIRE 2026 Image Denoising Challenge arXiv 预印本  
  <https://arxiv.org/html/2606.16031>

---

**总体判断：**  
截至本次检索，6 月 26 日未发现新的官方规则或截止日期变更；但 CVPR 2026 会后总结、视频入口、NTIRE 2026 Open Access 论文与挑战赛结果已经构成重要的会后研究与参赛复盘资料，建议继续跟踪视频补全、代码开源、IEEE Xplore 正式版本和 CVPR 2027 日期确认。

## OpenRouter 引用注释

- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/CVPR2026_workshops/NTIRE)
- [CVPR 2026 Shatters Records, Revealing Latest Breakthroughs in Computer Vision and AI](https://cvpr.thecvf.com/Conferences/2026/News/Closing)
- [The Third Challenge on Image Denoising at NTIRE 2026: Methods and Results](https://arxiv.org/html/2606.16031)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Beltrame_Winner_of_CVPR2026_NTIRE_Challenge_on_Image_Shadow_Removal_Semantic_CVPRW_2026_paper.html)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Vasluianu_Advances_in_Single-Image_Shadow_Removal_Results_from_the_NTIRE_2026_CVPRW_2026_paper.html)
- [CVPR 2026 News - The Computer Vision Foundation](https://cvpr.thecvf.com/Conferences/2026/News)
- [CVPR 2026 Shatters Records, Revealing Latest Breakthroughs in Computer Vision and AI](https://cvpr.thecvf.com/Conferences/2026/News/Closing)
- [CVPR 2026 Honors the Year's Most Innovative Computer Vision and AI Research](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)
- [CVPR 2026 Fields 16,000+ Paper Submissions on Technical Advances in AI](https://cvpr.thecvf.com/Conferences/2026/News/Technical_Program)
- [2026 Conference](https://cvpr.thecvf.com/Conferences/2026)
- [NTIRE2026: New Trends in Image Restoration and Enhancement](https://www.cvlai.net/ntire/2026/)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/CVPR2026_workshops/NTIRE)
- [Call for Participation: CVPR'26 NTIRE challenges](https://groups.google.com/g/codalab-competitions/c/oBXhJe96UdY)
- [[visionlist] [CFP] CVPR 2026 New Trends in Image Restoration and Enhancement (NTIRE) workshop and challenges](http://visionscience.com/pipermail/visionlist_visionscience.com/2026/010282.html)
- [NTIRE 2026 — Real-World Face Restoration Challenge](https://ntire-face.github.io/2026/)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/CVPR2026_workshops/NTIRE)
- [NTIRE2026: New Trends in Image Restoration and Enhancement](https://www.cvlai.net/ntire/2026/)
- [The Third Challenge on Image Denoising at NTIRE 2026: Methods and Results](https://arxiv.org/html/2606.16031)
- [NTIRE 2026 The Second Challenge on Day and Night Raindrop Removal for Dual-Focused Images: Methods and Results](https://arxiv.org/html/2604.10634)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Ren_The_Eleventh_NTIRE_2026_Efficient_Super-Resolution_Challenge_Report_CVPRW_2026_paper.html)
- [2026 Conference](https://cvpr.thecvf.com/Conferences/2026)
- [CVPR 2026 Honors the Year's Most Innovative Computer Vision and AI Research](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers)
- [CVPR 2026 Shatters Records, Revealing Latest Breakthroughs in ...](https://cvpr.thecvf.com/Conferences/2026/News/Closing)
- [CVPR 2026 s](https://cvpr.thecvf.com/Conferences/2026/Videos)
- [CVPR 2026 Events with Videos - The Computer Vision Foundation](https://cvpr.thecvf.com/Conferences/2026/Videos)
- [CVPR 2026 Shatters Records, Revealing Latest Breakthroughs in ...](https://cvpr.thecvf.com/Conferences/2026/News/Closing)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Vasluianu_Learning-Based_Ambient_Lighting_Normalization_NTIRE_2026_Challenge_Results_and_Findings_CVPRW_2026_paper.html)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Qu_NTIRE_2026_The_3rd_Restore_Any_Image_Model_RAIM_Challenge_CVPRW_2026_paper.html)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Fan_Multilevel_Illumination_Consistent_Mapping_for_Ambient_Lighting_Normalization_CVPRW_2026_paper.html)
- [CVPR 2026 Open Access Repository](https://openaccess.thecvf.com/content/CVPR2026W/NTIRE/html/Ciubotariu_Low_Light_Image_Enhancement_Challenge_at_NTIRE_2026_CVPRW_2026_paper.html)

