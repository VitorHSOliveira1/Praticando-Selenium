from selenium import webdriver
import time

navegador = webdriver.Chrome()

navegador.get("https://google.com")
navegador.maximize_window()
botao_verde = navegador.find_element("" ,"gNO89b")
botao_verde.click()
time.sleep(10)