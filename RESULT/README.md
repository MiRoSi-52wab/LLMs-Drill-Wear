# Prompt Engineering Selection

## 📌 Folder Overview

This folder contains the results of the project. This means that after developing the tools, selecting the best LLM and getting the best prompts for the single and multi-agent systems, it is possible to "talk" to our copilot. 

## ✨ Files Specifications

* **SingleAgent.ipynb**: This file contains the result for the Single Agent system.

* **MultiAgent.ipynb**: This file contains the result for the Multi-Agent system.

* **Tools_LLM/**: Just as in the LLM_Choice/ folder, the Tools_LLM/ folder only contains the implementation of the python functions that mimic the tools developed. This only needs to be changed if the same folder is changed inside the Tools/ folder. For example, if the new tools are created, this folder will be updated to also contain these tools.

## ⚙️ When to use Single/Multi-Agent?

For the Multi-Agent and Single Agent system we got the following plots:

![image.png](accuracy_comparison_radar.png)


![image.png](time_to_answer_questions.png)

As it can be seen above, the MA system is better at dealing with harder questions but also takes longer to respond. 
On the other hand, the SA system responds quickly but no so accurately for all difficulties. 

With this in mind, the choice between Multi-Agent and Single-Agent system depends on the application and the desired usage of the copilot. 
Both options are implemented inside the RESULT/ folder.

