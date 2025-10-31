# 🧠 Mental Health Support Chatbot

An AI-powered chatbot that detects emotions from user text and responds empathetically — built using **Streamlit** and **Transformers (DistilRoBERTa)**.

---

## 💡 Overview

This project uses **Natural Language Processing (NLP)** to analyze user input, identify the underlying **emotion**, and provide a comforting or encouraging response based on that emotion.

It’s designed to promote emotional awareness and mental well-being through simple, non-judgmental interactions.

---

## 🧩 Features

- 🧠 **Emotion Detection:** Identifies emotions like *joy, sadness, anger, fear, surprise, love, neutral*  
- 💬 **Empathetic Responses:** Gives supportive replies tailored to the detected emotion  
- ⚡ **Fast & Lightweight:** Uses `@st.cache_resource` to optimize model loading  
- 🎨 **Modern Web UI:** Clean, minimalist interface built with Streamlit  
- 🛡️ **Safe Support Tool:** Intended for awareness and support — not medical advice  

---

## 🧱 Tech Stack

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Streamlit** | For creating the interactive web app |
| **Transformers** | To access pre-trained emotion detection models |
| **DistilRoBERTa** | Emotion classification model by *J. Hartmann* |

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/mental_health_chatbot.git
   cd mental_health_chatbot

#Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows

#Install dependencies

pip install -r requirements.txt

#Run the app

streamlit run app.py



🧑‍💻 Developer

👨‍💻 Atharva K. A.
B.E. in Artificial Intelligence & Machine Learning
Sir M. Visvesvaraya Institute of Technology, Bengaluru

⚠️ Disclaimer

This chatbot is designed for emotional support and awareness only.
It is not a replacement for professional mental health care or therapy.