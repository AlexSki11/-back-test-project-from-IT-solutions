# -back-test-project-from-IT-solutions

Тестовое задание от IT-solutions(back)

Для начали работы нужно:

1) Создать виртуальное окружение python -m venv env и активировать его -  
 Windows: `venv\Scripts\activate.bat` 
 Linux/macOS: `source venv/bin/activate`
2) Установить библиотеки с 
 requirements `pip install -r requirements.txt`
 3) Перейти в папку с файлом manage.py
 4) Создать базу данных `py manage.py migrate`
 5) Запустить сервер `py manage.py runserver`

Теперь вам доступы такие ссылки:
* Аккаунт
1. ip:port/accounts/signup - Регистрация
2. ip:port/accounts/login - Войти в аккаунт 
* Записи машин
3. ip:port/ - список записей
4. ip:port/car_create - Создать запись
5. ip:port/car_delete/pk - удалить запись 
6. ip:port/car_edit/pk - изменить запись
7. ip:port/car_detail/pk - запись определенной машины
* Комментарии
8. ip:port/comment_create?id=pk - создать комментарий
9. ip:port/comment_delete/pk - удалить комментарий
10. ip:port/comment_edit/pk - изменить комментарий

Доступные API:

* GET ip:port/api/cars/ — получение списка автомобилей.
* GET ip:port/api/cars/id/ — получение информации о конкретном
автомобиле.
* POST ip:port/api/cars/ — создание нового автомобиля.
* PUT ip:port/api/cars/id/ — обновление информации о
автомобиле.
* DELETE ip:port/api/cars/id/ — удаление автомобиля.
* GET ip:port/api/cars/id/comments/ — получение комментариев к
автомобилю.
* POST ip:port/api/cars/id/comments/ — добавление нового
комментария к автомобилю.

В случае изменение моделей приложения "models" применить makemigrations

Модели так-же доступны для изменения в админ панели
Чтобы создать админ пользователя нужно в терминале:
* `py manage.py createsuperuser` - заполнить последовательно поля

После этого вы сможете зайти в админ панель по ссылке 
ip:port/admin/
