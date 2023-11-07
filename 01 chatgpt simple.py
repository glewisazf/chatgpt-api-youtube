import os
import openai

openai.api_key = "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"
MODEL = "gpt-3.5-turbo"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
    temperature=0,
)

print(response['choices'][0]['message']['content'])