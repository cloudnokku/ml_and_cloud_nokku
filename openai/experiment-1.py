import os
import openai
# openai.organization = "org-flLagEJ4kqb0hizKRARglw4E"
openai.api_key = "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"
# print(openai.Model.list())

input_question="what is large language models?"

# completion = openai.Completion.create(
#     prompt=input_question,
#     model="text-davinci-003"
# )
# print(f"completion by text-davinci-003  : {completion}")


messages = [ {"role": "system", "content": 
            "You are a intelligent assistant."} ]
messages.append(
            {"role": "user", "content": input_question},
        )
chat_completion = openai.ChatCompletion.create(
    messages=messages,
    model="gpt-3.5-turbo"
)
print(f"chat_completion by gpt-3.5-turbo  : {chat_completion}")

# embedding = openai.Embedding.create(
#   input=input_question,
#   model="text-embedding-ada-002"
# )
# print(f"embedding by text-embedding-ada-002  : {embedding}")