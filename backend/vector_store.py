from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

pdfs = [
    "../data/pocso.pdf",
    "../data/consumer.pdf",
    "../data/cybercrime.pdf",
    "../data/rti.pdf"
]

documents = []

for pdf in pdfs:
    loader = PyPDFLoader(pdf)
    documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="../chroma_db"
)

print("Vector DB Created Successfully")