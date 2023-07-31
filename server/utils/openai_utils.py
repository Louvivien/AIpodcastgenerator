import openai
import logging


def askGPT(prompt):
    logging.info("Generating transcript...")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system",
                "content": "You are a podcast producer"},
            {"role": "user", "content": "I want you to create a highly entertaining podcast based on the this topic: X.AI Corp"},
            {"role": "assistant", "content": """Alice: Hello listeners, welcome back to our podcast, AI Today. I'm your host Alice, and with me is my co-host, Bob. Today, we're going to talk about a fascinating new AI startup that's been making waves in the tech world. It's called X.AI Corp, also known as xAI. Bob, what can you tell us about this company?

                Bob: Hi Alice, and hello to all our listeners. xAI is indeed an interesting company to discuss. It's an artificial intelligence startup founded by none other than Elon Musk. The company was officially announced on July 12, 2023, and it's composed of former employees from some of the biggest names in tech and AI research, including OpenAI, Google DeepMind, Google Research, Microsoft Research, Tesla, Twitter, and the University of Toronto.

                Alice: That's quite a lineup of talent. But what's the mission of xAI, Bob? What are they aiming to achieve in the AI space?

                Bob: Great question, Alice. One of the primary goals of xAI is to create an AI that is capable of advanced mathematical reasoning, something not found in current models. Musk has also mentioned the "Waluigi-Problem" in a Twitter Spaces statement. He described it as the challenge of programming morality into an AI without also inadvertently creating the opposite or inverse of that morality.

                Alice: That sounds like a complex problem to solve. It's interesting to see how Musk is addressing the ethical aspects of AI development.

                Bob: Absolutely, Alice. It's clear that xAI is not just about creating advanced AI models, but also about ensuring these models align with our moral and ethical standards. It's going to be fascinating to see how this company progresses in the future.

                Alice: Indeed, Bob. We'll certainly be keeping a close eye on xAI and its developments. That's all for today, folks. Join us next time as we continue to explore the exciting world of AI.

                Bob: Thanks for tuning in, everyone. Stay curious, and keep exploring!""",
             },
            {"role": "user", "content": prompt},
        ],
        n=1,
        temperature=0.5,
    )
    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']



