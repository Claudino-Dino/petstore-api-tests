from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CarrinhoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def adicionar_produtos(self):
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn_inventory")))
        botoes = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        if len(botoes) > 1:
            for botao in botoes:
                self.wait.until(EC.element_to_be_clickable(botao))
                botao.click()
            print("""
-----------------------------------
    PRODUTOS ADICIONADOS ✅
-----------------------------------
                """)

    def finalizar_compra(self, nome, sobrenome, codigo_postal):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='checkout']"))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='first-name']"))).send_keys(nome)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='last-name']"))).send_keys(sobrenome)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='postal-code']"))).send_keys(codigo_postal)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='continue']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='finish']"))).click()
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/checkout-complete.html"))
        url_compra_finalizada = "https://www.saucedemo.com/checkout-complete.html"
        if self.driver.current_url == url_compra_finalizada:
            print("""
-----------------------------------
    COMPRA FINALIZADA ✅
-----------------------------------
                """)
