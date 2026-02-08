import streamlit as st
from app.utils import extract_text_from_pdf
from app.analyst import analyze_report

st.set_page_config(page_title="EarningsCall Analyst", layout="wide")

# --- 헤더 ---
st.title("AI 주식 종목 분석기")
st.caption("읽기 귀찮은 증권사 리포트(PDF)나 뉴스 기사를 넣어주세요.")
st.divider()

# --- 입력 섹션 ---
tab1, tab2 = st.tabs(["PDF 리포트 업로드", "뉴스 텍스트 입력"])

input_text = ""

with tab1:
    uploade_file = st.file_uploader("증권사 리포트 PDF", type=["pdf"])
    if uploade_file:
        with st.spinner("PDF 읽는 중..."):
            input_text = extract_text_from_pdf(uploade_file)
            if input_text:
                st.success(f"PDF 로드 완료!")

with tab2:
    text_area = st.text_area("뉴스 기사 본문을 붙여넣으세요.", height=300)
    if text_area:
        input_text = text_area

# --- 분석 버튼 ---
analyze_btn= st.button("투자 분석 시작", type="primary", width="stretch")

# --- 결과 섹션 ---
if analyze_btn:
    if not input_text:
        st.warning("분석할 데이터를 입력해주세요!")
    else:
        with st.spinner("월스트리트 애널리스트가 차트를 분석 중입니다..."):
            result  = analyze_report(input_text)

            if "error" in result:
                st.error(result["error"])
            else:
                # 데이터 파싱
                comp_name = result.get("company_name", "Unknown")
                score = result.get("sentiment_score", 0)
                verdict  = result.get("verdict", "Hold")
                summary = result.get("summary", "")
                metrics = result.get("key_metrics", {})
                risks = result.get("risks", [])
                oppty = result.get("opportunity", "")

                st.divider()
                st.header(f"{comp_name} 분석 리포트")

                # 투자 의견 (게이지)
                col1, col2, col3  = st.columns([1, 1, 1])

                # 점수에 따른 색상
                if score >= 5:
                    score_color = "red" # 국장은 빨강이 상승
                elif score <= -5:
                    score_color = "blue" # 파랑은 하락
                else:
                    score_color = "gray"

                col1.metric("투자 의견", verdict)
                col1.caption(f"감성 점수: {score} / 10")

                # 핵심 요약
                with col2:
                    st.markdown("### 핵심 요약")
                    st.info(summary)

                # 호재 및 기회
                with col3:
                    st.markdown("### 상승 모멘텀")
                    st.success(oppty)

                st.divider()

                # 재무 지표 & 리스크
                c1, c2 = st.columns(2)

                with c1:
                    st.subheader("주요 재무 지표")
                    for k, v in metrics.items():
                        st.markdown(f"**{k}:** {v}")
                
                with c2:
                    st.subheader("투자 리스크")
                    for r in risks:
                        st.error(f"- {r}")
