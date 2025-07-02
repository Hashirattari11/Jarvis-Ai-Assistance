from openai import OpenAI

client = OpenAI(
    api_key="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",

)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
