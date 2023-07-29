from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
#def home():
#    return 'Welcome! This is the homepage of the Elevenlabs Hackathon podcast.'
def home():
    # Renderiza la plantilla "podcast.html" también para la ruta raíz
    return render_template('podcast.html', episode_text='')
# Ruta para la página del podcast
@app.route('/podcast')
def podcast():
    # Simulación del texto del episodio
    episode_text = """
    Welcome to the Elevenlabs Hackathon podcast!

    Host 1: Hey there! Welcome back to another exciting episode of our podcast. I'm your host, ChatGPT-1.
    
    Host 2: And I'm your co-host, ChatGPT-2. We have a fascinating topic to discuss today.
    
    Host 1: Absolutely! Today, we are going to explore how we use Elevenlabs as TTS (Text-to-Speech) to generate audio from the text.
    
    Host 2: It's a fantastic technology that allows us to convert written text into spoken words seamlessly.
    
    Host 1: Indeed! We'll also talk about our experiences at the Elevenlabs Hackathon and some of the innovative projects we saw there.
    
    Host 2: So stay tuned, grab a cup of coffee, and let's dive into the world of TTS and the wonderful Hackathon experience.
    
    Host 1: Let's roll the intro music and get started!
    """

    # Renderiza la plantilla "podcast.html" y pasa el texto del episodio como parámetro
    return render_template('podcast.html', episode_text=episode_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

