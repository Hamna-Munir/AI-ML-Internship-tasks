# 🫀 Task 3: Heart Disease Prediction using Machine Learning

## 🎯 Objective  
To predict whether a person is at risk of heart disease using classification models trained on clinical health data.

---

## 📊 Dataset
- **Name:** Heart Disease UCI (Cleveland)  
- **Source:** [Kaggle](https://www.kaggle.com/datasets)  
- **File:** `heart.csv`  
- **Features:** age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal  
- **Target:** condition (1 = Heart Disease, 0 = No Disease)

---

## 🛠️ Steps Performed
1. Loaded the dataset using pandas.
2. Checked for missing values and data types.
3. Renamed the target column from `condition` (if needed).
4. Performed Exploratory Data Analysis:
   - 📊 Count plot of target classes
   - 🔥 Correlation heatmap of features
5. Split data using `train_test_split()` (80/20).
6. Applied `StandardScaler` for normalization.
7. Trained models:
   - 🔹 Logistic Regression
   - 🔸 Decision Tree Classifier
8. Evaluated using:
   - ✅ Accuracy
   - 🧮 Confusion Matrix
   - 📈 ROC-AUC Curve
9. Visualized feature importance from both models.

---

## 🔍 Final Observations
- Age, thalach (max heart rate), and oldpeak were strong predictors.
- Logistic Regression gave smoother ROC curves and better generalization.
- Decision Tree offered more interpretability but may overfit without pruning.

---

## 💻 Tools Used
- Python 3 (Jupyter Notebook)
- pandas, numpy
- seaborn, matplotlib
- scikit-learn (LogisticRegression, DecisionTreeClassifier, metrics)

---

## 📁 Files
- `heart.csv` — Cleaned dataset file  
- `heart_disease_prediction.ipynb` — Complete code, visualizations, and model results  
- `README.md` — This documentation

---

## 🙌 Author
**Hamna Munir** – AI/ML Engineering Intern – 2025


