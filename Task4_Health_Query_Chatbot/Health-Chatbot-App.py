from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import gradio as gr

# Load model and tokenizer
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
chatbot = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

# Chatbot function with safety filter
def health_chatbot(category, user_question):
    example_questions = {
        "Illnesses & Symptoms": "What causes a sore throat?",
        "Medicines": "Is paracetamol safe for children?",
        "Nutrition & Diet": "Which foods help improve immunity?",
        "Lifestyle & Wellness": "How much sleep does an adult need?",
        "Doctor Visits": "When should I see a doctor for a headache?"
    }
    unsafe_keywords = ["suicide", "kill", "overdose", "die", "harm", "self-harm"]
    if any(word in user_question.lower() for word in unsafe_keywords):
        return "⚠️ I'm not able to respond to that. Please contact a medical professional or helpline immediately."

    if category != "Custom" and not user_question.strip():
        user_question = example_questions.get(category, "")

    prompt = f"Act like a friendly health assistant. Give general information only. Question: {user_question}"
    result = chatbot(prompt)
    return result[0]["generated_text"]

# Gradio UI
categories = ["Illnesses & Symptoms", "Medicines", "Nutrition & Diet", "Lifestyle & Wellness", "Doctor Visits", "Custom"]

with gr.Blocks() as demo:
    gr.Markdown("## 🏥 Health Chatbot with Categories")
    category = gr.Radio(choices=categories, label="Select Category", value="Illnesses & Symptoms")
    user_input = gr.Textbox(label="Your Question (optional)", lines=2)
    output = gr.Textbox(label="Response")
    submit = gr.Button("Ask")
    submit.click(fn=health_chatbot, inputs=[category, user_input], outputs=output)

# Launch public link
demo.launch(share=True)
