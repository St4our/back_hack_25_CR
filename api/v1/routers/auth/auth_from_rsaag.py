import requests
from fastapi import APIRouter, Request, HTTPException
import httpx
from fastapi.responses import JSONResponse
import json

router = APIRouter(
    prefix="/login_from_rsaag"
)

CLIENT_ID = 28
CLIENT_SECRET = "2A5UHepXTRqdRMkYPSK3hq2WKH1JQA4jozThOVGxRe"
REDIRECT_URI = "http://hackathon-1.orb.ru/callback"
ELK_USER_INFO_URL = "https://lk.orb.ru/api/get_user"
ELK_TOKEN_URL = "https://lk.orb.ru/oauth/token"



@router.post('')
async def redirect_from_elk(request: Request):
    """Обрабатывает редирект с ЕЛК и получает токен доступа"""
    # Использование await для асинхронной функции
    body = await request.body()
    print(body)  # Печать байтовой строки запроса для дебага
    
    try:
        # Распарсить тело запроса
        body_json = json.loads(body)
        code = body_json.get("code")
        state = body_json.get("state")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Ошибка при декодировании тела запроса")
    
    if not code:
        raise HTTPException(status_code=400, detail="Ошибка: отсутствует временный код авторизации")
    
    
    # Запрос на получение access_token
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
        "grant_type": "authorization_code"
    }
    response = requests.post(ELK_TOKEN_URL, json=data)
    
    if response.status_code != 200:
        return f"Ошибка при получении токена: {response.text}", response.status_code
    
    tokens = response.json()
    access_token = tokens.get("access_token")
    print(tokens)
    
    # Запрос сведений о пользователе
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(f"{ELK_USER_INFO_URL}?scope=personal_data+email+auth_method", headers=headers)
    
    if user_info_response.status_code != 200:
        return f"Ошибка при получении данных пользователя: {user_info_response.text}", user_info_response.status_code
    
    user_info = user_info_response.json()
    return JSONResponse(content=user_info)