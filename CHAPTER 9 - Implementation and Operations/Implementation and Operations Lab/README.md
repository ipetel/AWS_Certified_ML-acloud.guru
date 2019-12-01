# Implementation and Operations Lab
Notice that this Lab is part C of <a href="https://github.com/ipetel/AWS_Certified_ML-acloud.guru/tree/master/CHAPTER%207%20-%20Algorithms/Algorithms%20Lab">Algorithms Lab</a>

**Use Case**

Mr. K has given us the go to deploy the optimized Linear Learner model in production! Once this is complete Mr. K's team can use it to investigate any newly reported UFO sighting. 
Our goal is to deploy the model into production and give Mr. K's team some way to interact with the deployed model. 

**Goal**

Deploy our Linear Learner model using SageMaker hosting and create a way to interact with the SageMaker endpoint created for the deployed model.


**My Solution**

I have created a solution that deploys a trained model and runs a real-time prediction on a live endpoint (I haven't created a way to interact with the SageMaker endpoint except using Notebook.), in my solution I have extended explanation for every step<br>
read the notebook for additional explanation.<br>
hope you will find this notebook useful.<br>

**Note**

1. in most of code cell that I'm using external libraries I'm importing it every time, although I can import all of them once on the start of the notebook, I wanted to show what libraries I'm using on every step.
2. there are numerous times that I'm assigning the same variables with the same values on different cells, again just want to to show what variables are used on every step.
