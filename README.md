# polls app

django приложение для создания и проведения опросов. на данный момент развернут по адресу: https://kleprer.pythonanywhere.com/

## функционал

- просмотр списка доступных опросов
- голосование за один из вариантов ответа
- просмотр статистики голосования
- создание опросов (для админа)

## установка

1. склонируйте репозиторий:
```bash
git clone https://github.com/kleprer/test_project.git
cd test_project
```
2. создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
3. установите зависимости:
```bash
pip install -r requirements.txt
```
3. выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
4. запустите сервер:
```bash
python manage.py runserver
```
