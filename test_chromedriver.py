from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# Caminho direto para o ChromeDriver
CHROME_DRIVER_PATH = "C:\\chromedriver-win64\\chromedriver.exe"

# Verifica se o caminho existe
if not os.path.exists(CHROME_DRIVER_PATH):
    print(f"❌ Caminho inválido: {CHROME_DRIVER_PATH}")
else:
    print(f"✅ Caminho correto: {CHROME_DRIVER_PATH}")

# Configurações do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Inicializa o ChromeDriver
try:
    driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH), options=options)
    driver.get("https://google.com")
    print("🚀 ChromeDriver funcionando corretamente.")
    driver.quit()
except Exception as e:
    print(f"⚠️ Erro encontrado: {e}")
