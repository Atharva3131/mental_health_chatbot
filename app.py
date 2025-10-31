import streamlit as st
from transformers import pipeline

# Set up Streamlit page
st.set_page_config(page_title="🧠 Mental Health Support Chatbot", layout="centered")
st.markdown("<h1 style='text-align: center;'>💬 Mental Health Support Chatbot</h1>", unsafe_allow_html=True)

# Sidebar info
st.sidebar.write("👨‍💻 Developed by Atharva K. A.")
st.sidebar.metric("Model", "DistilBERT Emotion Classifier")
st.sidebar.markdown("---")
st.sidebar.write("This chatbot detects emotion and responds empathetically.")

# Load pretrained model from Hugging Face
@st.cache_resource
def load_model():
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

emotion_model = load_model()

# Empathetic responses for each emotion
responses = {
    "joy": "That's wonderful to hear! 😊 Keep enjoying those positive vibes!",
    "anger": "It’s okay to feel angry sometimes. Take a deep breath, step back, and give yourself space to calm down. 🕊️",
    "sadness": "I'm really sorry you’re feeling sad. 💙 Remember, tough times pass, and talking to someone can really help.",
    "fear": "Fear often signals uncertainty. You’re stronger than you think. Try grounding yourself in the present moment. 🌱",
    "surprise": "Life sure has its twists! 🎢 Hope it was a good kind of surprise.",
    "love": "That’s so sweet! 💖 Love and kindness make life truly special.",
    "neutral": "Got it 👍. I’m here if you want to talk more about how you feel."
}

# Chat input area
st.markdown("### 🗣️ How are you feeling today?")
user_input = st.text_area("Type your thoughts here...", placeholder="e.g. I’ve been feeling low lately and anxious about studies...")

if st.button("Analyze Emotion"):
    if user_input.strip() != "":
        result = emotion_model(user_input)[0]
        emotion = result['label'].lower()
        score = round(result['score'] * 100, 2)

        st.markdown(f"### 🧩 Detected Emotion: **{emotion.capitalize()}** ({score}% confidence)")
        st.markdown(f"**Chatbot Response:** {responses.get(emotion, 'I understand. Emotions can be complex, and it’s okay to feel that way.')}")
    else:
        st.warning("Please type something to analyze your emotion!")

# Footer
st.markdown("---")
st.caption("💡 *Disclaimer: This chatbot is for emotional support and awareness, not medical advice.*")
