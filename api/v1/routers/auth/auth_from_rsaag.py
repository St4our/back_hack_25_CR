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

b'{"code":"def50200c82618cab570ae4accb9004bdc79556bc1f67041a51ffad0ff7bb81f3f147b5280830440a0568e219d8bbea6d67e9c891918f0a13fbbf010e08ddcaadde89aa649878ef73e9f337a80941f833604952a97e8d7276a42cbc33e1a389b2589838a00324dea116b5b2aa347a177e267d7faaeea8d773f4e00ff62bbd6744d1f17977b7d7608506d6049f689c7dfbff826d6a36a85e6ba36690f1120d50b4b41140a5493cc4553b57a2567f52aab10d6495e47be8277ff09abde8116d79b960f51c784782bf71664829c38fcb0d51528081992b514e1c2a3f1464b7fd49f3bea28e30799b6ea306d57c8227aa9260dac3795b26c7ecbb82fcd6ff62974e4e96e659a098a344932aa0066274aeb5bc849d75b8161e4af307b917686b422e93f761d8851a4aa6b9ec44472db2b4bade1624bcf769db9c31e71cc43d8daeeb6bb38d5d213c77f0a18a97040d128a7a8ab6ef1f6f15ffcec428d0b6f31420c20e05486ecb9f7bdd422fc5b3df3e2017c2d48fcc72fcd2e8b28a4b5f2214fd5","state":"http://hackathon-1.orb.ru/"}'

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
    user_info_response = requests.get(f"{ELK_USER_INFO_URL}?scope=rsaag_id+personal_data+esia_data+email+phone", headers=headers)
    
    if user_info_response.status_code != 200:
        return f"Ошибка при получении данных пользователя: {user_info_response.text}", user_info_response.status_code
    
    user_info = user_info_response.json()
    return JSONResponse(content=user_info)