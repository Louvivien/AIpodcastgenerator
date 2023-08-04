
import re, os
from elevenlabs import generate
import requests
from dotenv import load_dotenv
import random
from pydub import AudioSegment
import logging

# Load environment variables
load_dotenv()
elevenlabs_key = os.getenv('ELEVEN_API_KEY')
elevenlabs_url = os.getenv('ELEVENLABS_URL')


# list of custom voices cloned into elevenlabs
CUSTOM_VOICE = ['jessi']





def extract_dialogues(script, speaker1, speaker2):
    logging.info("Extracting dialogues...")
    # not using this function anymore, but keeping it here in case recurrent requests to 
    # elevenlabs api fails.
    speaker1_dialogue_pattern =  fr"{speaker1}: ([^\n]*?)\n"
    speaker2_dialogue_pattern =  fr"{speaker2}: ([^\n]*?)\n"
    
    # Use the re.findall() function to find all occurrences of the dialogue pattern
    speaker1_dialogues = re.findall(speaker1_dialogue_pattern, script)
    speaker2_dialogues = re.findall(speaker2_dialogue_pattern, script)
    
    return [speaker1_dialogues, speaker2_dialogues]


def get_all_voices():
    logging.info("Getting voices...")

    
    url = f'{elevenlabs_url}' + 'voices'
    headers = {
        'accept': 'application/json',
        'xi-api-key': elevenlabs_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Now you can work with the JSON response 'data'
        return data
    else:
        return (f"Failed to retrieve data. Status code: {response.status_code}")

def get_voice(voice_id):
    logging.info("Getting voice...")

   
    url = f'{elevenlabs_url}' + 'voices/' + f'{voice_id}'
    headers = {
        'accept': 'application/json',
        'xi-api-key': elevenlabs_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Now you can work with the JSON response 'data'
        return data
    else:
        return (f"Failed to retrieve data. Status code: {response.status_code}")


def filter_voice(gender, age, accent):
    '''
    gender: [male, female]
    age: [young, old, middle aged]
    accent: [american, british, australian, indian, african]
    '''
    logging.info("Filtering voice...")
    filtered_voices = []
    json_data = get_all_voices()

    if "voices" in json_data:
        for voice in json_data["voices"]:
            if "labels" in voice and "gender" in voice["labels"] and "age" in voice["labels"] and "accent" in voice["labels"]:
                if voice["labels"]["gender"] == gender and voice["labels"]["age"] == age and voice["labels"]["accent"] == accent:
                    filtered_voices.append(voice)
    if len(filtered_voices) == 0:
        raise Exception("No voice found, please try with a different voice settings.")
    
    voice = random.choice(filtered_voices)
    return random.choice(filtered_voices)


def concatenate_audio(audio_parts):
    logging.info("Concatenating voices...")
    # Concatenate all the audio parts into a single audio segment
    final_audio = AudioSegment.empty()
    final_audio = b"".join(audio_parts)

    return final_audio


def generate_audio(script, speaker1, speaker2, 
                   speaker1_age, speaker2_age,
                   speaker1_gender, speaker2_gender,
                   speaker1_accent, speaker2_accent,
                   speaker1_voice, speaker2_voice):
    try:
        logging.info("Generating audio...")
        transcript = script

        if speaker1_voice:
            sp1_voice = speaker1_voice
        else: 
            sp1_voice = speaker1.lower() if speaker1.lower() in CUSTOM_VOICE else filter_voice(speaker1_gender, speaker1_age, speaker1_accent)['name']

        if speaker2_voice:
            sp2_voice = speaker2_voice
        else:
            sp2_voice = speaker2.lower() if speaker2.lower() in CUSTOM_VOICE else filter_voice(speaker2_gender, speaker2_age, speaker2_accent)['name']

        # Split the transcript into parts for speaker1 and speaker2
        parts = re.split(fr'({speaker1.title()}:|{speaker2.title()}:)', transcript)
        logging.info(f"Splitting transcript...{parts}")

        audio_parts = []
        for i in range(1, len(parts), 2):
            speaker = parts[i].strip()
            text = parts[i+1].strip()
            
            # Generate audio for this part
            if speaker == f'{speaker1.title()}:':
                audio = generate(text=text, voice=sp1_voice, model="eleven_monolingual_v1")
            elif speaker == f'{speaker2.title()}:':
                audio = generate(text=text, voice=sp2_voice, model="eleven_monolingual_v1")
            print("Generated audio for: ", speaker)
            audio_parts.append(audio)

        # Combine the audio parts
        final_audio = concatenate_audio(audio_parts)  
        with open("podcast.mp3", "wb") as f:
            f.write(final_audio)
    except Exception as e:
        logging.exception(e)
        return False

    return True