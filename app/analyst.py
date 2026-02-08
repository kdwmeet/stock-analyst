from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from app.config import MODEL_NAME, SYSTEM_PROMPT

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_report(text_data):
    """텍스트 데이터를 분석하여 투자 리포트 JSON 반환"""

    if not text_data or len(text_data) < 100:
        return {"error": "내용이 너무 짧습니다. 분석할 데이터가 부족합니다."}
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"다음 리포트를 분석해줘:\n\n{text_data}"}
            ],
            reasoning_effort="low",
            response_format={"type": "json_object"}
        )

        result_json = json.loads(response.choices[0].message.content)
        return result_json
    
    except Exception as e:
        return {"error": f"분석 중 오류 발생: {str(e)}"}