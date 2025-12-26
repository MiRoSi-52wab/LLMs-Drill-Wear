# Degradation/Wear Tool Development

## 📌 Folder Overview

This folder is responsible for analyzing the given dataset and understand the importance of each of its features. The common goal of all the files inside this folder, is to create a solid truth-ground about the data, so that the tools and the agentic systems can be developed with the best features. 

For this reason, it is called "PreAnalysis" as it does fall into the creation of Tools and Agentic-System directly. Nevertheless, it creates a better understanding of what should and not be considered for such.

## ✨ Files Specifications

* **DegradationMultipleModels.ipynb**: This file creates and train XGBoost (Decision Trees) models for each material available in the dataset. With these models, and by using a certain criteria to define (Safe, Warning and Failure) zones, it is possible to predict given input parameters the likelihood of the tool suffering from Flank Wear Failure. 

As seen in the notebook, the models can correctly predict the zones. Nevertheless, this leads to a higher demand for storage space and there is some confusion from the models to fully understand the area between Safe and Warning regions. For this, the next file implements a different approach.

**Important**: For the scope of this project, the agentic tools were implemented using the models available in this file. 

* **DegradationOneModel.ipynb**: This file creates only one instance of a Decision Tree model for all the materials. For this reason, the model tries to learn all different areas for Safe, Warning and Failure to all models in parallel. Together with this, a filtering technique was used to better hanfle the confusion between Safe and Warning regions. 

In the scope of this project, this model was not used for the agentic tool; however, it is left as next step to simply save this model asn test it within the agent framework. 


## 🚀 Possible Next Steps: 

* **Single vs. Multiple Models**: In the scope of this project multiple models were used (one for each material). A possible next step is to evaluate and analyze performance compared to using only one model. 

* **Filtering for Multiple Model**: Implement the filtering technique used in single model into all the multiple moodels. This could lead to a better definition between Safe and Warning areas.