# MDM сервер SafeMobile

## Описание
Новая инкарнация MDM сервера
Теперь на FastApi и Asyncpg

## Работа в gitlab repo
[Правила работы в репозитории](http://gitlab.local/mdmserver/mdmserver/-/wikis/Правила-работы-в-репозитории)

## Установка и запуск
Создать виртуальное окружение  
`python3 -m venv env3`  

Активировать виртуальное окружение  
```
# Linux:
source env/bin/activate

# Windows:
env\Scripts\activate.bat
```

Установить зависимости
`pip install -r requirements.txt`

Запуск:
`python3 src/uvicorn_run.py`

