# Predictive Maintenance with KNN on Azure Machine Learning

> An end-to-end Machine Learning project for predicting industrial machine failures using KNN, Azure Machine Learning, MLflow, AutoML, Designer, and Managed Online Endpoints.

---

## 📌 Project Overview

Predictive maintenance helps identify potential machine failures before they occur, allowing maintenance teams to take preventive action and reduce unexpected downtime.

This project implements an end-to-end predictive maintenance workflow using the **AI4I 2020 Predictive Maintenance Dataset** and the **K-Nearest Neighbors (KNN)** classification algorithm.

The project explores three different machine learning approaches in Azure Machine Learning:

1. **Custom Jupyter Notebook** using Scikit-learn and MLflow
2. **Automated ML (AutoML)** restricted to the KNN algorithm
3. **Azure ML Designer** using a custom Python component

The complete workflow covers:

**Data Preparation → Model Training → Hyperparameter Tuning → Experiment Tracking → Model Registration → AutoML → Designer → Deployment → Endpoint Testing → Cleanup**

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Build a KNN-based predictive maintenance model.
- Clean and prepare the AI4I 2020 dataset.
- Understand the importance of feature scaling for KNN.
- Tune KNN hyperparameters using cross-validation.
- Track experiments using MLflow.
- Register the trained model in Azure Machine Learning.
- Train KNN using Azure Automated ML.
- Build a KNN workflow using Azure ML Designer.
- Deploy the model using a Managed Online Endpoint.
- Perform real-time inference testing.
- Compare different Azure ML approaches.
- Apply basic cloud and MLOps practices.
- Clean up Azure resources after completing the project.

---

# 🧠 Machine Learning Algorithm

## K-Nearest Neighbors (KNN)

KNN is a supervised machine learning algorithm used for classification.

For a new data point, KNN:

1. Calculates the distance between the new point and training samples.
2. Finds the nearest `K` observations.
3. Uses the neighbors' class labels to determine the prediction.

Since KNN is a **distance-based algorithm**, feature scaling is an important preprocessing step.

---

# 📊 Dataset

## AI4I 2020 Predictive Maintenance Dataset

The project uses the **AI4I 2020 Predictive Maintenance Dataset** from the UCI Machine Learning Repository.

The dataset contains machine and operational parameters that can be used to predict whether a machine will experience a failure.

### Target Variable

