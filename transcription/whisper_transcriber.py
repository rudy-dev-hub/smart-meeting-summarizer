import whisper

model = whisper.load_model("tiny")

def transcribe_audio(file_path):
    result = model.transcribe(file_path)
    return result["text"]
