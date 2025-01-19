from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Objetivo: Listar os itens existentes no site por preco.

navegador = webdriver.Chrome()

navegador.get("https://www.demoblaze.com/index.html")
navegador.maximize_window()

produto_cru = navegador.find_elements(By.XPATH ,"//*[@id='tbodyid']/div[1]")
nomes_produtos_cru = navegador.find_elements(By.CLASS_NAME ,"hrefch")
preco_produtos_cru = navegador.find_elements(By.TAG_NAME ,"h5")
next_button = navegador.find_elements(By.XPATH, "//*[@id='next2']")
produtos = []

def puxar_produtos_pra_cima():
    navegador.execute_script("arguments[0].scrollIntoView();", produto_cru)

def transformar_produtos_em_objeto():
    for nome_produto, preco_produto in zip(nomes_produtos_cru, preco_produtos_cru):
        nome = nome_produto.txt
        preco = preco_produto.text.replace("R$", "").strip()
        preco = int(preco)
        
        produtos.append({"nome": nome, "preco": preco})
        

puxar_produtos_pra_cima()
transformar_produtos_em_objeto()
time.sleep(3)
next_button.click()
time.sleep(3)
puxar_produtos_pra_cima()
transformar_produtos_em_objeto()

lista_em_ordem_crescente = sorted(produtos, key=lambda item: item["preco"])
navegador.execute_script("console.log(lista_em_ordem_crescente)")
print(lista_em_ordem_crescente)