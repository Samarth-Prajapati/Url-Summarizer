# URL Summarizer (YouTube & Website)

A **Generative AI application** that summarizes content from **YouTube videos or website URLs** into concise bullet-point summaries using an LLM.  
The application extracts text from the provided URL and generates a **structured summary (≤300 words)**.

The interface is built with **Streamlit**, and summarization is powered by **LangChain with Groq LLMs**.

---

## Features

- Summarize **YouTube videos**
- Summarize **web articles or blogs**
- Generates **bullet-point summaries**
- Uses **Groq LLM for fast inference**
- Automatic **text splitting for large content**
- Simple **Streamlit UI**
- Secure **API key input from sidebar**

---

## Project Architecture

```cmd
URL
 │
 ▼
Content Loader
 (YouTube / Website)
 │
 ▼
LangChain Summarization Chain
 │
 ▼
Groq LLM
 │
 ▼
Bullet-Point Summary
```

---

## Project Structure

```cmd
Url-Summarizer
│
├── .venv
│
├── UrlSummarizer
│   │
│   ├── loaders
│   │   ├── __init__.py
│   │   └── url_loader.py
│   │
│   ├── services
│   │   ├── __init__.py
│   │   └── summarizer.py
│   │
│   └── prompts
│       ├── __init__.py
│       └── summary_prompt.py
│
├── main.py
├── pyproject.toml
├── poetry.lock
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Python Version

This project was developed and tested using:

```
Python 3.13
```

---

## Installation & Setup

Follow the steps below to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-summarizer.git
cd Url-Summarizer
```

---

### 2. Create Virtual Environment

Create a virtual environment using Python.

```bash
python -m venv .venv
```

---

### 3. Activate Virtual Environment

#### Mac / Linux

```bash
source .venv/bin/activate
```

#### Windows

```bash
.venv\Scripts\activate
```

---

### 4. Install Dependencies

Install all required libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application

Start the Streamlit application.

```bash
streamlit run main.py
```

The application will open automatically in your browser.

---

## How to Use

1. Open the application.
2. Enter your **Groq API Key** in the sidebar.
3. Paste a **YouTube URL or Website URL**.
4. Click the **Summarize** button.
5. The system will generate a **bullet-point summary**.

---

## Example URLs

You can test the application using:

```
https://www.youtube.com/watch?v=example
```

or

```
https://example.com/blog/article
```

---

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq LLM
- YouTube Transcript API
- RecursiveCharacterTextSplitter

---

## Limitations

- Some websites block scraping.
- Videos without transcripts cannot be summarized.
- Very large content may take longer to process.

---

## Future Improvements

- Multi-language summarization
- Streaming responses
- Vector database integration for long documents
- Support for PDF or document uploads
- Model selection options

---

