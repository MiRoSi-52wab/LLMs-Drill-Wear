# Tool Development for Agentic System

## 📌 Folder Overview

In this folder we use the result from the Degradation and Quality tools and implement them into python functions that can later be used by the agentic system. 

## ✨ Files Specifications

The python files show the implementation of the python functions that are directly used as a tool for the agentic system. 

* For the degradation tool, this involves merely loading the decision tree models for each material and, by using the values for feed  and cutting speed, extract the predict values for (Safe, Warning, Failure) zones.

* For the quality tool, this involves creating if-else statements that mimic the rules created for the BEF and CCF criteria. By using the values for feed and cutting speed, it is possible to predict the quality of both.
