from dependencies import *

start_hour = int(input('Введите начальный час в формате 24-х часов: ... '))
end_hour = int(input('Введите конечный час в формате 24-х часов: ... '))
start_min = int(input('Введите начальную минуту в формате 24-х часов: ... '))
end_min = int(input('Введите конечную минуту в формате 24-х часов: ... '))

# Authentication
# Аутентификация
def authenticate(class_name_btn_auth):
    options = Options()
    options.add_argument('--headless')
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # Отключает флаг enable-automation, который указывает, что браузер запущен через Selenium / Disables the enable-automation flag, which indicates that the browser is launched via Selenium.
    options.add_experimental_option("useAutomationExtension", False) # Отключает автоматическое расширение, которое браузер добавляет при запуске. / Disables the automatic extension that the browser adds on startup.
    options.add_argument("--disable-blink-features=AutomationControlled") # Отключает специальную функцию , которая помечает браузер как управляемый автоматизированными инструментами. / Disables a special feature that marks the browser as being controlled by automated tools.
    options.add_argument("--disable-webrtc") # Отключает WebRTC, который может раскрыть реальный IP-адрес пользователя. / Disables WebRTC, which can reveal the user's real IP address.
    options.add_argument('--disable-gpu') # Отключает аппаратное ускорение через GPU / Disables hardware acceleration via GPU
    # options.add_argument('--disable-dev-shm-usage') # При запуске в контейнерах Docker стандартный /dev/shm имеет ограниченный размер, что может вызывать сбои. / When running in Docker containers, the default /dev/shm has a limited size, which can cause crashes.
    # options.add_argument('--no-sandbox') # Позволяет запускать браузер без ошибок в контейнерах и виртуальных машинах. / Allows you to run the browser without errors in containers and virtual machines.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(LOGIN_URL)
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    driver.find_element(By.ID, class_name_btn_auth).click()
    return driver

# Parser
# Парсер
def parse_page(driver, class_name_prs):
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    value = soup.find('div', {'class': class_name_prs}).text.strip()
    print('Result: ', value)
    return value

# Generates a random time within a given range
# Генерирует случайное время в пределах заданного диапазона
def get_random_time(start_hour, end_hour, start_min, end_min):
    start_time = datetime.now().replace(hour=start_hour, minute=0, second=0, microsecond=0)
    end_time = datetime.now().replace(hour=end_hour, minute=0, second=0, microsecond=0)

    # Generate a random hour and minute
    # Генерируем случайный час и минуту
    random_hour = random.randint(start_hour, end_hour - 1)
    random_minute = random.randint(start_min, end_min)

    # Create random time
    # Создаем случайное время
    random_time = start_time.replace(hour=random_hour, minute=random_minute)

    # If the random time has already passed today, then we set it to tomorrow
    # Если случайное время уже прошло сегодня, то устанавливаем в завтрашний день
    if random_time < datetime.now():
        random_time += timedelta(days=1)

    return random_time

# We get a random time in the specified range
# Получаем случайное время в указанном диапазоне
def main():
    random_time = get_random_time(start_hour, end_hour, start_min, end_min)
    print(f"Событие запланировано на: {random_time.strftime('%H:%M')}")

    # Calculate the delay before triggering
    # Рассчитываем задержку до срабатывания
    time_to_wait = (random_time - datetime.now()).total_seconds()
    
    # We wait until the specified time
    # Ожидаем до заданного времени
    time.sleep(time_to_wait)

    # We carry out the main task
    # Выполняем основную задачу
    print("Time's up! We're doing the main event...")
    job(message_text)

# Sending a message in telegram private messages
# Отправка сообщения в л.с. телеграма
async def send_message(token, chat_id, message):
    # Create an instance of the Bot class
    # Создаем экземпляр класса Bot
    bot = Bot(token=token)
    # Send a message to the specified chat
    # Отправляем сообщение в указанный чат
    await bot.send_message(chat_id=chat_id, text=message)

# Task planning service
# Служба планирования задач
def job(message_text):
    driver = authenticate(class_name_btn_auth)
    value = parse_page(driver, class_name_prs)

    if int(value) == 0:
        if __name__ == "__main__":
            asyncio.run(send_message(TOKEN, CHAT_ID, message_text))
    driver.quit()

if __name__ == "__main__":
    while True:
        main()