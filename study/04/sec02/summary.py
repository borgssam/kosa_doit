from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일에서 환경변수(API KEY 등) 로드
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def summarize_txt(file_path: str): # ① 텍스트 파일을 읽어 요약하는 함수
  # ② OpenAI 클라이언트 객체 생성
  client = OpenAI(api_key=api_key) 
  
  # ③ 지정된 경로의 텍스트 파일을 UTF-8 인코딩으로 읽어옵니다.
  with open(file_path, 'r', encoding='utf-8') as f:
    txt = f.read()
    
  # ④ 시스템 프롬프트 작성: AI에게 역할과 요약 형식을 지시합니다.
  system_prompt = f'''
  너는 다음 글을 요약하는 봇이다. 아래 글을 읽고, 저자의 문제 인식과 주장을 파악하고, 주요 내용을 한글로 요약하라. 
  작성해야 하는 포맷은 다음과 같다.
  # 제목
  ## 저자의 문제 인식 및 주장 (15문장 이내)
  ## 저자 소개  
  ================= 이하 텍스트 ===============

  { txt }
  '''

  print(system_prompt)
  print('=========================================')
  
  # ⑤ OpenAI API를 호출하여 요약 텍스트를 생성합니다.
  response = client.chat.completions.create(
    model="gpt-3.5-turbo", # 사용할 언어 모델 지정
    messages=[
      {"role": "system", "content": system_prompt}, # 시스템 프롬프트 전달
    ]
  )
  
  # API 응답에서 메시지 내용(요약 결과)만 추출하여 반환합니다.
  return response.choices[0].message.content

if __name__ == '__main__':
  # 요약할 원본 텍스트 파일의 경로
  file_path = './study/04/output/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축_with_preprocessing.txt'
  
  # 요약 함수 호출
  summary = summarize_txt(file_path)
  
  # 터미널에 요약 결과 출력
  print(summary)

  # ⑥ 요약된 결과를 새로운 텍스트 파일로 저장합니다.
  with open('./study/04/output/crop_model_summary.txt', 'w', encoding='utf-8') as f:
    f.write(summary)