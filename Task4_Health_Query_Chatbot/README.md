# 🧠 Task 4: General Health Query Chatbot (Prompt Engineering Based)

## 🎯 Objective  
To create a chatbot that can answer general health-related questions using a Large Language Model (LLM) with prompt engineering and safety filters.

---

## 🗂️ Dataset / Model
- **Model Used:** Mistral-7B-Instruct (or any open LLM like DistilGPT2)
- **Source:** Hugging Face Transformers Hub
- **API Use (Optional):** OpenAI GPT-3.5 (with API key)
- **Pipeline:** Text generation with prompt conditioning

---

## 🛠️ Steps Performed
1. Initialized Hugging Face Transformers pipeline.
2. Loaded tokenizer and causal LLM (e.g., DistilGPT2 or Mistral-7B).
3. Applied prompt engineering:
   - 💬 Prompt: “You are a helpful and safe medical assistant. Please answer clearly.”
4. Created a chatbot function to process queries and format replies.
5. Added basic safety checks (e.g., avoid harmful suggestions).
6. Built a full Gradio UI web app with:
   - ✅ User input textbox
   - ✅ Live chat interface
7. Exported as `.py` file and `.bat` launcher for desktop use.

---

## 💬 Example Queries to Try
- “What causes a sore throat?”
- “Is paracetamol safe for children?”
- “How much water should I drink daily?”
- “What are symptoms of vitamin D deficiency?”
- “Can I drink milk during a cold?”

⚠️ **Note:** Always consult a licensed doctor for medical advice.

---

## 💻 Tools Used
- Python 3.10  
- 🤗 Transformers  
- 🧠 Pretrained LLM (Mistral-7B / DistilGPT2)  
- 🎨 Gradio for UI  
- Torch (backend support for model inference)

---

## 📁 Files
- `Health-Chatbot-App.py` — Full chatbot code with Gradio interface  
- `Run_Health_Chatbot.bat` — One-click launcher for Windows  
- `README.md` — This documentation file  

---

## 🌐 Deployment
- Works locally with public Gradio URL
- Can be run in:
  - Google Colab
  - Jupyter Notebook
  - VS Code / Terminal (Python script)

---

## 🙌 Author
**Hamna Munir** – AI/ML Engineering Intern – 2025
