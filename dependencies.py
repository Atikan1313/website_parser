from secrets import URL, LOGIN_URL, USERNAME, PASSWORD, class_name_btn_auth, class_name_prs, TOKEN, CHAT_ID, message_text
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import schedule
import time
import random
from datetime import datetime, timedelta
import asyncio
from aiogram import Bot