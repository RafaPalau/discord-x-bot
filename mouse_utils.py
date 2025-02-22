import random
import time
from selenium.webdriver.common.action_chains import ActionChains

def human_like_mouse_move(driver):
    """Simula movimentações humanas do mouse sem sair da tela visível."""
    action = ActionChains(driver)
    window_size = driver.get_window_size()
    width = window_size["width"]
    height = window_size["height"]

    for _ in range(random.randint(3, 7)):
        x_offset = random.randint(0, width // 2)  # Limita ao meio da tela
        y_offset = random.randint(0, height // 2)
        try:
            action.move_by_offset(x_offset, y_offset).perform()
            time.sleep(random.uniform(0.3, 0.8))
        except Exception as e:
            print(f"⚠️ Erro ao mover o mouse: {e}")
            continue  # Continua mesmo se houver erro em um movimento
