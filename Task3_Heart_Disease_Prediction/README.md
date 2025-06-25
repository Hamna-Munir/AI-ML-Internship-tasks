📈 Task 3: Predict Heart Disease Risk (Classification)

🎯 Objective  
Build a machine learning model to predict whether a patient is at risk of heart disease using clinical health data.

🗂 Dataset  
Source: UCI Heart Disease Dataset (Cleveland)  
File Used: `heart.csv`  
Features: Age, Sex, Chest Pain Type, Resting BP, Cholesterol, Fasting Blood Sugar, Rest ECG, Max Heart Rate, Exercise Angina, Oldpeak, Slope, CA, Thal  
Target: `condition` (1 = Heart Disease, 0 = No Disease)

🛠 Tools and Libraries  
- Python 3  
- pandas, numpy  
- scikit-learn (Logistic Regression, Decision Tree Classifier)  
- matplotlib, seaborn  

🔍 Workflow  
1. **Data Loading**: Load and inspect heart.csv  
2. **Data Cleaning**: Check for missing values  
3. **EDA**: Visualize trends, correlations, and target distribution  
4. **Feature Engineering**: Prepare features and scale them  
5. **Train-Test Split**: 80/20 split using `train_test_split()`  
6. **Modeling**:
   - Logistic Regression  
   - Decision Tree Classifier  
7. **Evaluation**:
   - Accuracy  
   - Confusion Matrix  
   - ROC-AUC Score  
8. **Feature Importance**: Identify key risk factors

✅ Results  
Model | Accuracy | AUC Score  
------|----------|-----------  
Logistic Regression | ✨X.XX✨ | ✨0.XX✨  
Decision Tree | ✅X.XX✅ | ✅0.XX✅  

✅ Logistic Regression provided more stable results, while Decision Tree highlighted key feature importance effectively.

📊 Visualization  
- Confusion Matrices  
- ROC Curve  
- Feature Importance Plots

📁 Files Included  
- `heart.csv`: Cleaned dataset  
- `heart_disease_prediction.ipynb`: Complete notebook with code and visuals  
- `README.md`: This file  

👩‍💻 Author  
Hamna Munir  
AI/ML Internship Task — 2025  

📎 Keywords  
Machine Learning, Heart Disease, Classification, Logistic Regression, Decision Tree, Internship Task, AI ML
