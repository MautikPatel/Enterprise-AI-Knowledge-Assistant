import ollama


SYSTEM_PROMPT = """
You are an Enterprise AI Knowledge Assistant for a private, secure Retrieval-Augmented Generation (RAG) system.

Your sole task is to answer user questions based ONLY on the provided document excerpts.

Rules:

1. Base your answer only on the provided document context.

2. Never use external knowledge.

3. Never guess or invent information.

4. If the answer is not contained in the provided context, reply exactly with:

"I could not find that information in the uploaded documents."

5. Combine information from multiple document excerpts whenever appropriate.

6. Keep responses concise, professional and business-oriented.

7. Use bullet points when listing items.

8. Do NOT mention the context, retrieved chunks, documents, or that you are an AI assistant.

9. Do NOT include source filenames in your answer.
Those are displayed separately by the application.
"""


def generate_answer(question, retrieved_results):
    """
    Generate an answer using the retrieved document context.
    """

    MAX_CONTEXT_CHUNKS = 4

    documents = retrieved_results["documents"][0][:MAX_CONTEXT_CHUNKS]

    context = "\n\n".join(documents)

    prompt = f"""
==================================================
DOCUMENT CONTEXT
==================================================

{context}

==================================================
QUESTION
==================================================

{question}

==================================================
ANSWER
==================================================
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        options={
            "temperature": 0,
            "num_predict": 150,
            "num_ctx": 4096,
        },
    )

    return response["message"]["content"]