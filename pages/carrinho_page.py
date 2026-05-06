from selenium.webdriver.common.by import By

class CarrinhoPage:

    def __init__(self, driver):
        self.driver = driver

    def adicionar_produtos(self):
        botoes = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")

        if len(botoes) > 1 :
            for botao in botoes:
                botao.click()
            print("""
-----------------------------------
    PRODUTOS ADICIONADOS ✅
-----------------------------------
                """)

    def finalizar_compra(self, nome, sobrenome, codigo_postal):
        self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
        self.driver.find_element(By.XPATH, "//*[@id='checkout']").click()

        self.driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys(nome)
        self.driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys(sobrenome)
        self.driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys(codigo_postal)

        self.driver.find_element(By.XPATH, "//*[@id='continue']").click()

        self.driver.find_element(By.XPATH, "//*[@id='finish']").click()

        url_compra_finalizada = "https://www.saucedemo.com/checkout-complete.html"

        if (self.driver.current_url==url_compra_finalizada):
            print("""
-----------------------------------
    COMPRA FINALIZADA ✅
-----------------------------------
                """)