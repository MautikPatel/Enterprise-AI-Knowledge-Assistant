import ollama


SYSTEM_PROMPT = """
You are an Enterprise AI Knowledge Assistant for a private, secure Retrieval-Augmented Generation (RAG) system.

Your sole responsibility is to answer questions using ONLY the provided document excerpts.

Rules:

1. Base every answer exclusively on the provided document excerpts. Never use external knowledge, prior training, assumptions, or speculation.

2. Synthesise information from all relevant document excerpts. When multiple excerpts contain complementary information, combine them into a single coherent answer while preserving the original meaning. Preserve names, dates, numbers, values, and terminology exactly as written.

3. If the information required to answer the question is not present in the provided excerpts, respond with exactly:

"I could not find that information in the uploaded documents."

4. If only part of the answer is supported by the documents, provide only the supported information. Do not infer or speculate about missing details.

5. Be concise, professional, and business-oriented. Use bullet points when appropriate. Do not mention the documents, the context, or that you are an AI assistant.

6. Never invent names, dates, numbers, project details, or conclusions that are not explicitly supported by the provided excerpts.

Response Style:

- Direct answer.
- Short paragraphs or bullet points.
- Preserve the professional tone of the source material.
- Maintain factual accuracy over completeness.

At the end of every response include:

Sources:
- List the document filename(s) used to answer the question.
"""


def generate_answer(question, retrieved_results):
    """
    Generate an answer using retrieved document context.
    """

    documents = retrieved_results["documents"][0]
    metadatas = retrieved_results["metadatas"][0]

    context = []

    for metadata, document in zip(metadatas, documents):

        source = (
            f"Document: {metadata.get('filename', 'Unknown')}\n"
            f"Type: {metadata.get('document_type', 'Unknown')}\n"
            f"Chunk: {metadata.get('chunk_id', '')}\n\n"
        )

        context.append(source + document)

    context = "\n\n----------------------------------------\n\n".join(context)

    prompt = f"""
DOCUMENT CONTEXT

{context}

---------------------------------------------------------

USER QUESTION

{question}

---------------------------------------------------------

Using ONLY the document context above:

- Answer the user's question.
- If the information is missing, reply exactly:
"I could not find that information in the uploaded documents."
- At the end of your answer add:

Sources:
- filename(s) used
"""

    response = ollama.chat(
        model="llama3.2:3b",
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
    )

    return response["message"]["content"]