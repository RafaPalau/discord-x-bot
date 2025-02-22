import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from mouse_utils import human_like_mouse_move

def discord_login(driver, email, password):
    """Realiza o login no Discord com movimentações humanas."""
    driver.get("https://discord.com/login")
    time.sleep(5)  # Aguarda o carregamento

    try:
        # Movimentação do mouse antes de interagir
        human_like_mouse_move(driver)

        # Preenche o e-mail
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys(email)
        time.sleep(1)

        # Movimentação novamente antes de preencher a senha
        human_like_mouse_move(driver)

        # Preenche a senha
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        time.sleep(1)

        # Clica no botão "Log In"
        password_input.send_keys(Keys.RETURN)
        print("⚡ Tentando logar...")
        time.sleep(7)  # Aguarda o login completar

    except Exception as e:
        print(f"⚠️ Erro durante o login: {e}")
