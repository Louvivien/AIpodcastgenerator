from elevenlabs import generate
import datetime
import os
from flask import jsonify

def generate_audio(selected_text):
    # Voice using Eleven API 
    voice= "Bella" 

    # Get current timestamp 
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") 

    # File name with timestamp 
    nombre_archivo = f"audio{timestamp}.mp3" 

    try: 
        # Generate audio using Eleven API 
        audio = generate(text=selected_text, voice=voice, api_key=os.getenv('ELEVEN_API_KEY')) 

        # Save the audio to a file 
        with open(nombre_archivo, "wb") as file: 
            file.write(audio) 

        with open(nombre_archivo, "rb") as file: 
            audio_data = file.read() 

        # Ensure to delete the audio file after sending it to the client 
        #os.remove("audio.mp3") 

        # Return the audio as a response 
        return audio_data, 200, {'Content-Type': 'audio/mpeg'} 

    except Exception as e: 
        print(str(e))
        return jsonify(message='Error retrieving the audio from ElevenLabs'), 500

