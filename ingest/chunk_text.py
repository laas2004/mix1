from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_pages(pages, file_name):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " "]
    )

    documents = []

    for page in pages:
        chunks = splitter.split_text(page["text"])

        for chunk in chunks:
            documents.append({
                "text": chunk,
                "metadata": {
                    "file": file_name,
                    "page": page["page"],
                    "method": page["method"]
                }
            })

    return documents
