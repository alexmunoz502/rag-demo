# Docs That Talk Back

### An exploration into using Retrieval Augmented Generation to talk to your documentation

## Table of Contents

1. Introduction
2. Limitations of LLMs
3. What is RAG?
4. How does RAG work?
5. Let's build a RAG
6. Technical Highlights
7. Live Demo
8. The Power of RAGs
9. Applications
10. Conclusion

## 1. Introduction

Reading documentation to find the specific information you're looking for can be a time-consuming task, especially if it's not well-organized.

So, what if we could talk to our documentation and ask for the information we're looking for?

This project explores how we can use modern language models to extract meaningful answers from our documents without having to manually search or read through them.

At its core, this project is an answer to the following question:

How can we use natural language to query any document and get back accurate, useful answers?

We might think about using a tool like ChatGPT or Claude, but large language models like these have some limitations.

## 2. Limitations of LLMs

LLMs like GPT-4 are great at generating sophisticated responses. However, they can't fully solve our problem for a few reasons:

1. They aren't aware of our data. Without context, they can't answer questions about our documentation.
2. They hallucinate. LLMs are trained to generate realistic sounding text, but this means it's not always accurate.
3. They have memory limitations. Even if we pass all of our documents for context, eventually we will run out of memory.

So, if we can't just use ChatGPT, how can we talk to our language models about our docs and get grounded answers?

The answer is Retrieval Augmented Generation!

## 3. What is Retrieval Augmented Generation (RAG)?

Retrieval Augmented Generation is a technique that improves the quality and accuracy of generative AI models by grounding them in external data sources.

These data sources can be things like documentation, databases, or even emails.

At runtime, we retrieve relevant context from these data sources, and insert it into our prompts. Then, instead of generating text solely based on its training data, our LLM will generate responses that are grounded in our data.

One important clarification here is that we're not training a model on our data, but instead giving it the context at runtime for it to accurately generate text.

This all sounds great, but how do we actually do this?

## 4. How does RAG work?

There are two main parts to RAG systems:

1. Ingestion
2. Retrieval + Generation

### Ingestion:

In this step, we're working towards formatting our data in a way that our system can understand. When we retrieve data, we want to make sure we're only fetching data that is relevant to the user's query.

To do this we need to chunk our data into overlapping sections, and pass each chunk to an embedding model that will generate a vector representation of that chunk.

These vectors are stored in a specialized vector database that can handle similarity search.

_NOTE: The degree to which chunks overlap is arbitrary and should be tuned for your use case._

### Retrieval:

When the user asks a question, the query is passed through the same embedding model from our ingestion step. Then, we can perform a similarity search in our database to retrieve the top K most relevant chunks.

_NOTE: K here is an arbitrary value that you can play around with depending on system._

Once we have our relevant chunks pulled, we can insert them into a prompt that is engineered to provide the context, instructions for staying grounded, and guard rails to prevent hallucinations and answering irrelevant queries.

Lastly, the LLM uses the prompt to generate a grounded, contextualized response.

## 5. Let's Build a RAG

Now that we understand what RAG is and how it works, how can we use it to solve our problem?

We'll start by using our documentation as our source data for the ingestion step. We'll split our data into arbitrarily sized chunks and generate vector representations with our embedding model. Both the vectors and the chunks will then be stored in a vector database.

After our document is ingested, we'll let the user write natural language queries, which will get converted by our embedding model into vectors we can use for our database query.

We'll create a prompt that will contain both our context results from the database query, and instructions on how to behave. These instructions will explain to our LLM how to use the provided context to answer questions, adding guard rails to ensure it doesn't deviate from its purpose or hallucinate.

Finally, we'll write the LLM's generated response back to the user, completing the task.

## 6. Technical Highlights

- For our vectorized DB, we'll use ChromaDB
- For simplicity, we'll use OpenAI's python API to utilize OpenAI's models for embedding and text generation.
- For quick user interface, we'll use python Streamlit library
- I've prepared some sample data we can use to test out the app

Other notes to work in:

- How models can affect results (GPT3.5 vs 4.1)
- Include code snippets from the app here, really get into the nitty gritty details

## 7. Live Demo

Show off the rag demo and how it can be used to talk to documentation.

## 8. The Power of RAGs

As you can see, with just a few components, we were able to create a system that lets us talk to our documentation using natural language!

## 9. Applying RAG to the Productivity space

While this demo focused on documentation, I've thought about how these concepts could be applied to productivity tools.

For example, RAG could enable natural language interfaces for a variety of apps:

- Notes: "Can you summarize my notes on the project?"
- Calendars: "What's my availability next week?"
- Tasks: "What are my priorities for today?"

RAG is great for understanding personalized data, which is at the heart of many productivity tools.

## 10. Conclusion

Retrieval Augmented Generation is one of my favorite applications of AI. It's a simple concept, but incredibly powerful in action.

By grounding LLMs with real data, we can generate responses that are accurate and useful.

In the demo, we saw how RAG can be used to talk to our documentation, but the applications of this tech are limitless.

## Q&A

### Why not just copy and paste my document into ChatGPT and give it the same prompt?

- This does a good job at EMULATING the process of a RAG, and works perfectly fine for small form content.
- You're dumping a haystack and asking it to search for the needles
- Rag adds semantic filtering so GPT doesn't have to read everything
- This breaks down when using larger documents. You can't fit the whole thing into chat, RAG addresses this by dynamically retrieving only the relevant data
- You can't build a product off of it, breaks apart when trying to do multi-user or secure apps.
- Custom GPTs can't scale to arbitrary amounts of private data. They don't do live retrieval, and you have limited control.
