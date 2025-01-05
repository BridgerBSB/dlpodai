import whisper
model = whisper.load_model("base")
result = model.transcribe("DL_Podcast_EP_15_audio.mp3")
file = open("dlpod.txt", "w")
file.write(result["text"])