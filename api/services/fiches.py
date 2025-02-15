import cv2
import numpy as np
from PIL import Image, ImageEnhance
from time import sleep
import requests

api_gpt = 'chad-985321e2be134b2eb545670c8b85806bjk057368'

def enhance_image(image_path, output_path):
    # Загружаем изображение
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Улучшаем резкость
    sharpen_kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, sharpen_kernel)
    
    # Улучшаем контраст
    pil_image = Image.fromarray(sharpened)
    enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = enhancer.enhance(1.5)
    
    # Сохраняем результат
    enhanced_image.save(output_path)
    return output_path

def edit_gpt(topic):
    if topic != 'забудь':
        header = "Не добавляй комментариев от себя, мне нужна только отредактированная часть текста чтобы она была правильно построена и правильно структурирована в художественном стиле: "
        msg = f'{header}"{topic}"'
        msg += ' пришли только отредактированную часть текста'
        msg += ''

    if topic == 'забудь':
        header = ""
        msg = f'{topic}'
        msg += ''
        msg += ''

    try:
        request_json = {
            "message": f"{msg}",
            "api_key": api_gpt
        }

        response = requests.post(url='https://ask.chadgpt.ru/api/public/gpt-3.5',
                                json=request_json)
    except Exception as e:
        print(f'Ошибка! {e}')
        sleep(15)
        edit_gpt(topic)
        
    if response.status_code != 200:
        print(f'Ошибка! Код http-ответа: {response.status_code}')
        msg = 'Error'
        sleep(15)
        edit_gpt(topic)
    else:
        resp_json = response.json()

        if resp_json['is_success']:
            print(resp_json)
            resp_msg = resp_json['response']
            used_words = resp_json['used_words_count']
            print(f'Ответ от бота: {resp_msg}\nПотрачено слов: {used_words}')
            if '© 2021 Все права защищены.' in resp_msg:
                resp_msg = resp_msg.replace('© 2021 Все права защищены.', '')
            if 'Копирайтинг' in resp_msg:
                resp_msg = resp_msg.replace('Копирайтинг', '')
            if 'Текст:' in resp_msg:
                resp_msg = resp_msg.replace('Текст:', '')
            if 'Ответ от бота:' in resp_msg:
                resp_msg = resp_msg.replace('Ответ от бота:', '')
            if '#' in resp_msg:
                resp_msg = resp_msg.replace('#', '')
            if '*' in resp_msg:
                resp_msg = resp_msg.replace('*', '')
            if 'Вот отредактированная версия текста:' in resp_msg:
                resp_msg = resp_msg.replace('Вот отредактированная версия текста:', '')
            if 'Вот отредактированный вариант текста:' in resp_msg:
                resp_msg = resp_msg.replace('Вот отредактированный вариант текста:', '')
            if 'Вот отредактированный текст:' in resp_msg:
                resp_msg = resp_msg.replace('Вот отредактированный текст:', '')
            if 'Вот отредактированный' in resp_msg:
                resp_msg = resp_msg.replace('Вот отредактированный', '')
            if 'Вот отредактированная' in resp_msg:
                resp_msg = resp_msg.replace('Вот отредактированная', '')
            if 'версия текста:' in resp_msg:
                resp_msg = resp_msg.replace('версия текста:', '')
            if 'вариант текста:' in resp_msg:
                resp_msg = resp_msg.replace('вариант текста:', '')

            msg = resp_msg
            msg += '\n'
            msg += '\n'
            msg += '>Разработано командой CodeRed<'
            msg += '> https://coderedit.ru/ <'

            return msg
        
        else:
            sleep(15)
            print(resp_json)
            msg = 'Error'
            edit_gpt(topic)
