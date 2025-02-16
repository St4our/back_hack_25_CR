import requests
from fastapi import APIRouter, Request, HTTPException
import httpx
from fastapi.responses import JSONResponse

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
    code = request.query_params.get("code")
    state = request.query_params.get("state")
    
    if not code:
        return "Ошибка: отсутствует временный код авторизации", 400
    
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
    
    # Запрос сведений о пользователе
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(f"{ELK_USER_INFO_URL}?scope=rsaag_id+personal_data+esia_data+email+phone", headers=headers)
    
    if user_info_response.status_code != 200:
        return f"Ошибка при получении данных пользователя: {user_info_response.text}", user_info_response.status_code
    
    user_info = user_info_response.json()
    return JSONResponse(content=user_info)