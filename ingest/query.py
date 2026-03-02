# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
# from langchain_ollama import OllamaLLM

# CHROMA_DIR = "../chroma_db"

# embedding = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )

# vectordb = Chroma(
#     persist_directory=CHROMA_DIR,
#     embedding_function=embedding
# )

# llm = OllamaLLM(
#     model="llama3",
#     temperature=0
# )

# def ask(query):
#     docs = vectordb.similarity_search(query, k=3)

#     if not docs:
#         print("❌ I cannot answer this based on the provided documents.")
#         return

#     context = "\n\n".join(d.page_content for d in docs)
#     sources = set(d.metadata.get("source", "unknown") for d in docs)

#     prompt = f"""
# Answer ONLY from the context below.
# If the answer is not present, say: "I cannot answer this based on the provided documents."

# Context:
# {context}

# Question:
# {query}
# """

#     answer = llm.invoke(prompt)

#     print("\n✅ Answer:\n", answer)
#     print("\n📚 Sources:")
#     for s in sources:
#         print("-", s)


# while True:
#     q = input("\nAsk a question (or 'exit'): ")
#     if q.lower() == "exit":
#         break
#     ask(q)

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

CHROMA_DIR = "../chroma_db"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory=CHROMA_DIR,
    embedding_function=embedding
)

llm = OllamaLLM(
    model="llama3.2:latest",
    temperature=0
)

print("\nRAG system ready. Type 'exit' to quit.\n")

while True:
    query = input("Ask a question (or 'exit'): ").strip()
    if query.lower() == "exit":
        break

    # Retrieve documents
    docs = vectordb.similarity_search_with_score(query, k=4)

    if not docs:
        print("\n❌ I cannot answer this based on the provided documents.\n")
        continue

    # Filter weak matches (IMPORTANT CHANGE)
    filtered = [(d, s) for d, s in docs if s < 1.2]

    if not filtered:
        print("\n❌ I cannot answer this based on the provided documents.\n")
        continue

    context = ""
    sources = set()

    for doc, score in filtered:
        context += doc.page_content + "\n\n"
        sources.add(doc.metadata.get("source", "Unknown document"))

    prompt = f"""
You must answer ONLY using the context below.
If the answer is not explicitly present, say:
"I cannot answer this based on the provided documents."

Context:
{context}

Question:
{query}

Answer with clear bullet points when possible.
"""

    answer = llm.invoke(prompt).strip()

    if "cannot answer" in answer.lower():
        print("\n❌ I cannot answer this based on the provided documents.\n")
    else:
        print("\n✅ Answer:\n")
        print(answer)
        print("\n📚 Sources:")
        for src in sources:
            print(f"- {src}")
        print()
