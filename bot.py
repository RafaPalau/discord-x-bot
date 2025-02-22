from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

from login import discord_login
from cookies_handler import save_cookies, load_cookies
from mouse_utils import human_like_mouse_move

# 🔄 Carrega variáveis do .env
load_dotenv(override=True)

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
DISCORD_EMAIL = os.getenv("DISCORD_EMAIL")
DISCORD_PASSWORD = os.getenv("DISCORD_PASSWORD")
DISCORD_CHANNEL_URL = os.getenv("DISCORD_CHANNEL_URL")

# ⚙️ Configurações do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Inicializa o navegador
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)

# Tenta carregar cookies primeiro
driver.get("https://discord.com/app")
if not load_cookies(driver):
    discord_login(driver, DISCORD_EMAIL, DISCORD_PASSWORD)
    save_cookies(driver)

# Acessa o canal do Discord
driver.get(DISCORD_CHANNEL_URL)
time.sleep(5)

# Busca links do Twitter nas mensagens
messages = driver.find_elements(By.CSS_SELECTOR, 'a[href*="twitter.com"]')
for link in messages:
    tweet_url = link.get_attribute("href")
    print(f"👉 Encontrado Tweet: {tweet_url}")

    # Abre o link do Twitter em nova aba
    driver.execute_script(f"window.open('{tweet_url}', '_blank');")
    time.sleep(3)

    # Muda para a aba do Twitter
    driver.switch_to.window(driver.window_handles[-1])

    # Curtir o Tweet
    try:
        like_button = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="like"]')
        like_button.click()
        print("💖 Tweet curtido com sucesso!")
    except Exception as e:
        print("⚠️ Erro ao curtir o tweet:", e)

    # Fecha a aba do Twitter e volta ao Discord
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# ✅ Finaliza
print("✅ Finalizado.")
driver.quit()
