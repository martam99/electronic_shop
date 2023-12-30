Данный проект из себя представляет онлайн платформу торговой сети электроники с API интерфейсом и админ-панелью. 
Сеть представляет из себя иерархическую структуру из трёх уровней:
Завод(factory)
Розничная сеть(Retail)
Индивидуальный предприниматель (SP)
...................................
Для запуска программы нужно установить следующие пакеты:
asgiref==3.7.2
Django==5.0
django-filter==23.5
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1
drf-yasg==1.21.7
generics==6.0.0
inflection==0.5.1
packaging==23.2
psycopg2-binary==2.9.9
PyJWT==2.8.0
python-dotenv==1.0.0
pytz==2023.3.post1
PyYAML==6.0.1
sqlparse==0.4.4
tzdata==2023.3
uritemplate==4.1.1
....................
Для начала запуска проекта установить все пакеты и сохранить в виртуальной окружности.

Для создания суперпользователя нужно в файле «.env_sample» ввести свои данные и ввести команду python manage.py csu
...................
Для создания группы сотрудников ввести команду python manage.py emp_group
...................
Для создания активного пользователя и добавления пользователя в группу сотрудников python manage.py cu
...................
Для создания базы данных в .env_sample введите свои данные. Далее в терминале введите:
psql -U (имя пользователя ) -d (имя основной базы) и через команду create database (имя вашей базы); создайте базу данных и сделайте миграции:
python manage.py makemigrations и python manage.py migrate
..................
Запустить программу python manage.py runserver
.................
Для авторизации пользователя сделать post запрос по урлу http://127.0.0.1:8000/employee/api/token и ввести свои данные (email и password). 
После получения jwt токена вставить токен и делать get и post запросы к базе данных․
․․․․․․․․․․․․․․․․․
Для фильтрации магазинов по стране ввести в строке запроса «урл+/?contacts__country=страна»
................
Чтобы открыть документацию ввести: http://127.0.0.1:8000/redoc/ или http://127.0.0.1:8000/swagger/
․․․․․․․․․․․․․․․․
