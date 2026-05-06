from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def fazer_login(self, email, senha):
        self.driver.find_element(By.XPATH,"//*[@id='user-name']").send_keys(email)
        self.driver.find_element(By.XPATH,"//*[@id='password']").send_keys(senha)
        self.driver.find_element(By.XPATH   ,"//*[@id='login-button']").click()

        url_carrinho_page = "https://www.saucedemo.com/inventory.html"

        if (self.driver.current_url==url_carrinho_page):
            print("""
-----------------------------------
    LOGIN EFETUADO ✅
-----------------------------------
                """)

