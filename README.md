# Sites Monitoring Utility

This utility check status your sites.

Now it contain check below:

- the server response status HTTP 200
- domain name paid on 1 month

# Requirements

- Python3.6
- Virtualenv

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Before run script you should add sites which you want to monitor in text file. Format below:
```
http://site1.xx
http://site2.xx
....
```

# Example launch script

You can run the script like this:
```bash
$ python3.6 check_sites_health.py <path_to_file> 
```
Example result:
```bash
https://devman.org: [OK][OK]
http://yandex.ru: [OK][OK]
http://111.com: [OK][OK]
```

# Sites Monitoring Utility

Данная утилита позволяет автоматически проверять состояние ваших сайтов.

В данных момент осуществляются следующие проверки:

- сервер отвечает на запрос статусом HTTP 200
- доменное имя проплачено как минимум на один месяц вперед

# Требования к окружению

- Python3.6
- Virtualenv

# Как установить

Python3.6 должен быть установлен. Затем используйте pip (или pip3, если есть конфликт со старой версией Python2) для установки зависимостей:
```bash
$ pip install -r requirements.txt # alternatively try pip3
```
Рекомендуется использовать [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) для лучшей изоляции.

Перед запуском необходимо добавить те сайты, которые необходимо мониторить, в текстовый файл. Формат файла ниже:
```
http://site1.xx
http://site2.xx
....
```

# Примеры запуска скриптов

Запуск скрипта осуществляется следующим образом:
```bash
$ python3.6 check_sites_health.py sites.txt 
```

Результат работы:
```bash
https://devman.org: [OK][OK]
http://yandex.ru: [OK][OK]
http://111.com: [OK][OK]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
