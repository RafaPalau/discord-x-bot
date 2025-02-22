from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

CHROME_DRIVER_PATH = "C:\\chromedriver-win64\\chromedriver.exe"  # Ajuste se necessário

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

try:
    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
    driver.get("https://google.com")
    print("🚀 Navegador abriu com sucesso.")
    driver.quit()
except Exception as e:
    print(f"⚠️ Erro ao abrir o navegador: {e}")
