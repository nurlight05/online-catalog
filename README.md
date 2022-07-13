<div align="center">
  <h3 align="center">Online catalog</h3>
</div>







## С чего начать
Весь список модулей для полноценной работы проекта находится в файле `requirements.txt`. Вы можете установить их с помощью менеджера пакетов `pip`.

<p align="right">(<a href="#top">Наверх</a>)</p>



### Инструменты

* [![Python][Python]][Python-url]
* [![Django][Django]][Django-url]
* [![Bootstrap][Bootstrap]][Bootstrap-url]
* [![Postgresql][Postgresql]][Postgresql-url]
* [![VSCode][VSCode]][VSCode-url]

<p align="right">(<a href="#top">Наверх</a>)</p>

## Начало
Сначала клонируйте проект из репозиторий с помощью следующей команды. 
* git
  ```sh
  $ git clone https://github.com/nurlight05/online-catalog.git
  ```

### Установка

_Ниже показаны важные моменты во время установки проекта._

1. Прежде всего убедитесь, чтобы в переменной _INSTALLED_APPS_ которая находится в `settings.py` есть следующие названия приложении
   ```sh
   ...
   'employee',
   'django_seed',
   'django_extensions',
   'rest_framework',
   ...
   ```
2. Потом настройте данные _Postgresql_ в том же файле `settings.py`
   ```sh
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'db_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'server_ip or localhost',
           'PORT': '5432',
       }
   }
   ```
3. На следующем шагу создайте миграции
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Теперь можно запустить следующую команду чтобы заполнять БД данными
   ```sh
   python manage.py runscript -v3 seed
   ```

<p align="right">(<a href="#top">Наверх</a>)</p>


## Использование

1. Чтобы изменить лимит результатов API для получения список сотрудников, вы можете изменить параметры DRF Paginator в `settings.py`
   ```sh
   REST_FRAMEWORK = {
       'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
       'PAGE_SIZE': 10
   }
   ```
2. Так как API сделан с помощью DRF Serializer, вы можете изменить глубину рекурсий
   ```sh
   ...
   fields = ('name', 'position', 'hired', 'salary', 'supervisor', 'employees')
   depth = 4
   ...
   ```
3. Путь к API
   ```sh
   127.0.0.1:8000/api/epmloyees/
   ```

<p align="right">(<a href="#top">Наверх</a>)</p>



## Функционалы

- [x] API которая возвращает все данные сотрудников
- [x] Логин и регистрация
- [x] Поиск по всем параметрам сотрудников
- [x] Сортировка по всем данным сотрудников
- [x] Кнопка для скачивания все данные из БД как JSON файл

<p align="right">(<a href="#top">Наверх</a>)</p>


## Контакты

Абдраим Нурболат - [@nur_lan_uly](https://www.instagram.com/nur_lan_uly/) - nurlight05@gmail.com

Ссылка проекта: [https://github.com/nurlight05/online-catalog](https://github.com/nurlight05/online-catalog)

<p align="right">(<a href="#top">Наверх</a>)</p>

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com
[VSCode]: https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white
[VSCode-url]: https://code.visualstudio.com
[Bootstrap]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Postgresql]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org
