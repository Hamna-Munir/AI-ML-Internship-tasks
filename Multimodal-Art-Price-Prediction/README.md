# 🎨 Multimodal Art Price Prediction

This project predicts the **sale price of Andy Warhol artworks** using both:

- 🧮 **Tabular features** (purchase price, appreciation, etc.)
- 🖼️ **Image features** (extracted from artwork images using CNN)

---

## 📊 Dataset

We used the **Million Dollar Art Market Dataset** filtered for Andy Warhol's artworks.

📁 CSV File Used: `artworks_andy_warhol.csv`  
📸 Images were pulled using the `image_url` column from the dataset.

---

## 🚀 Model

We trained a `RandomForestRegressor` using combined tabular and image features.

✅ Evaluation:
- **MAE**: 💰 ~X USD
- **RMSE**: 💰 ~Y USD

---

## 📥 Load Trained Model

The model is saved inside this GitHub repository.

📁 File: `art_price_multimodal_model.pkl`

To load it:

```python
import joblib

# Load the model
model = joblib.load("art_price_multimodal_model.pkl")

# Predict new artwork price
# Ensure input matches training schema
# prediction = model.predict(new_data)
📦 Requirements
Python 3.7+

pandas

numpy

matplotlib

scikit-learn

joblib

Install them with:


pip install pandas numpy matplotlib scikit-learn joblib

👩‍💻 Contributed by
Hamna Munir
AI/ML Intern — July 2025
