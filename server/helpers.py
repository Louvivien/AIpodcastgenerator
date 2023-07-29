from flask import render_template, jsonify
import datetime
import os
from elevenlabs import generate
from urllib.parse import urlparse

def valid_url(url):
    """valid_url
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def read_episode_text():
    try:
        with open("episode_text.txt", "r") as episode_file:
            return episode_file.read()
    except FileNotFoundError:
        print("El archivo 'episode_text.txt' no fue encontrado.")
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
    return None


def home():
    # Renderiza la plantilla "podcast.html" también para la ruta raíz
    return render_template('podcast.html', episode_text='')


def podcast():
    # Leer el texto del episodio desde el archivo
    episode_text = read_episode_text()

    # Renderizar la plantilla "podcast.html" y pasar el texto del episodio como parámetro
    return render_template('podcast.html', episode_text=episode_text)

