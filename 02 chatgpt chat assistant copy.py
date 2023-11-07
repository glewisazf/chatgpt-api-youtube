import os

import openai
import json

openai.api_key = "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"

message_history = []


def chat(inp, role="user"):
    message_history.append({"role": "user", "content": inp})
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role": "assistant", "content": reply_content})
    return reply_content


for i in range(2):
    user_input = input(">: ")
    print("User input was", user_input)
    print()
    chat(user_input)
    print()
