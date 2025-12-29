# Tools Development

## 📌 Folder Overview

In this folder, the development of tools is made, together with their translation into simple python functions. The process relies on first evaluating the tools and refine them to acquire good results, followed by capturing their behavior into a function that can be used as a tool for the agentic system.

## ✨ Folders Specifications

* **Degradation_Tool**: In this folder, by using the values of the Flank Wear Failure (FWF) it is possible to estimate the degradation of the drill bit. This is done by the creation of (Safe, Warning, Failure) zones that are identified by a decision tree model. Two different approaches are suggested and developed inside, using one of them for the agentic system.


* **Quality_Tool**: Similarly to the degradation tool, by using a decision tree model over the Build-ip Edge Failure (BEF) and Compression Chip Failure (CCF) values of the dataset, it is possible to determine the quality of the drilling process. 


* **Tools_LLM**: Lastly, in this folder, both degradation and quality tools are translated into python functions that can be used by the agentic system. This only presents the results of the tools, as their development is encompassed in the folders mentioned above.

* **Torque_regression.ipynb**: This is an extra file that was used to implement the torque regression for any material. As of now, this file was not used for any tool, but it can be convienient to extend the existant tools to provide values for more materials than just the ones in the dataset.

