import os
from openai import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    client = OpenAI(api_key=openai_api_key)
    user_message = "안녕하세요! 오늘 날씨 어때요?"
    response = ask_chatgpt(client, user_message)
    print("ChatGPT 응답:", response)


def ask_chatgpt(client, user_message):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "당신은 유능한 어시스턴트입니다."},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    main()
