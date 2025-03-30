import requests

base_url = "https://ru.yougile.com"
TOKEN = '#ВСТАВИТЬ СЮДА ТОКЕН'
my_headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
    }


def test_create_project():
    body = {
        "title": "Morganite",
        "users": {
            "918e6d8e-6d6a-48cb-b0f5-31d1173705d4": "admin"
        }
    }
    resp = requests.post(base_url+'/api-v2/projects', json = body, headers = my_headers)
    assert 'id' in resp.json()
    assert resp.status_code == 201


def test_create_project_without_headers():
    body = {
        "title": "Morganite",
        "users": {
            "918e6d8e-6d6a-48cb-b0f5-31d1173705d4": "admin"
        }
    }
    resp = requests.post(base_url+'/api-v2/projects', json=body)
    assert resp.status_code == 401
    assert resp.json()["message"] == "Unauthorized"


def test_update_project():
    body_before = {
        "title": "Morganite",
        "users": {
            "918e6d8e-6d6a-48cb-b0f5-31d1173705d4": "admin"
        }
    }
    body_after = {
        "title": "Morganite_new"
    }
    resp = requests.post(base_url+'/api-v2/projects', json=body_before, headers = my_headers)
    project_id = resp.json()['id']
    assert resp.status_code == 201
    resp_put = requests.put(base_url+'/api-v2/projects/'+project_id, json=body_after, headers = my_headers)
    assert resp_put.status_code == 200
    assert resp_put.json()['id'] == project_id


def test_update_project_not_found():
    body_after = {
        "title": "Morganite_new"
    }
    project_id = '0987654321'
    resp_put = requests.put(base_url+'/api-v2/projects/'+project_id, json=body_after, headers = my_headers)
    assert resp_put.status_code == 404
    assert resp_put.json()['message'] == 'Проект не найден'


def test_get_project():
    body = {
        "title": "Morganite",
        "users": {
            "918e6d8e-6d6a-48cb-b0f5-31d1173705d4": "admin"
        }
    }
    resp = requests.post(base_url+'/api-v2/projects', json=body, headers = my_headers)
    project_id = resp.json()['id']
    assert resp.status_code == 201
    resp_get = requests.get(base_url+'/api-v2/projects/'+project_id, headers = my_headers)
    assert resp_get.status_code == 200
    assert resp_get.json()['title'] == 'Morganite'


def test_get_project_not_found():
    project_id = 'asdfghjkkl'
    resp_get = requests.get(base_url+'/api-v2/projects/'+project_id, headers = my_headers)
    assert resp_get.status_code == 404
    assert resp_get.json()['message'] == 'Проект не найден'
