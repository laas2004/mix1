import chromadb
from chromadb.config import Settings

CHROMA_DIR = "../chroma_db"

client = chromadb.Client(
    Settings(persist_directory=CHROMA_DIR)
)

collection = client.get_collection("documents")

def query_documents(question):
    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    if not results["documents"]:
        return "I cannot answer this from the provided documents."

    response = ""
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        response += f"\n📄 {meta['file']} | Page {meta['page']} | {meta['method']}\n{doc}\n"

    return response


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type exit): ")
        if q.lower() == "exit":
            break
        print(query_documents(q))
