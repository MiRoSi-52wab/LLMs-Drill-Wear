# LLM Selection Process

## 📌 Folder Overview

Affter implementing the tools, it is possible to start with the selection of the Large Language Model. For th scope of this project, the models available in the Ollama library were considered. The models used wre restrianed to RAM usage, since the LLMs were hosted locally. 

## ✨ Files Specifications

* **Tools_LLM/**: This is the same folder present in Tools/Tools_LLM, but for reasons of using a jupyter notebook we decied that it was better to have a copy of the folder inside LLM_Choice/ too. This allows the user to have a stable version for selecting the LLM, while at the same time developing new approaches for the tool inside the Tools/ folder. Whenever a tool is changed, it is just needed to paste the new Tools_LLM folder into the LLM_Choice folder.

* **CorrectAnswers.py**: This file creates the JSON files "correct_answers(...).json". These formated data files contain the expected responses for the user queries used for testing the LLMs. These queries can be inspected inside the SingleAgent.ipynb file.

* **ChooseLLM.ipynb**: Main file responsible for evaluating the accuracy and response time of different LLMs. By comparing these results, it is pssible to select a LLM that fits the criteria necesssary for the application. In this case, we selected the LLM with the highest accuracy without highly influenciating the response time. For this, the result was the usage of granite3.3:2b.

## 🚀 Possible Next Steps: 

* **Experiment with more LLMs**: Since the LLMs were being hosted locally, there was a constraint on how much RAM could be used. for this reason, it is interesting to experiment with bigger and more complex models to evaluate how response quality varies.

* **Increase User Queries**: Increasing the number of user queries can reveal some underlying problems with the LLMs that are not seen for lower number of queries.

* **Evaluate LLMs not Manually**: As of now, the LLM responses were evaluated manually due to their response being of natural language. This is a time consuming process that could be optimized by the usage of another LLM to evaluate question-response quality. Another option is to force the tested LLMs to respond in a format that is coherent with the JSON files "correct_answers(...).json"