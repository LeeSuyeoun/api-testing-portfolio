'''
쿼리 파라미터(필터) 써보기

'''

import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId" : 1, "_limit" : 3} # postId=1의 댓글 3개만
r = requests.get(url, params=params)

print("요청 URL : ", r.url) #실제 호출된 전체 URL 확인
print("개수 :", len(r.json()))
