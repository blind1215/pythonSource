import requests

with requests.Session() as s:
    r = s.get("https://api.github.com/events", timeout=0.001)

    # 수신 상태 체크 함수(상태 체크 시 이상이 있으면 다음 문장을 처리 안함)
    r.raise_for_status()

    print(r.text)