# 📰 AI-Powered News Summarizer
![GitHub Repo](https://img.shields.io/badge/Status-Active-brightgreen) ![License](https://img.shields.io/badge/License-MIT-blue) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange)

🚀 **AI-Powered News Summarizer** is a **Streamlit-based web app** that extracts text from online news articles and generates concise summaries using **Hugging Face NLP models** like BART, Pegasus, and T5.

---

## 📌 **Features**
✅ **Extracts Full Article Content** from URLs  
✅ **Supports Manual Text Input**  
✅ **AI-Powered Summarization** using **Hugging Face Models**  
✅ **Supports Three Different Models** (BART, Pegasus, T5)  
✅ **Highlights the Most Important Sentence**  
✅ **Fully Responsive UI with Streamlit**  

---

## 🚀 **Getting Started**

### 📂 **1. Clone the Repository**
```bash
git clone https://github.com/basavaadarsh/AI-Powered-News-Paper-Summerizer.git
cd AI-Powered-News-Paper-Summerizer
```
### 📦 **2. Install Dependencies**
Ensure you have Python 3.8+ installed, then install required packages:

```
pip install -r requirements.txt
```
### 🔑 **3. Set Up Hugging Face API Key**
1. **Create a Hugging Face account**: [Sign Up Here](https://huggingface.co/join)
2. **Generate an API Key**:
   - Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Click **"New API Token"**
   - Copy the generated API Key.
3. **Store the API Key Securely**:
   - Open the `.env` file in the project folder.
   - Paste the key inside it like this:
     
     ```ini
     HUGGINGFACE_API_KEY=your_actual_hugging_face_api_key
     ```
     
⚠️ **DO NOT SHARE YOUR API KEY PUBLICLY!**  
Ensure `.env` is in `.gitignore` to prevent exposure.

### 🎯 **Running the Application**
To launch the **Streamlit web app**, run:

```bash
streamlit run news_summarizer.py
```
This will start the AI-Powered News Summarizer in your browser at:
```
http://localhost:8501
```

### 📸 **Screenshots**

![image](https://github.com/user-attachments/assets/f1543fff-d198-4520-a1e6-10782573c064)

![image](https://github.com/user-attachments/assets/b46c69fd-cf60-4826-94bd-456ba70a9431)


### ⚙️ **How It Works**
1️⃣ **Enter** a news article **URL** or **paste text manually**  
2️⃣ **Select** an AI model from **BART, Pegasus, or T5**  
3️⃣ **Adjust** summary length settings  
4️⃣ **Click** **Summarize Text**  
5️⃣ **Get** a **concise summary** with **highlighted important points**  

---

### 🛠 **Tech Stack**
- **Python 3.8+**
- **Streamlit** (Web UI)
- **Newspaper3k** (Article Extraction)
- **BeautifulSoup** (HTML Parsing)
- **Hugging Face Transformers API** (Summarization)
- **dotenv** (Environment Variable Management)

### ❗ Troubleshooting

🔴 **1. ModuleNotFoundError: No module named 'streamlit'**

   Run: `pip install -r requirements.txt`

   If issue persists: `pip install streamlit`

🔴 **2. API Not Working or KeyError: 'HUGGINGFACE_API_KEY'**

   Ensure `.env` file is created and the `HUGGINGFACE_API_KEY` is correctly set within the `.env` file.

   Restart the terminal and run: `streamlit run news_summarizer.py`

🔴 **3. requests.exceptions.RequestException: API Rate Limit Exceeded**

   Free-tier users have rate limits. Try again later or upgrade to a paid Hugging Face plan.

### 👨‍💻 Contributing

🎉 We welcome contributions!

If you have ideas or improvements, follow these steps:

1.  Fork this repository.
2.  Clone it to your local machine.
3.  Create a new branch (`git checkout -b feature-xyz`).
4.  Make your changes and commit.
5.  Push to your fork and submit a Pull Request.

### 📜 License

🔖 This project is licensed under the MIT License.

See [LICENSE](LICENSE) for more details.

## 📬 **Contact**
If you have any questions or feedback, feel free to reach out:

📧 **Email:** [basavaadarsh4@gmail.com](mailto:basavaadarsh4@gmail.com)  
🔗 **LinkedIn:** [Adarsh](https://www.linkedin.com/in/nelavalli-basava-adarsh-3598b916a/)

⭐ **If you like this project, consider giving it a star on GitHub!** ⭐

