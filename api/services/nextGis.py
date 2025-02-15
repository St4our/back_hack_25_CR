import requests
from typing import Dict, Any
from requests.auth import HTTPBasicAuth

username = 'hackathon_18'
password = 'hackathon_18_25'
auth = HTTPBasicAuth(username, password)

# Базовый URL API
base_url = 'https://geois2.orb.ru/api'

# Идентификатор векторного слоя
layer_id = 8786

async def add_feature(layer_id: int, feature_data: Dict[str, Any]) -> Dict[str, Any]:
    url = f'{base_url}/resource/{layer_id}/feature/'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, auth=auth, json=feature_data)
    return response.json()

async def upload_file(file_path: str, file_name: str) -> Dict[str, Any]:
    url = f'{base_url}/component/file_upload/'
    headers = {
        'Accept': '*/*'
    }
    files = {
        'file': (file_name, open(file_path, 'rb')),
        'name': (None, file_name)
    }
    response = requests.post(url, headers=headers, auth=auth, files=files)
    return response.json()

# 4. Прикрепление файла к записи
async def attach_file(layer_id: int, feature_id: int, file_data: Dict[str, Any]) -> Dict[str, Any]:
    url = f'{base_url}/resource/{layer_id}/feature/{feature_id}/attachment/'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, auth=auth, json=file_data)
    return response.json()

# 5. Изменение записи
async def update_feature(layer_id: int, feature_id: int, feature_data: Dict[str, Any]) -> Dict[str, Any]:
    url = f'{base_url}/resource/{layer_id}/feature/{feature_id}'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.put(url, headers=headers, auth=auth, json=feature_data)
    return response.json()

# 6. Удаление записи
async def delete_features(layer_id: int, feature_ids: list) -> int:
    url = f'{base_url}/resource/{layer_id}/feature/'
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/json'
    }
    response = requests.delete(url, headers=headers, auth=auth, json=feature_ids)
    return response.status_code

# 7. Удаление вложений
async def delete_attachment(layer_id: int, feature_id: int, attachment_id: int) -> int:
    url = f'{base_url}/resource/{layer_id}/feature/{feature_id}/attachment/{attachment_id}'
    headers = {
        'Accept': '*/*'
    }
    response = requests.delete(url, headers=headers, auth=auth)
    return response.status_code

# 8. Запрос информации по записи
async def get_features(layer_id: int) -> Dict[str, Any]:
    url = f'{base_url}/resource/{layer_id}/feature/'
    headers = {
        'Accept': '*/*'
    }
    response = requests.get(url, headers=headers, auth=auth)
    return response.json()
