'''
DELETE 삭제

'''

import requests

r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print("상태 코드 : ", r.status_code)