import pickle
import os

def save_cookies(driver, path="discord_cookies.pkl"):
    """Salva cookies de sessão."""
    with open(path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)
    print("🍪 Cookies salvos.")

def load_cookies(driver, path="discord_cookies.pkl"):
    """Carrega cookies de sessão se existirem."""
    if os.path.exists(path):
        with open(path, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
        print("🍪 Cookies carregados.")
        return True
    return False
