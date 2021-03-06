# json(JavaScript Object Notation) : 키-값 쌍
# 특정 프로그래밍 언어나 플랫폼 독립적
# 인터넷에서 데이터를 주고 받을 때 많이 사용
# {"name":"hong","age":30}

# 기본라이브러리 이용 json, requests 사용
import json

data = """
    {
        "id":"01",
        "language":"Java",
        "edition":"third",
        "author":"Heart",
        "history":
        [
            {
                "date":"2021-03-03",
                "item":"iPhone"
            },
            {
                "date":"2021-03-04",
                "item":"android"
            }
        ]
    }
"""
# json 형식의 데이터를 파이썬 객체로 역직렬화(딕셔너리 형태로 변환)
json_data = json.loads(data)

print(type(json_data))  # <class 'dict'>
print(json_data)

print(json_data["id"])
print(json_data["history"][0])
print(json_data["history"][0]["date"])
