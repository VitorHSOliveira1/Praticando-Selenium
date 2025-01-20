from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Objetivo: Registrar conta, lgoar na conta, adicionar 3 itens especificos no carrinho e fazer o checkout com suscesso

navegador = webdriver.Chrome()

navegador.get("https://www.demoblaze.com/index.html")
navegador.maximize_window()

botao_registrar = navegador.find_element(By.XPATH ,"//*[@id='signin2']")
botao_logar = navegador.find_element(By.XPATH ,"//*[@id='login2']")
botao_add_cart = navegador.find_element(By.CLASS_NAME ,"btn btn-success btn-lg")
botao_home = navegador.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]/a")
botao_registrar = navegador.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
botao_login = navegador.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
botao_carrinho = navegador.find_element(By.XPATH, "//*[@id='cartur']")
botao_checkout = navegador.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
input_username_registrar = navegador.find_element(By.XPATH ,"//*[@id='sign-username']")
input_username_login = navegador.find_element(By.XPATH, "//*[@id='loginusername']")
input_password_registrar = navegador.find_element(By.XPATH ,"//*[@id='sign-password']]")
input_password_login = navegador.find_element(By.XPATH ,"//*[@id='loginpassword']")
input_cart_name = navegador.find_element(By.XPATH ,"//*[@id='name']")
input_cart_country = navegador.find_element(By.XPATH ,"//*[@id='country']")
input_cart_city = navegador.find_element(By.XPATH ,"//*[@id='city']")
input_cart_creditcard = navegador.find_element(By.XPATH ,"//*[@id='card']")
input_cart_month = navegador.find_element(By.XPATH ,"//*[@id='month']")
input_cart_year = navegador.find_element(By.XPATH ,"//*[@id='year']")
item1 = navegador.find_element(By.XPATH ,"//*[@id='tbodyid']/div[1]/div/div/h4/a")
item2 = navegador.find_element(By.XPATH ,"//*[@id='tbodyid']/div[4]/div/div/h4/a")
item3 = navegador.find_element(By.XPATH ,"//*[@id='tbodyid']/div[3]/div/div/h4/a")
preco_atual_string = navegador.find_element(By.XPATH, "//*[@id='totalp']").text
preco_autal = preco_atual_string = int(preco_atual_string)




def registar_e_logar():
    botao_registrar.click()
    time.sleep(3)
    input_username_registrar.send_keys("vitorhsoliveira13@gmail.com")
    input_password_registrar.send_keys("clarice123")
    time.sleep(3)
    botao_login.click()
    time.sleep(3)
    input_username_login.send_keys("vitorhsoliveira13@gmail.com")
    input_password_login.send_keys("123456")
    botao_login.click()
    

def adiciona_carrinho_e_volta ():
    botao_add_cart.click()
    botao_home.click()
    
    
def adicionar_itens():
    item1.click()
    adiciona_carrinho_e_volta()

    navegador.execute_script("arguments[0].scrollIntoView();", item2)
    item2.click()
    adiciona_carrinho_e_volta()

    item3.click()
    adiciona_carrinho_e_volta()

def abrir_carrinho():
    botao_carrinho.click()
    time.sleep(3)

def responder_formulario():
    botao_checkout.click()
    time.sleep(3)
    input_cart_name.send_keys("Vitor Hugo Silva de Oliveira")
    input_cart_country.send_keys("Brazil")
    input_cart_city.send_keys("Destrito Federal")
    input_cart_creditcard.send_keys("XXXXXXXXXXXXXXXX")
    input_cart_month.send_keys("9")
    input_cart_year.send_keys("2001")
    
def verificar_preco_certo():
    preco_certo = 1810
    if preco_certo != preco_autal:
        navegador.execute_script("alert('Erro encontrado na precificação');")
    else:
        pass

registar_e_logar()
time.sleep(5)
adicionar_itens()
time.sleep(5)
abrir_carrinho()
verificar_preco_certo()
responder_formulario()
time.sleep(10)
