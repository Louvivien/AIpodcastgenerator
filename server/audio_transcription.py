import openai

def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe("whisper-1", audio_file)
        return response["text"]
    except Exception as e:
        print(f"Error calling Whisper API: {str(e)}")
        return None

