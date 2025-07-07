# Docs That Talk Back

An exploration into using Retrieval Augmented Generation to talk to your documentation

## Table of Contents

1. Introduction of Problem
2. Limitations of LLMs
3. What is RAG?
4. How does RAG work?
5. Let's build a RAG
6. Technical Highlights
7. Live Demo
8. Recap Power of RAGs
9. Applications of RAG
10. Conclusion and Q&A

## Introduction of Problem

Let's clarify the problem we're trying to solve:

How can we use natural language to extract information about our documentation?

## Limitations of LLMs

- LLMs are designed to generate text
- Without grounding, they will hallucinate
-

How can we talk to our language models about our docs?

## What is Retrieval Augmented Generation (RAG)?

Retrieval Augmented Generation is a technique used to enhance the accuracy of generative AI models by supplying context from specific data sources. [\*](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)

In other words, it can connect LLMs with data sources to provide grounding.

## How does RAG work?

##

## Technical Highlights

This all sounds great, but how do we do this?

1. Chunk data
2. Use embedding model to generate embeddings for each chunk -> maybe talk about what embeddings are
3. Prompt engineering + Guardrails
4. How models can affect results (GPT3.5 vs 4.1)
5. Preventing re-ingestion? is this important?

I can use code snippets from the app here

## Live Demo

Show off the rag demo and how it can be used to talk to documentation.

## Applying RAG to the Productivity space

AI Assistant for...

- Note taking, "Summarize my notes on XYZ",
- Calendar, "Whats my availability for next week", "Whens my next 1:1?"
- Task lists, "What are my priorities for today?", "Which tasks are waiting on others?"

## Q&A

Show QR code that links to github repository
Thank everyone for listening
Open floor for questions
When no more questions, thank everyone again.

Retrieving data using natural language

## Why not just copy and paste my document into ChatGPT and give it the same prompt?

- This does a good job at EMULATING the process of a RAG, and works perfectly fine for small form content.
- You're dumping a haystack and asking it to search for the needles
- Rag adds semantic filtering so GPT doesn't have to read everything
- This breaks down when using larger documents. You can't fit the whole thing into chat, RAG addresses this by dynamically retrieving only the relevant data
- You can't build a product off of it, breaks apart when trying to do multi-user or secure apps.

- Custom GPTs can't scale to arbitrary amounts of private data. They don't do live retrieval, and you have limited control. (WHY?)
