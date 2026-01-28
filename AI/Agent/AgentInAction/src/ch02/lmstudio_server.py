from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="test-api-key")
completion = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "system", "content": "항상 라임을 맞춰서 응답하세요."},
        {"role": "user", "content": "네 소개를 해"},
    ],
    temperature=0.7,
)

print(completion.choices[0].message)
