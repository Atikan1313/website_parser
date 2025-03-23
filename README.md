# Site parser (where authorization is required) in python with regular sending of notifications to a telegram bot based on selenium on windows 10/11

## Setup
1. Install globally:

- python>=3.13.2;
- pip>=24.3.1;
2. Register `PATH` (if you did not do this when installing python globally) environment variable;
3. Install a virtual environment for further convenience of working with the code and to avoid cluttering the working machine with unnecessary packages:
- In the project folder:
```python
python -m venv venv
venv\scripts\activate
```
4. Install python dependencies:
```python
pip install -r requirements.txt
```
5. You will need to add your data to the file: `secrets.py`, which should contain:
- URL - a link to the site where the information will be parsed;
- `LOGIN_URL` - a link to authorization;
- `USERNAME` - login from the account;
- `PASSWORD` - password from the account;
- `class_name_prs` - the class by which the parser will search for the necessary data for output;
- `class_name_btn_auth` - the class by which the parser will search for the button for authorization;
- `TOKEN` - telegram token;
- `CHAT_ID` - user id to which notification will be sent;
- `message_text` - message to be sent in telegram PM.
6. Run the parser with the command:
```python
python main.py
```
7. Enter:
- Start hour in 24-hour format;
- End hour in 24-hour format;
- Start minute in 24-hour format;
- End minute in 24-hour format.
8. Wait for notification in PM.

## Upcoming improvements:
- Adding the ability to enable `--headles` mode. It is written about [here](https://www.selenium.dev/blog/2023/headless-is-going-away/);
- Implementation of improved stability of the parser on Linux servers:
- Disabling hardware acceleration via GPU;
- Using `/tmp` instead of `/dev/shm` (shared memory between processes in Linux);
- Disabling the isolated environment (sandbox) Chrome.
---

# Парсер сайтов (где требуется авторизация) на python с регулярной отправкой уведомлений в бот-телеграм на основе selenium на windows 10/11

## Настройка
1. Установить глобально: 
- python>=3.13.2;
- pip>=24.3.1;
2. Прописать `PATH` (если не сделали это при установки python глобально) переменную среды;
3. Установить виртуальное окружение для дальнейшего удобства рвботы с кодом и чтобы не засорять рабочую машину ненужными пакетами:
- В папке с проектом:
```python
python -m venv venv
venv\scripts\activate
```
4. Установить зависимости python:
```python
pip install -r requirements.txt
```
5. Вам понадобится добавить свои данные в файл: `secrets.py`, в котором должны быть:
- URL - ссылка на сайт, где будет парситься информация;
- `LOGIN_URL`- ссылка на авторизацию;
- `USERNAME` - логин от учетной записи;
- `PASSWORD` - пароль от учетной записи;
- `class_name_prs` - класс по которому парсер будет искать нужную для вывода данных;
- `class_name_btn_auth` - класс по которому парсер будет искать кнопку для авторизации;
- `TOKEN` - токен телеграма;
- `CHAT_ID` - id пользователя, которому будет приходить уведомление;
- `message_text` - сообщение которое будет приходить в л.с. телеграма.
6. Запустить парсер командой:
```python
python main.py
```
7. Ввести:
- Начальный час в формате 24-х часов;
- Конечный час в формате 24-х часов;
- Начальную минуту в формате 24-х часов;
- Конечную минуту в формате 24-х часов.
8. Ожидать уведомления в л.с.

## Предстоящие улучшения:
- Добавление возможности включения режима `--headles`. Про него написано [тут](https://www.selenium.dev/blog/2023/headless-is-going-away/);
- Реализация улучшения стабильности работы парсера на серверах linux:
    - Отключение аппаратного ускорения через GPU;
    - Использование `/tmp` вместо `/dev/shm` (общая память между процессами в Linux);
    - Отключение изолированной среды (sandbox) Chrome.