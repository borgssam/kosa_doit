from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.9,
    messages=[
        {"role": "system", "content": "너는 배트맨 이야기 속의 조커야. 그 이야기 속의 조커 캐릭터에 부합하게 답변해줘."},
        {"role": "user", "content": "배트맨과의 관계는 어떻게 되니?"},
    ])
print(response)
print("="*50)
print(response.choices[0].message.content)
print("="*50)