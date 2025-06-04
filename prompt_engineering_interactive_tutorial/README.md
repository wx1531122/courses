# Welcome to Anthropic's Prompt Engineering Interactive Tutorial
中文翻译：# 欢迎参加 Anthropic 的提示工程互动教程

## Course introduction and goals
中文翻译：## 课程介绍和目标

This course is intended to provide you with a comprehensive step-by-step understanding of how to engineer optimal prompts within Claude.
中文翻译：本课程旨在让您全面、逐步地了解如何在 Claude 中设计最佳提示。

**After completing this course, you will be able to**:
中文翻译：**完成本课程后，您将能够**：
- Master the basic structure of a good prompt 
中文翻译：- 掌握良好提示的基本结构
- Recognize common failure modes and learn the '80/20' techniques to address them
中文翻译：- 识别常见的故障模式并学习“80/20”技术来解决这些问题
- Understand Claude's strengths and weaknesses
中文翻译：- 了解 Claude 的优点和缺点
- Build strong prompts from scratch for common use cases
中文翻译：- 针对常见用例从头开始构建强大的提示

## Course structure and content
中文翻译：## 课程结构和内容

This course is structured to allow you many chances to practice writing and troubleshooting prompts yourself. The course is broken up into **9 chapters with accompanying exercises**, as well as an appendix of even more advanced methods. It is intended for you to **work through the course in chapter order**. 
中文翻译：本课程的结构旨在让您有许多机会练习自己编写和排除提示故障。课程分为 **9 个章节，并附有练习**，还有一个包含更高级方法的附录。您应该**按章节顺序学习本课程**。

**Each lesson has an "Example Playground" area** at the bottom where you are free to experiment with the examples in the lesson and see for yourself how changing prompts can change Claude's responses. There is also an [answer key](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing).
中文翻译：**每节课底部都有一个“示例演练场”区域**，您可以在其中自由地试验课程中的示例，亲眼看看更改提示会如何改变 Claude 的响应。还有一个[答案 kunci](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing)。

Note: This tutorial uses our smallest, fastest, and cheapest model, Claude 3 Haiku. Anthropic has [two other models](https://docs.anthropic.com/claude/docs/models-overview), Claude 3 Sonnet and Claude 3 Opus, which are more intelligent than Haiku, with Opus being the most intelligent.
中文翻译：注意：本教程使用我们最小、最快、最便宜的模型 Claude 3 Haiku。Anthropic 还有[另外两款模型](https://docs.anthropic.com/claude/docs/models-overview)，Claude 3 Sonnet 和 Claude 3 Opus，它们比 Haiku 更智能，其中 Opus 是最智能的。

*This tutorial also exists on [Google Sheets using Anthropic's Claude for Sheets extension](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing). We recommend using that version as it is more user friendly.*
中文翻译：*本教程也存在于 [Google 表格中，使用 Anthropic 的 Claude for Sheets 扩展程序](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing)。我们建议使用该版本，因为它更易于用户使用。*

When you are ready to begin, go to `01_Basic Prompt Structure` to proceed.
中文翻译：准备好开始后，请转到 `01_Basic Prompt Structure` 继续。

## Table of Contents
中文翻译：## 目录

Each chapter consists of a lesson and a set of exercises.
中文翻译：每章包含一节课和一组练习。

### Beginner
中文翻译：### 初级
- **Chapter 1:** Basic Prompt Structure
中文翻译：- **第 1 章：**基本提示结构

- **Chapter 2:** Being Clear and Direct  
中文翻译：- **第 2 章：**清晰直接

- **Chapter 3:** Assigning Roles
中文翻译：- **第 3 章：**分配角色

### Intermediate 
中文翻译：### 中级
- **Chapter 4:** Separating Data from Instructions
中文翻译：- **第 4 章：**将数据与指令分开

- **Chapter 5:** Formatting Output & Speaking for Claude
中文翻译：- **第 5 章：**格式化输出和替 Claude 发言

- **Chapter 6:** Precognition (Thinking Step by Step)
中文翻译：- **第 6 章：**预知（循序渐进思考）

- **Chapter 7:** Using Examples
中文翻译：- **第 7 章：**使用示例

### Advanced
中文翻译：### 高级
- **Chapter 8:** Avoiding Hallucinations
中文翻译：- **第 8 章：**避免幻觉

- **Chapter 9:** Building Complex Prompts (Industry Use Cases)
中文翻译：- **第 9 章：**构建复杂提示（行业用例）
  - Complex Prompts from Scratch - Chatbot
中文翻译：  - 从头开始构建复杂提示 - 聊天机器人
  - Complex Prompts for Legal Services
中文翻译：  - 法律服务的复杂提示
  - **Exercise:** Complex Prompts for Financial Services
中文翻译：  - **练习：**金融服务的复杂提示
  - **Exercise:** Complex Prompts for Coding
中文翻译：  - **练习：**编码的复杂提示
  - Congratulations & Next Steps
中文翻译：  - 祝贺和后续步骤

- **Appendix:** Beyond Standard Prompting
中文翻译：- **附录：**超越标准提示
  - Chaining Prompts
中文翻译：  - 链接提示
  - Tool Use
中文翻译：  - 工具使用
  - Search & Retrieval
中文翻译：  - 搜索和检索