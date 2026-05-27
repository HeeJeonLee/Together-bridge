# requirements: crewai, requests, schedule
import requests, json, schedule, time
from crewai import Crew, Agent

# 서비스별 템플릿 로드
with open('service_templates.json', 'r', encoding='utf-8') as f:
    service_templates = json.load(f)["services"]

# 1. config.json 로드
with open('config.json', 'r') as f:
    config = json.load(f)

# 2. 콘텐츠 생성 에이전트
content_agent = Agent(
    name="ContentAgent",
    llm=config['content_engine']['provider'],
    tools=[config['content_engine']['provider'] + "API"]
)

# 3. 평가 에이전트 (신규 AI/툴 자동 탐색)
eval_agent = Agent(
    name="EvalAgent",
    llm="Claude",
    tools=["ProductHuntAPI", "topai.toolsAPI"],
    role="평가/비교/교체"
)

# 4. 설계 에이전트 (워크플로우 재설계)
design_agent = Agent(
    name="DesignAgent",
    llm="Claude",
    tools=["n8nAPI", "ZapierAPI"],
    role="업무 재설계/최적화"
)

# 5. 멀티에이전트 허브
crew = Crew([content_agent, eval_agent, design_agent])


# 6. 서비스별 자동화 워크플로우 예시
def run_service_workflow(service_name, data):
    # 서비스 템플릿 찾기
    template = next((s for s in service_templates if s["name"] == service_name), None)
    if not template:
        print(f"[ERROR] 서비스 템플릿을 찾을 수 없음: {service_name}")
        return
    # 1. 외부 API 연동 (모의)
    print(f"[API] {template['external_api']} 호출 (데이터: {data})")
    # 2. AI 콘텐츠 생성 (예: 안내 메시지)
    prompt = f"{service_name} 안내 메시지 생성: {data}"
    api_url = config['content_engine']['api_url']
    api_key = config['content_engine']['api_key']
    res = requests.post(api_url, json={"prompt": prompt, "max_tokens": 300},
                        headers={"Authorization": f"Bearer {api_key}"})
    print(f"[AI] 생성된 메시지: {res.json()}")
    # 3. 알림 전송 (모의)
    for channel in template['notification']:
        print(f"[NOTIFY] {channel}로 알림 전송: {data}")

# 기존 단일 콘텐츠 생성 함수도 유지
def generate_content(prompt):
    api_url = config['content_engine']['api_url']
    api_key = config['content_engine']['api_key']
    res = requests.post(api_url, json={"prompt": prompt, "max_tokens": 300},
                        headers={"Authorization": f"Bearer {api_key}"})
    return res.json()

# 7. 평가/교체 자동화 함수 (예시)
def auto_evaluate_and_update():
    print("최신 AI 툴 자동 평가 및 교체 시도")
    # 예시: 더 나은 툴 발견 시 config.json 자동 수정
    # config['content_engine']['provider'] = "Gemini"
    # with open('config.json', 'w') as f: json.dump(config, f)

# 8. 운영 자동화 스케줄러
schedule.every().day.at("03:00").do(auto_evaluate_and_update)

# 9. 메인 루프
if __name__ == "__main__":
    # 예시: 병원 동행 서비스 워크플로우 실행
    run_service_workflow("병원 동행 서비스", {
        "고객명": "홍길동",
        "연락처": "010-1234-5678",
        "병원명": "서울대병원",
        "진료일시": "2026-06-01 10:00",
        "특이사항": "휠체어 필요"
    })
    # 기존 AI 콘텐츠 생성 예시
    print(generate_content("여성안전 동행 서비스 홍보 콘텐츠 생성"))
    while True:
        schedule.run_pending()
        time.sleep(60)
