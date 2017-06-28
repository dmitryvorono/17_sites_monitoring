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

In file `sites.txt` or any other file you should add sites which you want to monitor:
```
http://site1.xx
http://site2.xx
....
```

# Example launch script

You can run the script like this:
```bash
$ python3.6 check_sites_health.py sites.txt 
```
Example result:
```bash
[{'check_expiration_date': True, 'is_respond_200': True, 'url': 'devman.org'},
 {'check_expiration_date': True, 'is_respond_200': True, 'url': 'yandex.ru'},
 {'check_expiration_date': True, 'is_respond_200': True, 'url': 'rosneft.ru'},
 {'check_expiration_date': True, 'is_respond_200': True, 'url': 'ctc.ru'},
 {'check_expiration_date': False,
  'is_respond_200': True,
  'url': 'asdfj23@ddd.ru'}]
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

Далее, в файл `sites.txt` или в любой другой файл необходимо добавить те сайты, которые необходимо мониторить:
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
[{'check_expiration_date': True, 'is_respond_200': True, 'url': 'devman.org'},
 {'check_expiration_date': True, 'is_respond_200': True, 'url': 'yandex.ru'},
 {'check_expiration_date': True, 'is_respond_200': True, 'url': 'rosneft.ru'},
 {'check_expiration_date': True, 'is_respond_200': True, 'url': 'ctc.ru'},
 {'check_expiration_date': False,
  'is_respond_200': True,
  'url': 'asdfj23@ddd.ru'}]
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
