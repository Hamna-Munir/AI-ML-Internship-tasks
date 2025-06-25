# 📈 Task 2: Predict Future Stock Prices (Short-Term)

## 🎯 Objective
Use historical stock data from Yahoo Finance to predict the **next day's closing price** using machine learning regression models.

---

## 🗂 Dataset
- **Source:** Yahoo Finance API (via `yfinance` library)
- **Stock Used:** Apple Inc. (`AAPL`)
- **Features:** Open, High, Low, Volume
- **Target:** Next day's Close price

---

## 🛠 Tools and Libraries
- Python 3
- [yfinance](https://pypi.org/project/yfinance/)
- pandas, numpy
- scikit-learn (Linear Regression, Random Forest)
- matplotlib, seaborn

---

## 🔍 Workflow

1. **Data Loading**: Fetch stock data using `yfinance`
2. **Feature Engineering**: Use today's data to predict next day's close
3. **Train-Test Split**: 80/20 time-based split (no shuffle)
4. **Modeling**:
   - Linear Regression
   - Random Forest Regressor
5. **Evaluation**:
   - RMSE
   - R² Score
6. **Visualization**:
   - Actual vs Predicted Closing Prices

---

## ✅ Results

| Model             | RMSE (↓) | R² Score (↑) |
|------------------|----------|--------------|
| Linear Regression|  ✨X.XX✨   |  ✨0.XX✨       |
| Random Forest     |  ✅X.XX✅   |  ✅0.XX✅       |

✅ *Random Forest performed better in capturing patterns.*

---

## 📁 Files Included
- `predict_stock_price_task2.ipynb`: Complete notebook with code and plots
- `README.md`: This file

---

## 👩‍💻 Author
Hamna Munir  
AI/ML Internship Task — 2025

---

## 📎 Keywords
`Machine Learning`, `Stock Prediction`, `Regression`, `Random Forest`, `yfinance`, `Internship Task`, `AI ML`
