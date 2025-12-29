# Degradation/Wear Tool Development

## 📌 Folder Overview

This folder contains the files that allow for the analysis and development of the degradation tool. It contains two files, each proposing a different approach for the prediction of the flank wear failure (FWF). Below both files are explained in more detail, together with comments on the files themselves.

After deveolping the tool, this will be transalted into a python function that can be later used for the agenti system. This function is located inside the folder "Tools_LLM". 

## ✨ Files Specifications

* **DegradationMultipleModels.ipynb**: This file creates and train XGBoost (Decision Trees) models for each material available in the dataset. With these models, and by using a certain criteria to define (Safe, Warning and Failure) zones, it is possible to predict given input parameters the likelihood of the tool suffering from Flank Wear Failure. 

As seen in the notebook, the models can correctly predict the zones. Nevertheless, this leads to a higher demand for storage space and there is some confusion from the models to fully understand the area between Safe and Warning regions. For this, the next file implements a different approach.

**Important**: For the scope of this project, the agentic tools were implemented using the models available in this file (DegradationMultipleModels). 

* **DegradationOneModel.ipynb**: This file creates only one instance of a Decision Tree model for all the materials. For this reason, the model tries to learn all different areas for Safe, Warning and Failure to all models in parallel. Together with this, a filtering technique was used to better hanfle the confusion between Safe and Warning regions. 

In the scope of this project, this model was not used for the agentic tool; however, it is left as next step to simply save this model asn test it within the agent framework. 


## 🚀 Possible Next Steps: 

* **Single vs. Multiple Models**: In the scope of this project multiple models were used (one for each material). A possible next step is to evaluate and analyze performance compared to using only one model. 

* **Filtering for Multiple Model**: Implement the filtering technique used in single model into all the multiple moodels. This could lead to a better definition between Safe and Warning areas.