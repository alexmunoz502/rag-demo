import streamlit as st
from src.ingest import ingest_text
from src.query import query_docs

st.set_page_config(page_title="RAG Demo", page_icon="📚")

st.title("📖 RAG Demo App")

# === Upload & Ingest ===
st.header("1. Upload Document")
uploaded_file = st.file_uploader("Choose a .txt or .md file", type=["txt", "md"])

if uploaded_file:
    filename = uploaded_file.name

    # Use session state to track whether or not this has already been ingested
    if "ingested_files" not in st.session_state:
        st.session_state.ingested_files = set()

    if filename not in st.session_state.ingested_files:
        text = uploaded_file.read().decode()
        ingest_text(text=text, source_id=filename)
        st.session_state.ingested_files.add(filename)
        st.success(f"✅ Document '{filename}' ingested!")
    else:
        st.info(f"📁 Document '{filename}' already ingested.")

# === Ask Question ===
st.header("2. Ask a Question")
question = st.text_input("What do you want to know?")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = query_docs(question)  # Your existing query function
            st.markdown("### 🧠 Answer")
            st.write(answer)
