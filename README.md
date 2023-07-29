# AI podcast generator
tool to generate a podcast with AI

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



