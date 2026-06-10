import pymupdf  # PDF 파일을 다루기 위한 PyMuPDF 라이브러리 임포트
import os       # 파일 경로 및 이름 처리를 위한 os 모듈 임포트

# ① PDF 파일 열기 및 초기 설정
pdf_file_path = "./study/04/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf"
doc = pymupdf.open(pdf_file_path)  # 지정된 경로의 PDF 파일을 엽니다.

# 머리글(Header)과 바닥글(Footer)로 간주할 높이 영역 설정
header_height = 80
footer_height = 80

# 전체 텍스트를 누적해서 저장할 문자열 변수 초기화
full_text = ''

# ② 페이지별 텍스트 추출 (머리글, 바닥글 제외)
for page in doc: # 문서의 모든 페이지를 순회하며 반복
  rect = page.rect # 현재 페이지의 크기(너비, 높이 등) 정보를 가져옵니다.
  
  # 특정 영역(clip)만 지정하여 텍스트를 추출합니다.
  # 최상단부터 머리글 영역까지 텍스트 추출 (현재 코드에서는 사용하지 않지만 확인용으로 추출)
  header = page.get_text(clip=(0, 0, rect.width , header_height))
  # 최하단 바닥글 영역의 텍스트 추출
  footer = page.get_text(clip=(0, rect.height - footer_height, rect.width , rect.height))
  
  # 머리글과 바닥글을 제외한 실제 본문 영역의 텍스트만 추출
  text = page.get_text(clip=(0, header_height, rect.width , rect.height - footer_height))
  
  # 추출된 본문 텍스트를 전체 텍스트에 추가하고 페이지 구분을 위한 구분선을 덧붙임
  full_text += text + '\n------------------------------------\n'

# ③ 파일명만 추출하여 저장할 경로 생성
pdf_file_name = os.path.basename(pdf_file_path) # 경로에서 파일명과 확장자만 추출
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자(.pdf)를 제거하고 순수 파일명만 추출

# 추출한 텍스트를 저장할 txt 파일 경로 지정
txt_file_path = f"./study/04/output/{pdf_file_name}_with_preprocessing.txt"

# 지정한 경로에 추출한 텍스트를 UTF-8 인코딩으로 파일에 쓰기(저장)
with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)