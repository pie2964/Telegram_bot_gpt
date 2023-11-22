import schedule
import time
import asyncio
import telegram
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

async def send_message(chat_id, text):
    token = "6988074211:AAE9qvTTMcl09hxwwQ5slUlijMDCZBqHcSM"
    bot = telegram.Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=text)

async def main():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "겨울에 대한 시를 써줘. json"}
        ],
        response_format={"type":"json_object"}
    )

    chat_id = "-1002072112022"
    text = str(completion.choices[0].message)
    await send_message(chat_id, text)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    while True:
        schedule.run_pending()
        time.sleep(1)
