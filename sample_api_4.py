'''
PUT vs PATCH 차이 체감

'''

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

#PUT : 전체 교체(보낸 필드가 "전부"가 기준)
put_body = {"id":1, "title" : "전체교체", "body" : "본문", "userId" : 1}
print("Put : " , requests.put(url, json=put_body).json())

patch_body = {"title" : "제목만 수정"}
print("patch:", requests.patch(url, json=patch_body).json())