# 🗂️ Docs That Talk Back

**An exploration into using Retrieval Augmented Generation (RAG) to talk to your documentation.**

## 🚀 Overview

Reading documentation to find the specific information you're looking for can be a time-consuming task, especially if it's not well-organized.

So, what if we could talk to our documentation and ask for the information we're looking for?

This project explores how we can use modern language models to extract meaningful answers from our documents without having to manually search or read through them.

## 📁 Project Structure

```
rag-demo/
├── sample_data/
├── src/
│   ├── app/
│   │   └── app.py
│   ├── config/
│   │   └── settings.py
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── prompt.py
│   │   ├── query.py
│   │   └── store.py
│   └── utils/
│       └── log.py
```

## 🛠 Tools Used

| Tool         | Purpose                                        |
|--------------|------------------------------------------------|
| `uv`         | Project management |
| `openai`     | Embedding + completion |
| `chromadb`   | Vector database |
| `streamlit`  | Web-based UI |
| `ruff`       | Linting and formatting                         |



## ▶️ How to Run the App

Make sure you've installed [`uv`](https://github.com/astral-sh/uv), and have a valid `.env` file with your OpenAI API key. Check out the `.env.example` file for reference.

Then run:

```bash
uv run --env-file .env py -m streamlit run ./src/app/app.py
```



## 🎯 What This Project Demonstrates

This demo app walks through the entire RAG pipeline:

1. **Ingestion**  
   - Splits documents into chunks  
   - Embeds them using OpenAI embeddings model
   - Stores them in a Chroma vector database  

2. **Retrieval & Generation**  
   - Embeds the user's question
   - Performs similarity search in the vector store  
   - Builds a grounded prompt  
   - Uses open AI completion model to generate a response


## 🧠 Key Learnings

- LLMs **without retrieval** will hallucinate, especially when answering questions about your specific data
- RAG lets us ground our models with **live, eternal data**, without having to train them ourselves.
- You don't need fine-tuning to get powerful, contextual responses



## 💡 Why Not Just Use ChatGPT?

> _Can't I just paste my document into ChatGPT?_

For small docs, ChatGPT can do this, but it has some big limitations. RAG gives you:
- ✅ Scalability, using semantic filtering to retrieve only relevant chunks of context
- ✅ Support for large documents
- ✅ The ability to build real applications on top of it
- ✅ Fine-grained control over prompts and generated responses

## 🧪 Try It with Your Own Docs

Use the web interface to import text file. I've currently tested it with `.txt` and `.md` file types, but it probably works with others. The uploaded documents will be ingested and then you can ask it any questions!


## 📬 Questions or Comments?

Feel free to reach out if you have any questions or if you want to chat about this project.

Happy coding!
