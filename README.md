# AI podcast generator

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<p align="center">
  <h3 align="center">AI podcast generator</h3>

  <p align="center">
    a cutting-edge tool designed to revolutionize the way you create and share podcasts! Imagine converting your favorite news articles, blog posts, or any written content into captivating audio episodes effortlessly
    <br />
    <a href="https://github.com/Louvivien/AIpodcastgenerator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://lablab.ai/event/ai-agents-hackathon/let-them-live">View Project</a>
    ·
    <a href="https://github.com/Louvivien/AIpodcastgenerator/issues">Report Bug</a>
    ·
    <a href="https://github.com/Louvivien/AIpodcastgenerator/issues">Request Feature</a>
        ·
    <a href="https://discord.gg/e3sZ2wxWR2">Join our Discord</a>
  </p>
</p>

![Python Version][python-image]
![License][license-image]

## Setup 

1. Install Python 3.9 or later.

2. Clone this repository:

    ```bash
    git clone https://github.com/Louvivien/AIpodcastgenerator.git 
    cd AIpodcastgenerator
    ```
    
    
3. Go to the server folder
    ```bash

cd server
    ```


 4. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a `.env` file in the root directory and add your Instagram username and password:

    ```bash

        MONGO_URI=
        MONGO_PASSWORD=
        JWT_SECRET=
        ELEVEN_API_KEY=
        PINECONE_API_KEY=
        PINECONE_ENV=
        SERPAPI_API_KEY=
        OPENAI_API_KEY=
        CACHE_REDIS_URL=
        HUGGING_FACE_API_KEY=
    ```

6. Run the script:

    ```bash
    python main.py
    ```


Open another terminal windows
    
7. 
    ```bash

cd client
    ```


8. install packages
    ```bash

   npm i
    ```


9. start the client
    ```bash

   npm start

    ```





## Usage

Make sure the account sending messaged as a bio with a little story

This script logs into Instagram using the provided username and password, finds a user by their username, and sends them a direct message. It uses AutoGPT and LangChain to automate the conversation with the user.

## Troubleshooting

If the script is not working as expected, check the following:

- Make sure your Instagram username and password are correct and the account is not locked or restricted.
- Check the console for any error messages.

## Ongoing work

The integration of AutoGPT, LangChain, and Instagram is complete. It can engage in a conversation, follow user based on a topic and comment.
We will add some other methods in instagram and add other social media : can identify the content of an image and comment from what it as identified in the picture
For now the client is not connected to the server

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.

[python-image]: https://img.shields.io/badge/python-v3.6+-blue.svg
[license-image]: https://img.shields.io/badge/license-MIT-blue.svg

[contributors-shield]: https://img.shields.io/github/contributors/Louvivien/AIpodcastgenerator.svg?style=for-the-badge
[contributors-url]: https://github.com/Louvivien/AIpodcastgenerator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Louvivien/AIpodcastgenerator.svg?style=for-the-badge
[forks-url]: https://github.com/Louvivien/AIpodcastgenerator/network/members
[stars-shield]: https://img.shields.io/github/stars/Louvivien/AIpodcastgenerator.svg?style=for-the-badge
[stars-url]: https://github.com/Louvivien/AIpodcastgenerator/stargazers
[issues-shield]: https://img.shields.io/github/issues/Louvivien/AIpodcastgenerator.svg?style=for-the-badge
[issues-url]: https://github.com/Louvivien/AIpodcastgenerator/issues
[license-shield]: https://img.shields.io/github/license/Louvivien/AIpodcastgenerator.svg?style=for-the-badge
[license-url]: https://github.com/Louvivien/AIpodcastgenerator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555








# AI podcast generator
tool to generate a podcast with AI

## Setup 

