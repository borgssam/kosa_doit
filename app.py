import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 로드
load_dotenv()

st.title("🤖 나만의 AI 챗봇")

# 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 세션 상태로 대화 기록 관리
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 처리
if prompt := st.chat_input("무엇이든 물어보세요!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # OpenAI API 호출
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        )
        answer = response.choices[0].message.content
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})