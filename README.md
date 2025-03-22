# Site parser (where authorization is required) in python with periodic information output based on selenium on windows 10/11

## Setup
1. Install globally:
- python>=3.13.2;
- pip>=24.3.1;
2. Specify `PATH` (if you did not do this when installing python globally) environment variable;
3. Set up a virtual environment for further convenience of working with the code and to avoid cluttering up the working machine with unnecessary packages:
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
- URL - link to the site where the information will be parsed;
- LOGIN_URL - authorization link;
- USERNAME - account login;
- PASSWORD - account password;
- class_name - the class by which the parser will search for the data needed to output.
6. Run the parser with the command:
```python
python main.py
```

## Upcoming improvements:
- Adding the ability to send notifications via a telegram bot;
- Adding the ability to enable the `--headles` mode. It is written about (here)[https://www.selenium.dev/blog/2023/headless-is-going-away/];
- Implementation of improved parser stability on Linux servers:
- Disabling hardware acceleration via GPU;
- Using `/tmp` instead of `/dev/shm` (shared memory between processes in Linux);
- Disabling the isolated environment (sandbox) Chrome.
---

# Парсер сайтов (где требуется авторизация) на python с периодическим выводом информации на основе selenium на windows 10/11

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
- LOGIN_URL- ссылка на авторизацию;
- USERNAME - логин от учетной записи;
- PASSWORD - пароль от учетной записи;
- class_name - класс по которому парсер будет искать нужную для вывода данных.
6. Запустить парсер командой:
```python
python main.py
```

## Предстоящие улучшения:
- Добавление возможности отправки уведомлений через бот-телеграм;
- Добавление возможности включения режима `--headles`. Про него написано (тут)[https://www.selenium.dev/blog/2023/headless-is-going-away/];
- Реализация улучшения стабильности работы парсера на серверах linux:
    - Отключение аппаратного ускорения через GPU;
    - Использование `/tmp` вместо `/dev/shm` (общая память между процессами в Linux);
    - Отключение изолированной среды (sandbox) Chrome.