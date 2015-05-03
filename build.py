import os

os.system("git clone https://github.com/ivan371/webtanks")

os.chdir("webtanks/sources/tanks")

os.system("python manage.py runserver")

os.system("gnome-open http://127.0.0.1:8000/webtanks")
