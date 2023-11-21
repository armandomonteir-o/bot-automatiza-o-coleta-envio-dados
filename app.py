from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Edge()
driver.get('https://www.novaliderinformatica.com.br/computadores')

titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

workbook = openpyxl.Workbook()
workbook.create_sheet('Produtos')
sheet_produtos = workbook['Produtos']
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'
workbook.save('produtos.xlsx')

for titulo, preco in zip (titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])

workbook.save('produtos.xlsx')



