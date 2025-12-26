# Analysis of Dataset and its Features

## 📌 Folder Overview

This folder is responsible for analyzing the given dataset and understand the importance of each of its features. The common goal of all the files inside this folder, is to create a solid truth-ground about the data, so that the tools and the agentic systems can be developed with the best features. 

For this reason, it is called "PreAnalysis" as it does fall into the creation of Tools and Agentic-System directly. Nevertheless, it creates a better understanding of what should and not be considered for such.

## ✨ Files Specifications

* **features_importance.ipynb**: This file is responsible for evaluating the feature importance of every column in the dataset with the goal of identifying the values of the FWF (Flank Wear Failure) column. The Degradation tool uses these values as reference for prediction, and for that reason it is important to understand which parameters of the drilling process create a bigger impact on the outcome. 

* **time_relevance.ipynb**: This file aims to reconfirm the idea that for this dataset it is not possible to correctly use the information of the "Processing Time" for FWf prediction. This is done by introducing a new variable (Tf) that will be later used in the degradation tool.

