from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

def get_answer(question):

    docs = vectorstore.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an Indian Legal Assistant.

Answer only from the provided legal documents.
if the info not present and its related to pdf info just give one line meaning of that 
If information is unavailable, reply:

"Information not found in available legal acts.
Maximum 250 words
Easy-to-understand language
Suitable for non-legal users"

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.text
