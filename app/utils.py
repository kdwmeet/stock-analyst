from pypdf import PdfReader
import streamlit as st

def extract_text_from_pdf(uploaded_file):
    """업로드된 PDF 파일에서 텍스트 추출"""
    try:
        if uploaded_file is None:
            return None
        
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        # 너무 긴 리포트는 앞쪽 5페이지만 읽어도 충분 (비용 절감)
        max_pages = min(len(pdf_reader.pages), 15)

        for i in range(max_pages):
            extracted = pdf_reader.pages[i].extract_text()
            if extracted:
                text += extracted + "\n"
        
        if not text.strip():
            return "텍스트를 추출할 수 없는 PDF입니다."
        
        return text
    except Exception as e:
        st.error(f"PDF 처리 오류: {e}")
        return None