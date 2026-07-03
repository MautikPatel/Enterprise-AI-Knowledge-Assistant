import ollama


def generate_answer(question, retrieved_results):
    """
    Generate an answer using retrieved document context.
    """

    documents = retrieved_results["documents"][0]

    context = "\n\n".join(documents)

    prompt = f"""
You are an Enterprise AI Knowledge Assistant.

Answer ONLY using the provided document context.

If the answer is not available in the documents, respond with:

"I could not find that information in the uploaded documents."

-----------------------------
DOCUMENT CONTEXT
-----------------------------

{context}

-----------------------------
QUESTION
-----------------------------

{question}

Provide a professional and concise answer.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]