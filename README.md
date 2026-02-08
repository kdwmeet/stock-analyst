# Earnings Call Analyst (주식 종목 리포트 분석기)

## 1. 프로젝트 개요

Earnings Call Analyst는 개인 투자자가 해석하기 어려운 증권사 리포트(PDF)나 긴 호흡의 경제 뉴스 텍스트를 분석하여, 투자 매력도를 정량적으로 평가하고 핵심 정보를 요약해 주는 FinTech 솔루션입니다.

방대한 금융 텍스트 데이터에서 유의미한 정보를 추출하기 위해 OpenAI의 **gpt-5-mini** 모델을 활용합니다. 금융 도메인 지식을 갖춘 AI 애널리스트가 기업의 재무 성과, 잠재적 리스크, 성장 모멘텀을 분석하여 매수/매도/중립의 투자 의견을 제시합니다.

### 주요 기능
* **Financial Sentiment Analysis:** 텍스트 전반의 뉘앙스를 분석하여 투자 심리 점수(-10 ~ +10)를 산출.
* **Key Metrics Extraction:** 매출액, 영업이익, 순이익 등 핵심 재무 데이터를 텍스트에서 자동 추출.
* **Risk & Opportunity Detection:** 기업이 직면한 대외적 리스크 요인과 성장 기회 요인을 식별.
* **Investment Verdict:** 분석된 데이터를 종합하여 Buy(매수), Hold(중립), Sell(매도) 중 하나의 투자 의견 제시.

## 2. 시스템 아키텍처

본 시스템은 비정형 금융 문서(PDF, Text)를 입력받아 구조화된 투자 리포트로 변환하는 파이프라인으로 구성됩니다.

1.  **Data Ingestion:** 사용자가 증권사 리포트(PDF)를 업로드하거나 뉴스 기사 텍스트를 입력.
2.  **Preprocessing:** `pypdf` 라이브러리를 사용하여 PDF 내 텍스트를 추출하고 불필요한 서식을 제거.
3.  **Prompt Engineering:** '시니어 주식 애널리스트' 페르소나를 적용하여 객관적이고 수치 중심적인 분석을 수행하도록 지시.
4.  **AI Inference:** **gpt-5-mini** 모델이 금융 문맥(Financial Context)을 이해하고 JSON 포맷으로 결과 생성.
5.  **Visualization:** Streamlit UI를 통해 감성 점수, 핵심 지표, 리스크 요인을 대시보드 형태로 시각화.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI **gpt-5-mini**
* **Web Framework:** Streamlit
* **PDF Processing:** pypdf
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

데이터 처리 유틸리티, 분석 로직, 환경 설정을 분리하여 유지보수성을 높인 모듈형 구조입니다.

```text
stock-analyst/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 및 분석 대시보드 UI
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # 애널리스트 페르소나 및 분석 프롬프트 정의
    ├── utils.py          # PDF 텍스트 추출 로직 (pypdf 기반)
    └── analyst.py        # OpenAI API 통신 및 JSON 데이터 파싱 로직
```

## 5. 설치 및 실행 가이드
### 5.1. 사전 준비
Python 환경이 설치되어 있어야 합니다. 터미널에서 저장소를 복제하고 프로젝트 디렉토리로 이동하십시오.

```Bash
git clone [레포지토리 주소]
cd stock-analyst
```
### 5.2. 의존성 설치
PDF 처리 및 웹 프레임워크 구동을 위한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고, 유효한 OpenAI API 키를 입력하십시오.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 실행
Streamlit 애플리케이션을 실행합니다.

```Bash
streamlit run main.py
```
## 6. 출력 데이터 사양 (JSON Schema)
AI 모델은 분석 결과를 다음과 같은 JSON 구조로 반환합니다. 이를 통해 증권 앱의 뉴스 요약 서비스나 알림 봇으로 확장할 수 있습니다.

```JSON
{
  "company_name": "Samsung Electronics",
  "sentiment_score": 8,
  "verdict": "매수 (Buy)",
  "summary": "메모리 반도체 가격 반등과 HBM 수요 증가로 인한 어닝 서프라이즈 기록. 하반기 실적 개선세가 뚜렷할 것으로 전망됨.",
  "key_metrics": {
    "Revenue": "71조 원 (YoY +11%)",
    "Operating Profit": "6.6조 원 (YoY +931%)"
  },
  "risks": [
    "글로벌 경기 침체로 인한 스마트폰 수요 둔화",
    "파운드리 부문의 적자 지속"
  ],
  "opportunity": "AI 시장 확대로 인한 고대역폭메모리(HBM) 수주 증가"
}
```

## 7. 실행 화면
<img width="1266" height="796" alt="스크린샷 2026-02-09 064056" src="https://github.com/user-attachments/assets/9f451ca6-2050-44da-990f-3d15b84f2e7c" />

