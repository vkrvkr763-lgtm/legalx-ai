from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="../chroma_db",
    embedding_function=embeddings
)

query = "What is the punishment under POCSO?"

results = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(results, 1):
    print(f"\n===== RESULT {i} =====\n")
    print(doc.page_content[:1000])