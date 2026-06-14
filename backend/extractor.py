from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

# CHANGE ONLY THIS
pdf_name = "rti"

with open(
    f"generated/summaries/{pdf_name}.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

prompt = f"""
Return ONLY valid JSON.

No markdown.
No explanation.
No code fences.

Format:

{{
  "key_rights": [],
  "important_provisions": [],
  "important_penalties": [],
  "who_can_benefit": []
}}

Content:
{text}
"""

response = llm.invoke(prompt)

os.makedirs(
    "generated/key_info",
    exist_ok=True
)

with open(
    f"generated/key_info/{pdf_name}.json",
    "w",
    encoding="utf-8"
) as f:
    f.write(response.content)

print(f"{pdf_name} key info generated!")