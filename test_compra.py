from selenium import webdriver
from pages.login_page import LoginPage
from pages.carrinho_page import CarrinhoPage
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from time import sleep
import os

def carregar_driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    return driver

def comprar_produtos(): 
    load_dotenv()
    user = os.getenv("USUARIO")
    senha = os.getenv("SENHA")
    nome = os.getenv("NOME")
    sobrenome = os.getenv("SOBRENOME")
    codigo_postal = os.getenv("CODIGO_POSTAL")

    driver = carregar_driver()
    driver.get("https://www.saucedemo.com/")

    loginObj = LoginPage(driver)
    carrinhoObj = CarrinhoPage(driver)

    loginObj.fazer_login(user, senha)
    carrinhoObj.adicionar_produtos()
    carrinhoObj.finalizar_compra(nome,sobrenome,codigo_postal)

if __name__ == "__main__":
    comprar_produtos()