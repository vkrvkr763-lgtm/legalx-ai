from langchain_community.document_loaders import PyPDFLoader

pdfs = [
    "../data/pocso.pdf",
    "../data/consumer.pdf",
    "../data/cybercrime.pdf",
    "../data/rti.pdf"
]

docs = []

for pdf in pdfs:
    loader = PyPDFLoader(pdf)
    docs.extend(loader.load())

print("Total Pages:", len(docs))