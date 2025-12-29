# Festo Plant for Discrete Manufacturing Developing Simulation Models for Industrial Copilots

**Technical University of Munich (TUM)**
**Siemens Technology AG**
**Course:** Software Lab 2025 

## 📌 Project Overview

This project is an implementation of both **Single Agent** and **Multi-Agent** systems that through the usage of developed tools aim to predict the wear and quality of the drilling process in a Festo Plant. With this project, new users can query the agentic system about different drilling processes and receive natural language responses from the Large Language Models. 

The goal of the project is to create an interface that allows users (with little experience about Festo Plant Drilling Processes) to get responses about different characteristics of the process, by only the usage of natural language. 

The dataset used was from: *https://www.kaggle.com/datasets/raphaelwallsberger/xai-drilling-dataset*

## ✨ Key Features & Tasks

This software implements the agentic systems and tool extensions derived from the project requirements:

### 🔹 Agentic Systems
* **Single Agent System**: Created only 1 Agent to logically respond to user's queries by handlinh simulateneously all tasks.
* **Multi Agent (Supervisor System)**: Implemented 3 Agents: **Quality Agent**, **Wear Agent**, **Supervisor**. These 3 agents work together to respond to queries by specializing in only 1 part of the tasks needed. 


### 🚀 Tools Created

#### Tool 1: Wear and Degradation Tool
* **Inputs**: Material to be used for drilling, feed rate when drilling [mm/min] and cutting speed [m/min].
* **Outputs**: The tool uses XGBoost to classify different probabilities of failure. By dividing the wear into 3 categories: 0 (no wear), 1 (degradation) and 2 (failure of flank), the tool outputs the probability of the system falling into each category. More information inside the Degradation Tool folder. 

#### Tool 2: Quality of Drilling Tool
* **Inputs**: Cooling rate [%] used in drilling process, feed rate, cutting speed and drill bit material.
* **Outputs**: The tool also uses a decision tree algorithm with boosting to create different criteria for decision. With these creiteria, the tool is able to correctly predict if there will be Good or Bad quaity of drilling following the BEF and CCF data. More information inside Quality Tool folder.


## 📂 Project Structure

```text
LLMs-Drill-Wear/
├── Literature/                  # Project assignment and theoretical background.
│   ├── ...
│   └── ...
├── Dataset/                     # Folder containing dataset and initial analysis of features.
│   ├── XAI_Drilling_Dataset.csv # Datase file.
│   └── PreAnalysis/             # Analysis of feature's importance and processing time independence.
│       ├── features_importance.ipynb   # Feature's Importanced Ranked for Flank Wear Failure (FWF).
│       ├── time_issue.ipynb     # Proof that Processing Time Data is Irrelevant.
│       └── README.md            # Further explanation about pre-analysis.
├── Degradation_Tool/            # Folder containing development of Wear/Degradation Tool.
│   ├── DegradationOneModel.ipynb       # Degradation tool by only using 1 XGBoost model for all materials. 
│   ├── DegradationMultipleModels.ipynb # Degradation tool by using 1 model for each material.
│   └── README.md                # More information regarding Degradation tool.
├── LLM_Choice/                  # Folder containing analysis over different LLMs performance on responses.
│   └── Tools_LLM/               # Folder containing the implementation of Degradation and Quality Tools into Python functions. 
│       ├── saved_models/        # Saved models for wear prediction from Degradation tool. 
│       └── __init__.py          # Python functions for agentic system
│   ├── correct_answers_EASY_MEDIUM.json     # JSON file with expected responses for user's queries.
│   ├── CorrectAnswers.py                    # Python file to create JSON file above.
│   ├── Single_LLM_Choice.ipynb              # Notebook to evaluate different LLMs performance based on accuracy and time.
│   └── README.md                            # More information regarding LLM choice for the agentic systems.
├── PromptEngineering/                  # Folder containing analysis over different prompt techniques.
│   └── FinalAnalysis/           # Folder containing the analysis of both agentic systems together. 
│       ├── ...         
│       └── FINALComparison.py   # Comparison between best Single Agent and Multi-Agent systems.
│   └── MultiAgentResponses/           # Folder containing the analysis of Multi-Agent.
│       ├── ...         
│       └── MultiPromptAnalysis.py   # Analysis of Multi-Agent responses for different prompts.
│   └── SingleAgentResponses/           # Folder containing the analysis of Single Agent. 
│       ├── ...         
│       └── SinglePromptAnalysis.py.py   # Analysis of Single Agent responses for different prompts.
│   ├── MultiAgentPrompts.ipynb         # Notebook for acquiring performance of Multi-Agent for Prompts.
│   ├── SingleAgentPrompts.ipynb        # Notebook for acquiring performance of Single Agent for Prompts.
│   └── README.md                       # More information for Prompt Engineering.
├── RESULT/                      # Folder that creates final agentic systems given all performance analysis and features importance.
│   ├── ...
│   ├── FinalMultiAgent.ipynb 
│   └── FinalSingleAgent.ipynb 
└── README.md                    # Project documentation

```

## ⚙️ InstallationTo run this project, you need **Python 3.x** and the following scientific computing libraries:

* **NumPy**: For vector and matrix operations.
* **Matplotlib**: For plotting and animation.

You can install the dependencies using pip:

```bash
pip install numpy matplotlib

```

## 🚀 Usage1. **Navigate to the Source Code directory:**
```bash
cd "Source Code"

```


2. **Run the simulation:**
```bash
python MainDEM.py

```


3. **Configuration:**
You can modify simulation parameters directly in `MainDEM.py` under the `Inputs` section:
* `coeff_of_restitution`: Coefficient of restitution (e).
* `mu_friction`: Coefficient of friction (\mu).
* `particles`: Initial positions, velocities, and properties of particles.
* `delta_t`: Time step size.

## 👥 Contributors

* **Eduardo Silva (03805057)** - *Responsible for LLM choice, Agentic System and Prompt Engineering*
* **Adri ()** - *Resposible for Degradation/Wear tool literature and development*
* **Lin ()** - *Responsible for Quality tool literature and development* 