from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "겨울에 대한 시를 써줘. json"}
  ],
  response_format={"type":"json_object"}
)

print(completion.choices[0].message)
