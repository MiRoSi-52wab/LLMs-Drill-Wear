# Quality Tool Development

## 📌 Folder Overview

This folder contains all the files that were used for the development and refinement of the drilling quality tool. As explained in the files, since the Flank Wear Failure (FWF) values were used for the degradation criteria, the quality tool relies on another two types of failure:

* Build-up Edge Failure (BEF): *Represented as a binary feature, a build-up edge failure indicates the occurrence of material accumulation on the cutting edge of the drill bit due to a combination of low cutting speeds and insufficient cooling. A value of 1 signifies the presence of this failure mode, while 0 denotes its absence.*

* Compression Chip Failure (CCF): *This binary feature captures the formation of compressed chips during drilling, resulting from the factors high feed rate, inadequate cooling and using an incompatible drill bit. A value of 1 indicates the occurrence of at least two of the three factors above, while 0 suggests a smooth drilling operation without compression chips.*

Using these two types of failure, we assume that the drilling quality will be a direct subproduct of such. For this approach, we use again decision tree models, and by using their top-K rules (k is integer number selected to optimize recall while maintaining the depth of the model low) we implement them to a python function in "Tools_LLM". This python function will the be used by the agentic system.

**Important**: For quality tool, it is necessary to optimize Recall and not Precision of our decision models. This is the procedure for any safety/quality process, since it is better to obtain false "Bad Quality" results, then to obtain false "Good Quality". 

## ✨ Files Specifications

* **RecallTest.ipynb**: This is the first file used for the prediction of BEF and CCF quality. The user can select the parameters initially to test different train-test data splits and evaluate which of these create the better result for Recall. 

* **RuleExtraction.ipynb**: The second file of the folder is responsible for extractig the rules that define the decision tree model. With these rules, we implement them directly into a python function inside the "Tools_LLM" folder.

* **RuleReducing.ipynb**: Lastly, it is important to reduce the number of rules (even if it lower the values of Recall slightly) to prevent overfitting the dataset. This also allows for smaller and faster inference models.

## 🚀 Possible Next Steps: 

* **Evaluate BEF and CCF Togheter**: As of now, we have two decision tree models for each of the failure procedures (BEF and CCF). This allos for precise results for each off the scenarions. However, it might be interesting to create regions of quality (like how it was done for FWF degradation tool) by using the product of results of BEF and CCF. 

* **Quantitize Quality**: The results are binary (Good or Bad Quality), but how can one quantitify this quality, making it possible to distinguish between same value results?