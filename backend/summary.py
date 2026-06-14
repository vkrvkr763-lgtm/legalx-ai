from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
import os

load_dotenv()

# CHANGE ONLY THIS
pdf_name = "rti"

loader = PyPDFLoader(f"data/{pdf_name}.pdf")

docs = loader.load()

text = "\n".join(
    [doc.page_content for doc in docs]
)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

prompt = f"""
Summarize this legal act.

Requirements:
- Maximum 300 words
- Simple language
- Easy for ordinary citizens
- Explain purpose
- Explain rights
- Explain protections
- Explain penalties

Content:
{text[:15000]}
"""

response = llm.invoke(prompt)

os.makedirs(
    "generated/summaries",
    exist_ok=True
)

with open(
    f"generated/summaries/{pdf_name}.txt",
    "w",
    encoding="utf-8"
) as f:
    f.write(response.content)

print(f"{pdf_name} summary generated!")
