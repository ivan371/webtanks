import os

# Ставим django.
sudo apt-get install python-pip
pip install django

# Копируем программу из репозитория.
git clone https://github.com/ivan371/webtanks/mysite

# Запускаем сервер
cd mysite
python manage.py runserver

# Открываем страничку в браузере
gnome-open http://127.0.0.1:8000/aipyweb
