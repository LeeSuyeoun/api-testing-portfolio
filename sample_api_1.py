'''
GET로 JSON 받기 (조회)
'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1" #공개 Mock API
r = requests.get(url, headers={"Accept" : "application/json"})

print("상태코드 : ", r.status_code)
print("컨텐츠 타입 : ", r.headers.get("Content-Type"))

data = r.json()

print("글 ID : ", data["id"])
print("제목 : ", data["title"])
