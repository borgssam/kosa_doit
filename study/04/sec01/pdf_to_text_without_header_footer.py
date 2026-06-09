import pymupdf
import os

#①
pdf_file_path = "./study/04/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf"
doc = pymupdf.open(pdf_file_path)

full_text = ''

#②