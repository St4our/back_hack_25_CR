🚀 Запуск проекта с помощью Docker
Этот проект состоит из фронтенда и бэкенда, которые разворачиваются с помощью Docker Compose.

📌 Установка необходимых программ
Перед началом работы необходимо установить:

Docker
Docker Compose
Проверить установку можно командами:

sh
Копировать
Редактировать
docker --version
docker compose version
📥 Клонирование репозиториев
Склонируйте фронтенд и бэкенд в отдельные папки:

sh
Копировать
Редактировать
git clone https://github.com/St4our/front_nack_25_CR.git front_nack_25_CR
git clone https://github.com/St4our/back_hack_25_CR.git back_hack_25_CR

В директории back_hack_25_CR создать папку static и файл .env
Наполнение .env:
```
EMAIL_ADDRESS=docgpt@yandex.ru
EMAIL_PASSWORD=lokjooyguvnaekfh
EMAIL_SERVER=smtp.yandex.ru

API_LINK=http://127.0.0.1:9000

JWT_SECRET=popka0gurca
```

cd back_hack_25_CR
sudo docker build -t api -f api.dockerfile .
sudo docker run --name api -d -p 4000:4000 api

sudo docker build -t admin -f admin.dockerfile .
sudo docker run --name admin -d -p 5000:5000 admin

cd ..
cd front_nack_25_CR

Заходим в папку фронта

cd hac-25-admin
docker build -t vue-app .
docker run --name admin_app -p 80:80 -d vue-app

cd ..
cd hac-25-user
docker build -t vue-app .
docker run --name user_app -p 80:80 -d vue-app



Если недостаточно информации или есть вопросы, обращайтесь 👉https://t.me/StanislavD_1

модуль ИИ чат
Для запуска:

Распакуйте в нужную папку архив chat.zip

Установка зависимостей (если зависимости прописаны в файле req.txt): 

pip install -r req.txt 
или
pip3 install -r req.txt
 

Запуск файла на ubuntu :

nohup python -u chat.py &
или
nohup python3 -u chat.py & 

Запуск файла на windows :

python chat.py
или
python3 chat.py

чат запускается как отдельная страница на:
http://ваш_ip:9000/ai #на данный момент с фронта на vue обращение к нашему сайту, можете изменить на ваш
