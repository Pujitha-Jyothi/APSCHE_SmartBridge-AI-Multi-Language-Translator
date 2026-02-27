from dotenv import load_dotenv
import streamlit as st
import os
from google import genai

# Streamlit page config
st.set_page_config(page_title="AI-Powered Language Translator", page_icon="🌐")
st.header("🌐 AI-Powered Language Translator")

# Load environment file (custom name: code.env)
load_dotenv(dotenv_path="code.env")

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("API Key not found. Please check your code.env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Translation function
def translate_text(text, source_language, target_language):
    prompt = f"Translate the following text from {source_language} to {target_language}: {text}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text

def main():
    text = st.text_area("📝 Enter text to translate:")

    source_language = st.selectbox(
        "🌐 Select source language:",
        ["English", "Spanish", "French", "German", "Chinese"]
    )

    target_language = st.selectbox(
        "🎯 Select target language:",
        ["English", "Spanish", "French", "German", "Chinese"]
    )

    if st.button("🔁 Translate"):
        if text:
            try:
                translated_text = translate_text(text, source_language, target_language)
                st.subheader("📘 Translated Text:")
                st.write(translated_text)
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")
        else:
            st.warning("⚠️ Please enter text to translate.")

if __name__ == "__main__":
    main()
