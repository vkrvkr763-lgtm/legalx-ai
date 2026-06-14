import os
from gtts import gTTS

# CHANGE ONLY THIS
pdf_name = "rti"

with open(
    f"generated/summaries/{pdf_name}.txt",
    "r",
    encoding="utf-8"
) as f:
    summary = f.read()

os.makedirs(
    "generated/audio",
    exist_ok=True
)

tts = gTTS(
    text=summary,
    lang="en"
)

tts.save(
    f"generated/audio/{pdf_name}.mp3"
)

print(
    f"{pdf_name}.mp3 generated successfully!"
)