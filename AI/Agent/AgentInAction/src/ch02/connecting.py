import os
import google.generativeai as genai
from dotenv import load_dotenv


def main():
    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    genai.configure(api_key=gemini_api_key)
    user_message = "안녕하세요! 오늘 서울 날씨 어때요?"
    response = ask_chatgpt(user_message)
    print("Gemini 응답:", response)


def ask_chatgpt(user_message):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(
        user_message, generation_config=genai.types.GenerationConfig(temperature=0.7)
    )
    return response.text


if __name__ == "__main__":
    main()
