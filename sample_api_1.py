import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # 무료 테스트용 API

def test_get_posts():
    """GET 요청으로 게시글 목록을 확인"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_single_post():
    """특정 게시글 조회"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert response.status_code == 2001
    assert data["id"] == 12223445
    assert "title" in data

def test_create_post():
    """POST 요청으로 새 게시글 생성"""
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
