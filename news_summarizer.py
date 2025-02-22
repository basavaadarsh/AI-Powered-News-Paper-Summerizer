import streamlit as st
import requests
from newspaper import Article
from bs4 import BeautifulSoup
import validators
import time
import heapq  
import os
from dotenv import load_dotenv  # Import dotenv

st.set_page_config(page_title="AI News Summarizer", layout="wide")

# Load environment variables from .env file
load_dotenv()

# Hugging Face API Key from .env
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not HUGGINGFACE_API_KEY:
    st.error("❌ API Key is missing! Please add it to the .env file.")

API_URL = "https://api-inference.huggingface.co/models/"

# Summarization Models
SUMMARIZATION_MODELS = {
    "BART (Stable)": "facebook/bart-large-cnn",
    "Pegasus (Best for News)": "google/pegasus-xsum",
    "T5-Large (Best for Long Docs)": "t5-large",
}

# Algorithm descriptions
ALGORITHM_DETAILS = {
    "Pegasus (Best for News)": "Transformer-based NLP Model (Pre-trained Pegasus, optimized for news summarization)",
    "BART (Stable)": "Bidirectional Auto-Regressive Transformer (Pre-trained BART, works well for general summarization)",
    "T5-Large (Best for Long Docs)": "Text-To-Text Transfer Transformer (T5) (General NLP model with strong summarization ability)"
}

# Validate and Fetch News Article Text
def fetch_article(url):
    """Validates the URL and fetches article text using Newspaper3k or BeautifulSoup."""
    
    if not validators.url(url):
        return "❌ Error: Invalid URL. Please enter a proper link starting with http:// or https://"

    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                paragraphs = soup.find_all("p")
                full_text = "\n".join([p.get_text() for p in paragraphs])
                return full_text if full_text else "❌ Error: Could not extract article text."
            else:
                return f"❌ Error: Failed to fetch article (Status Code: {response.status_code})"
        except Exception as e:
            return f"❌ Error: Could not fetch article. {str(e)}"

# Summarize Large Text
def summarize_large_text(text, model, min_length, max_length):
    chunks = [text[i:i+3000] for i in range(0, len(text), 3000)]
    summaries = []
    for i, chunk in enumerate(chunks[:2]):  
        summary = summarize_text(chunk, model, min_length, max_length)
        summaries.append(summary)
    return " ".join(summaries)

# Summarize Text
def summarize_text(text, model, min_length, max_length):
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {
        "inputs": text[:1500],
        "parameters": {"max_length": max_length, "min_length": min_length, "do_sample": False, "temperature": 0.6}
    }

    try:
        response = requests.post(API_URL + model, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and len(result) > 0:
            return result[0].get("summary_text") or result[0].get("generated_text", "❌ No summary returned.")
        return "❌ Unexpected API Response Format."
    except requests.exceptions.RequestException as e:
        return f"❌ API Error: {str(e)}"

# Extract Important Sentence from Summary
def extract_important_sentence(summary):
    """Extracts the most important sentence from the AI-generated summary"""
    sentence_list = summary.split('. ')  
    word_frequencies = {}

    for word in summary.split():
        word = word.lower()
        word_frequencies[word] = word_frequencies.get(word, 0) + 1

    sentence_scores = {}
    for sentence in sentence_list:
        for word in sentence.lower().split():
            if word in word_frequencies and len(sentence) < 250:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    if sentence_scores:
        return max(sentence_scores, key=sentence_scores.get)
    return None

# Streamlit UI Layout
st.title("📰 AI-Powered News Summarizer")

st.sidebar.title("⚙️ Settings")
model_choice = st.sidebar.selectbox("🔍 Choose a Model", list(SUMMARIZATION_MODELS.keys()))
st.sidebar.markdown(f"🧠 **Algorithm Used:** {ALGORITHM_DETAILS[model_choice]}")
min_length = st.sidebar.slider("📏 Min Length", 30, 300, 50)
max_length = st.sidebar.slider("📏 Max Length", 50, 600, 150)

url = st.text_input("🔗 Enter News Article URL", "")
manual_text = st.text_area("📌 OR Paste News Article Text Below:")

# Checkbox for Highlighting Important Sentences
highlight_button = st.checkbox("🔍 Highlight Important Point")

if st.button("Summarize Text"):
    progress_bar = st.progress(0)
    with st.spinner("⏳ Fetching and summarizing..."):
        article_text = manual_text if manual_text else fetch_article(url)

        if "Error" in article_text:
            st.error(article_text)
        else:
            progress_bar.progress(30)

            summary = summarize_large_text(article_text, SUMMARIZATION_MODELS[model_choice], min_length, max_length)
            progress_bar.progress(70)

            important_sentence = extract_important_sentence(summary)
            if important_sentence:
                highlighted_summary = summary.replace(
                    important_sentence,
                    f'<span style="background: rgba(255, 255, 0, 0.5); padding: 4px; border-radius: 5px;">{important_sentence}</span>'
                )
            else:
                highlighted_summary = summary

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("📰 Full Article (First 1000 Characters)")
                st.write(article_text[:1000] + "...")

            with col2:
                st.subheader("✍️ AI-Generated Summary")
                st.markdown(f"<div>{highlighted_summary}</div>", unsafe_allow_html=True)

            progress_bar.progress(100)
            progress_bar.empty()

st.markdown("🚀 **Developed By Team Cobra Techs**")
