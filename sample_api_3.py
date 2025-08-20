'''
POST로 리소스 생성(등록)

'''

import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title" : "수연이의 API 테스트 연습",
    "body" : "이건 처음 실습 하는 POST 리소스 생성 하는 중입니다.",
    "userId" : 1
}

r = requests.post(url, json=payload, headers={"Content-Type" : "application/json"})


print("상태코드 : ", r.status_code)
print("응답 :", r.json())