```text
machine_failure

The dataset contains a highly imbalanced target, with approximately 3.4% machine failures.

Because of this imbalance, accuracy alone is not sufficient for evaluating the model.

The project therefore considers:

Recall
F1 Score
AUC
Confusion Matrix
🛠️ Technology Stack
Category	Technology
Cloud Platform	Microsoft Azure
ML Platform	Azure Machine Learning
Programming Language	Python
Machine Learning	Scikit-learn
Data Processing	Pandas
Visualization	Matplotlib, Seaborn
Experiment Tracking	MLflow
AutoML	Azure Automated ML
Visual ML	Azure ML Designer
SDK	Azure ML SDK v2
Version Control	Git
Repository	GitHub
Deployment	Azure Managed Online Endpoint
☁️ Azure Resources
Azure Machine Learning Workspace
mlw-lab1-iram15
Resource Group
rg-mlab1-iram15
Compute Instance
Name:
ci-iram15-lab1

VM Size:
Standard_DS11_v2
Compute Cluster
Name:
cc-lab1

Minimum Nodes:
0

Maximum Nodes:
2

The compute cluster was configured with a minimum node count of 0 to avoid unnecessary compute usage when the cluster was idle.

🔄 End-to-End Project Workflow
AI4I 2020 Dataset
        │
        ▼
Data Cleaning & Preparation
        │
        ▼
Azure ML Data Assets
        │
        ├──────────────────┐
        │                  │
        ▼                  ▼
KNN Notebook           AutoML KNN
        │                  │
        └────────┬─────────┘
                 │
                 ▼
        Azure ML Designer
                 │
                 ▼
       Model Evaluation
                 │
                 ▼
        Model Registration
                 │
                 ▼
     Managed Online Endpoint
                 │
                 ▼
       Real-Time Prediction
                 │
                 ▼
             Cleanup
🧹 Part 1 — Azure ML Workspace

The project infrastructure was created using Microsoft Azure.

The following resources were configured:

Azure Resource Group
Azure Machine Learning Workspace
Compute Instance
Compute Cluster

The Azure ML workspace used for this project was:

mlw-lab1-iram15
💻 Part 2 — Compute Resources

Azure ML compute resources were created for running notebooks, experiments, and machine learning workloads.

Compute Instance
ci-iram15-lab1
Compute Cluster
cc-lab1

The compute cluster was configured with:

Minimum Nodes: 0
Maximum Nodes: 2

This configuration helps reduce unnecessary compute usage when no jobs are running.

🔗 Part 3 — GitHub Integration

A GitHub repository was created to maintain the project source code, notebooks, data preparation files, deployment scripts, and documentation.

Repository:

azureml-knn-maintenance

Git was used for version control and project tracking.

🧹 Part 4 — Data Preparation

The AI4I dataset was downloaded and prepared for machine learning.

The data preparation workflow included:

Loading the original dataset
Cleaning column names
Removing unnecessary identifier information
Removing leakage-prone failure-mode columns
Preparing the target variable
Checking missing values
Checking class imbalance
Selecting relevant features
Creating a clean CSV file
Registering the data in Azure ML

The cleaned dataset is stored at:

data/ai4i_clean.csv

Azure ML data assets were also created for the project.

🤖 Part 5 — KNN Notebook

The first machine learning approach was implemented using a custom Jupyter Notebook.

Workflow
Dataset
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
KNN
   ↓
Hyperparameter Tuning
   ↓
Cross-Validation
   ↓
Evaluation
   ↓
MLflow Tracking
   ↓
Model Registration

The notebook used:

Python
Pandas
Scikit-learn
StandardScaler
KNN
GridSearchCV
Stratified Cross-Validation
MLflow
Hyperparameter Tuning

A 5-fold Stratified Cross-Validation strategy was used.

The KNN model was tuned across multiple hyperparameter combinations.

The selected configuration was:

Best K:
5

Weights:
Distance

Scaler:
StandardScaler
Registered Model

The trained model was registered in Azure ML as:

knn-maintenance-notebook
📈 MLflow Experiment Tracking

MLflow was used to track machine learning experiments.

The tracked information included:

Model parameters
Evaluation metrics
Experiment runs
Confusion matrix artifacts
Model information

This improves experiment reproducibility and makes model comparison easier.

⚙️ Part 6 — Automated ML

The second approach used Azure Automated ML.

The AutoML experiment was restricted to the KNN algorithm.

Workflow
Azure ML Dataset
       ↓
Automated ML Job
       ↓
KNN Algorithm
       ↓
Hyperparameter Search
       ↓
Model Evaluation
       ↓
Best AutoML KNN Model

AutoML was used to automatically search and evaluate different KNN configurations.

This provided a comparison between manually tuned KNN and automated model experimentation.

🧩 Part 7 — Azure ML Designer

The third approach used Azure Machine Learning Designer.

A visual machine learning pipeline was created using a custom Python component.

Designer Workflow
Input Data
     ↓
Data Preparation
     ↓
Custom Python Component
     ↓
KNN Processing
     ↓
Model Evaluation
     ↓
Metrics

The custom Python script is located at:

designer/knn_designer_script.py

This demonstrates how Azure ML Designer can combine visual machine learning workflows with custom Python logic.

🚀 Part 8 — Model Deployment

The trained model was deployed using an Azure ML Managed Online Endpoint.

Endpoint
knn-maint-iram15-v3
Deployment
Deployment Name:
blue

Instance Type:
Standard_DS2_v2

The Managed Online Endpoint provides a real-time inference interface for sending machine data and receiving predictions.

🧪 Endpoint Testing

The deployment was tested using authenticated requests.

The testing workflow included:

Endpoint connectivity
Authentication
JSON request payload
Real-time inference
HTTP response validation

The deployment test returned:

HTTP Status: 200

Testing files:

deployment/
├── sample-request.json
└── test_endpoint.py

Security: Endpoint keys and other sensitive credentials are not stored in the GitHub repository.
.

📊 Model Comparison

The project compares three different KNN workflows.
ApproachBest KWeightsScaler UsedTest RecallTest F1AUCNotebook KNN + GridSearch5DistanceStandardScaler0.5330.5790.885Automated ML KNNTunedAutoStandardScaler (Auto)0.5400.5910.890Designer KNN5DistanceStandardScaler0.525
Evaluation Focus

Because machine failures represent only a small portion of the dataset, accuracy alone may not provide a complete picture of model performance.

The project therefore emphasizes:

Recall
F1 Score
AUC
Confusion Matrix

These metrics provide more information about how effectively the model identifies machine failures.

📁 Repository Structure
azureml-knn-maintenance/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── ai4i_clean.csv
│
├── notebooks/
│   ├── 00_prepare_data.ipynb
│   ├── 01_knn_notebook.ipynb
│   └── 02_deploy_endpoint.py
│
├── automl/
│   └── automl_results.md
│
├── designer/
│   └── knn_designer_script.py
│
├── deployment/
│   ├── sample-request.json
│   └── test_endpoint.py
│
└── screenshots/
    └── Parts 1-9 evidence
🔐 Security & Best Practices

The project follows basic cloud development and security practices.

Sensitive endpoint keys are not committed to GitHub.
Credentials are kept outside source code.
.gitignore is used to prevent unwanted files from being committed.
Compute resources are configured with controlled node limits.
Azure resources are cleaned up after the project.
Deployment configuration is separated from application code.
🧹 Part 9 — Cleanup

Cloud compute resources can generate costs while they are active.

After completing the required experiments, deployment testing, and screenshots, the Azure resources were cleaned up.

The project resource group was:

rg-mlab1-iram15

The cleanup process prevents unnecessary cloud resources from remaining active after project completion.

📸 Project Evidence

Screenshots documenting the project workflow are stored in:

screenshots/

The evidence covers:

Part 1 → Azure Workspace
Part 2 → Compute Resources
Part 3 → GitHub Integration
Part 4 → Data Preparation
Part 5 → KNN Notebook + MLflow
Part 6 → AutoML
Part 7 → Designer Pipeline
Part 8 → Endpoint Deployment & Testing
Part 9 → Comparison & Cleanup
📚 Key Learnings
Machine Learning

Through this project, I gained practical experience with:

K-Nearest Neighbors
Feature scaling
StandardScaler
Hyperparameter tuning
GridSearchCV
Stratified Cross-Validation
Classification metrics
Confusion Matrix
Imbalanced datasets
Azure Machine Learning

I worked with:

Azure ML Workspace
Resource Groups
Compute Instances
Compute Clusters
Data Assets
Model Registration
Automated ML
Azure ML Designer
Managed Online Endpoints
Real-time inference
MLOps & Development

The project also provided practical experience with:

MLflow
Git
GitHub
Experiment tracking
Model registration
Deployment
Endpoint testing
Cloud resource management
Project documentation
💡 Key Technical Insights
Feature Scaling

KNN is a distance-based algorithm. Therefore, features with larger numerical ranges can have a greater influence on distance calculations.

Using:

StandardScaler()

helps normalize numerical features before applying KNN.

Imbalanced Data

Only a small percentage of observations represent machine failures.

Therefore, evaluating the model only through accuracy can be misleading.

Recall, F1 Score, AUC, and the confusion matrix provide additional insight into failure detection performance.

Experiment Tracking

MLflow provides a structured way to track:

Parameters
Metrics
Artifacts
Experiments
Models

This improves reproducibility and makes experimentation easier to manage.

Multiple Azure ML Workflows

The project demonstrates three ways to build machine learning workflows:

Custom Code
     ↓
Jupyter Notebook

Automated Workflow
     ↓
AutoML

Visual Workflow
     ↓
Azure ML Designer
▶️ Endpoint Testing

If the endpoint is active, the deployment can be tested using:

python deployment/test_endpoint.py

Environment variables can be configured securely:

export AML_ENDPOINT_URL="<YOUR_ENDPOINT_URL>"
export AML_ENDPOINT_KEY="<YOUR_ENDPOINT_KEY>"

Never commit actual endpoint keys or credentials to the repository.

👩‍💻 Author
Iram Shahzadi

BS Computer Science

Technologies Demonstrated
Python
Machine Learning
KNN
Scikit-learn
Pandas
Azure Machine Learning
MLflow
AutoML
Azure ML Designer
Git
GitHub
Model Deployment
Cloud Computing
⭐ Project Summary

This project demonstrates a complete machine learning lifecycle using Microsoft Azure:

                 DATA
                  │
                  ▼
        Data Preparation
                  │
                  ▼
        Feature Processing
                  │
                  ▼
       ┌──────────┼──────────┐
       │          │          │
       ▼          ▼          ▼
   Notebook     AutoML    Designer
      KNN         KNN        KNN
       │          │          │
       └──────────┼──────────┘
                  ▼
          Model Evaluation
                  │
                  ▼
          Model Registration
                  │
                  ▼
       Managed Online Endpoint
                  │
                  ▼
         Real-Time Prediction
                  │
                  ▼
              Cleanup

The project demonstrates how a machine learning model can move from raw data to experimentation, evaluation, registration, deployment, and real-time inference using Azure Machine Learning.
