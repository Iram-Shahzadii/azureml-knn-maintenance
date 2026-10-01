# Azure ML KNN — Predictive Maintenance

A complete **Machine Learning + MLOps project** for predicting machine failures using **K-Nearest Neighbors (KNN)** and **Microsoft Azure Machine Learning**.

The project covers the complete ML lifecycle:

**Data Preparation → Model Training → Evaluation → AutoML → Designer → Model Registration → Deployment → Real-Time Inference → Cleanup**

---

## 🎯 Project Objective

The goal is to build a classification model that predicts whether a machine is likely to **fail** based on industrial sensor and operational data.

Because machine failures represent a small portion of the dataset, **accuracy alone is not sufficient**. The project therefore focuses on:

| Metric               | Purpose                                        |
| -------------------- | ---------------------------------------------- |
| **Recall**           | Measures how many actual failures are detected |
| **F1 Score**         | Balances precision and recall                  |
| **AUC**              | Measures overall classification performance    |
| **Confusion Matrix** | Shows correct and incorrect predictions        |

---

## 🛠️ Technologies Used

| Category                | Technologies              |
| ----------------------- | ------------------------- |
| **Language**            | Python                    |
| **ML Algorithm**        | K-Nearest Neighbors (KNN) |
| **ML Libraries**        | Scikit-learn, Pandas      |
| **Cloud Platform**      | Microsoft Azure           |
| **ML Platform**         | Azure Machine Learning    |
| **Experiment Tracking** | MLflow                    |
| **Automation**          | Azure AutoML              |
| **Visual ML**           | Azure ML Designer         |
| **Version Control**     | Git & GitHub              |
| **Deployment**          | Managed Online Endpoint   |

---

## 📁 Repository Structure

```text
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
```

---

## ☁️ Azure ML Workflow

The project implements **three different Azure ML workflows**:

```text
                    Dataset
                       │
                       ▼
               Data Preparation
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Notebook       AutoML      Designer
        KNN            KNN          KNN
          │            │            │
          └────────────┼────────────┘
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
```

### Main Azure Components

* **Azure ML Workspace**
* **Compute Instance**
* **Compute Cluster**
* **Data Assets**
* **MLflow**
* **Automated ML**
* **Azure ML Designer**
* **Model Registry**
* **Managed Online Endpoint**

---

## 🤖 KNN Model

KNN is a **distance-based classification algorithm**, so feature scaling is important.

The project uses:

```python
StandardScaler()
```

Numerical features are scaled before applying KNN to prevent features with larger numerical ranges from dominating distance calculations.

The model workflow includes:

* **Train/Test Split**
* **StandardScaler**
* **Stratified Cross-Validation**
* **GridSearchCV**
* **Hyperparameter Tuning**
* **Recall, F1, AUC Evaluation**
* **Confusion Matrix**

---

## 🔬 Experiments

### 1. Custom KNN Notebook

The notebook implements the KNN workflow manually using **Scikit-learn** and tracks experiments using **MLflow**.

### 2. Azure AutoML

AutoML was used to automatically experiment with different configurations and identify a suitable KNN setup.

Results are documented in:

```text
automl/automl_results.md
```

### 3. Azure ML Designer

A visual pipeline was created using **Azure ML Designer** to demonstrate a low-code ML workflow.

---

## 🚀 Model Deployment

The trained model can be deployed through an **Azure Managed Online Endpoint** for real-time predictions.

Test the endpoint with:

```bash
python deployment/test_endpoint.py
```

Configure credentials through environment variables:

```bash
export AML_ENDPOINT_URL="<YOUR_ENDPOINT_URL>"
export AML_ENDPOINT_KEY="<YOUR_ENDPOINT_KEY>"
```

**Never commit endpoint keys, credentials, or other secrets to GitHub.**

---

## 📸 Project Evidence

Screenshots documenting the complete workflow are available in:

```text
screenshots/
```

| Part       | Evidence                      |
| ---------- | ----------------------------- |
| **Part 1** | Azure ML Workspace            |
| **Part 2** | Compute Resources             |
| **Part 3** | GitHub Integration            |
| **Part 4** | Data Preparation              |
| **Part 5** | KNN Notebook + MLflow         |
| **Part 6** | AutoML                        |
| **Part 7** | Azure ML Designer             |
| **Part 8** | Endpoint Deployment & Testing |
| **Part 9** | Comparison & Cleanup          |

---

## 🔐 Security & Cleanup

Basic cloud security practices were followed:

* **Secrets are excluded from GitHub**
* **Credentials are stored outside source code**
* **`.gitignore`** is used for sensitive/unwanted files
* **Compute resources use controlled limits**
* **Azure resources are cleaned up after experiments**

Resource group used:

```text
rg-mlab1-iram15
```

Cleanup helps prevent unnecessary cloud resource usage after project completion.

---

## 📚 Key Learnings

### Machine Learning

* **K-Nearest Neighbors**
* **Feature Scaling**
* **StandardScaler**
* **Hyperparameter Tuning**
* **GridSearchCV**
* **Stratified Cross-Validation**
* **Classification Metrics**
* **Confusion Matrix**
* **Imbalanced Classification**

### Azure & MLOps

* **Azure Machine Learning**
* **MLflow Experiment Tracking**
* **AutoML**
* **Azure ML Designer**
* **Model Registration**
* **Managed Online Endpoints**
* **Real-Time Inference**
* **Git & GitHub**
* **Cloud Resource Management**

---

## 👩‍💻 Author

### Iram Shahzadi

**BS Computer Science**

**Focus:** Machine Learning • MLOps • Azure • Python

---

## ⭐ Project Summary

This project demonstrates a complete **end-to-end machine learning lifecycle** using Azure Machine Learning.

It shows how a model can move from:

**Raw Data → Data Preparation → KNN Training → Evaluation → AutoML → Designer → Model Registration → Deployment → Real-Time Prediction → Cleanup**

The project combines **Machine Learning, Cloud Computing, and MLOps practices** in a single practical workflow.
