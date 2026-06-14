import streamlit as st
import json
import os
from backend.rag import get_answer

st.set_page_config(
    page_title="LegalX AI Knowledge Centre",
    layout="wide"
)

st.title("⚖️ LegalX AI Knowledge Centre")

topic = st.selectbox(
    "Select Legal Act",
    [
        "POCSO",
        "RTI",
        "Consumer Protection",
        "Cyber Crime"
    ]
)

# SUMMARY

st.subheader("Summary")

try:
    with open(
        f"generated/summaries/{topic.lower().replace(' ','_')}.txt",
        "r",
        encoding="utf-8"
    ) as f:
        summary = f.read()

    st.write(summary)

except:
    st.info("Summary not generated yet.")

st.subheader("Audio Debug")

audio_path = "generated/audio/pocso.mp3"

st.write("Audio file:", audio_path)
st.write("Exists:", os.path.exists(audio_path))

if os.path.exists(audio_path):
    st.subheader("🔊 Listen to Summary")
    
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")

# CHATBOT IN MIDDLE

st.markdown("---")

chat_container = st.container(border=True)

with chat_container:

    st.subheader("🤖 AI Legal Assistant")

    question = st.text_input(
        "Ask a legal question"
    )

    if st.button("Ask"):

        if question:

            with st.spinner("Thinking..."):

                answer = get_answer(question)

            st.success(answer)

st.markdown("---")

# KEY INFO

try:

    with open(
        f"generated/key_info/{topic.lower().replace(' ','_')}.json",
        "r",
        encoding="utf-8"
    ) as f:

        content = f.read()

    content = content.replace("```json", "")
    content = content.replace("```", "")

    data = json.loads(content)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Key Rights")

        for item in data["key_rights"]:
            st.write("•", item)

        st.subheader("Important Provisions")

        for item in data["important_provisions"]:
            st.write("•", item)

    with col2:

        st.subheader("Important Penalties")

        for item in data["important_penalties"]:
            st.write("•", item)

        st.subheader("Who Can Benefit")

        for item in data["who_can_benefit"]:
            st.write("•", item)

except:

    st.info("Key information not generated yet.")