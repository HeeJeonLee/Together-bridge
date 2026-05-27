# requirements: crewai, requests, schedule
import requests, json, schedule, time
from crewai import Crew, Agent

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

# 6. 콘텐츠 생성 함수
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
    print(generate_content("여성안전 동행 서비스 홍보 콘텐츠 생성"))
    while True:
        schedule.run_pending()
        time.sleep(60)
