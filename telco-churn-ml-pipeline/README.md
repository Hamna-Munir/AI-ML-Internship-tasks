# Telco Churn ML Pipeline

This project is an end-to-end machine learning pipeline for predicting customer churn using the **Telco Customer Churn Dataset**. It includes data preprocessing, model training, hyperparameter tuning, and model export using Scikit-learn.

---

## 📁 Files Included

| File                          | Description                                        |
|-------------------------------|----------------------------------------------------|
| `telco_churn_pipeline.ipynb`  | Full Google Colab notebook with pipeline code      |
| `telco_churn_pipeline.pkl`    | 🔗 [Download from Google Drive](https://drive.google.com/file/d/1dD6o8G4AEwF0oh4EJRtFFa8BaTGqQqdn/view?usp=sharing) |
| `telco_churn.csv`             | Cleaned dataset used for training (from Kaggle)    |

---

## 📊 Dataset Overview

- **Source**: [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Records**: 7,032 customer entries
- **Features**:
  - Demographics (e.g., gender, senior citizen, partner)
  - Services (e.g., internet service, phone service)
  - Account info (e.g., tenure, payment method)
  - Target: `Churn` (Yes/No)

---

## ⚙️ Pipeline Workflow

1. **Data Cleaning**
   - Converted `TotalCharges` to numeric
   - Removed rows with missing values

2. **Preprocessing**
   - Categorical: OneHotEncoder
   - Numerical: StandardScaler

3. **Modeling**
   - Trained with Random Forest and Logistic Regression
   - Tuned using GridSearchCV

4. **Model Export**
   - Saved using `joblib` for reusability

---

## 🚀 How to Run the Project in Google Colab

1. Open the notebook: `telco_churn_pipeline.ipynb`
2. Upload the dataset: `telco_churn.csv`
3. Run all cells
4. Download or load the saved model as shown below

---

## 🔗 Download Trained Model

The trained model is saved externally due to GitHub's 25MB limit.

👉 [Download `telco_churn_pipeline.pkl`](https://drive.google.com/file/d/1dD6o8G4AEwF0oh4EJRtFFa8BaTGqQqdn/view?usp=sharing)

---

### 📦 How to Use the Trained Model

After downloading the `.pkl` file:

```python
import joblib

# Load the model
model = joblib.load("telco_churn_pipeline.pkl")

# Predict new customer churn
# new_data must match the training schema
prediction = model.predict(new_data)
🧰 Requirements
Python 3.7+

pandas

scikit-learn

joblib

Install all dependencies using:

pip install pandas scikit-learn joblib
🤝 Contributed by
Hamna Munir
AI/ML Intern | July 2025
