from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fazer_login(self, email, senha):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']"))).send_keys(email)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']"))).send_keys(senha)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-button']"))).click()
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
        url_carrinho_page = "https://www.saucedemo.com/inventory.html"
        if self.driver.current_url == url_carrinho_page:
            print("""
-----------------------------------
    LOGIN EFETUADO ✅
-----------------------------------
                """)
