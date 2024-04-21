from openai import OpenAI
import time
from .generator import text_to_keywords

def audio_to_text(path) -> str:
    client = OpenAI()

    audio_file= open(path, "rb")

    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    return transcription.text

# start = time.time()
# # text = audio_to_text("presentation.wav")
# text = audio_to_text("Brian Cox explains quantum mechanics in 60 seconds - BBC News.wav")
# print(text)
# print(text_to_keywords(text))
# print(time.time() - start)