#Automação de um programa para BUSCAR A COTAÇÃO: JAQUETAS MOTO


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#Colocar dentro do parenteses o "caminho" do executavel "chromedriver.exe"
driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin\chromedriver.exe")

#Maximiza tela
driver.maximize_window()



#__________________________________________________X11 GUARD 2_______________________________________________________________________
#X11 GUARD 2
driver.get("https://www.google.com.br/")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("jaqueta x11 guard 2 masculina vermelha tamanho g")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#click em shopping
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()


#Seleciona valor e imprime

primeiro_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
primeira_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
primeira_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/span/a/div[1]/h4').text

segundo_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]').text
segunda_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
segunda_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/span/a/div[1]/h4').text

terceiro_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
terceira_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
terceira_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/span/a/div[1]/h4').text

quarto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
quarta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
quarta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/span/a/div[1]/h4').text

quinto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
quinta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
quinta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/span/a/div/h4').text

sexto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
sexta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
sexta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/span/a/div[1]/h4').text

setimo_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
setima_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
setima_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/span/a/div/h4').text

print("")
print('Pesquisa: JAQUETA X11 GUARD 2')
print(primeiro_preco,'/ ', primeira_loja,'/ ', primeira_descricao)
print(segundo_preco,'/ ', segunda_loja,'/ ', segunda_descricao)
print(terceiro_preco,'/ ', terceira_loja,'/ ', terceira_descricao)
print(quarto_preco,'/ ', quarta_loja,'/ ', quarta_descricao)
print(quinto_preco,'/ ', quinta_loja,'/ ', quinta_descricao)
print(sexto_preco,'/ ', sexta_loja,'/ ', sexta_descricao)
print(setimo_preco,'/ ', setima_loja,'/ ', setima_descricao)
print('______________________________________________________________________________________________________________________')


#__________________________________________________TEXX RONIN_______________________________________________________________________
#TEXX RONIN
driver.get("https://www.google.com.br/")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("jaqueta texx ronin tamanho g")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#click em shopping
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()


pesquisa2_primeiro_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
pesquisa2_primeira_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_primeira_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/span/a/div[1]/h4').text

pesquisa2_segundo_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]').text
pesquisa2_segunda_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_segunda_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/span/a/div[1]/h4').text

pesquisa2_terceiro_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
pesquisa2_terceira_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_terceira_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/span/a/div[1]/h4').text

pesquisa2_quarto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
pesquisa2_quarta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_quarta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/span/a/div[1]/h4').text

pesquisa2_quinto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
pesquisa2_quinta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_quinta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/span/a/div/h4').text

pesquisa2_sexto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
pesquisa2_sexta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_sexta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/span/a/div[1]/h4').text

pesquisa2_setimo_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
pesquisa2_setima_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
pesquisa2_setima_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/span/a/div/h4').text

print("")
print('Pesquisa: JAQUETA TEXX RONIN')
print(pesquisa2_primeiro_preco,'/ ', pesquisa2_primeira_loja,'/ ', pesquisa2_primeira_descricao)
print(pesquisa2_segundo_preco,'/ ', pesquisa2_segunda_loja,'/ ', pesquisa2_segunda_descricao)
print(pesquisa2_terceiro_preco,'/ ', pesquisa2_terceira_loja,'/ ', pesquisa2_terceira_descricao)
print(pesquisa2_quarto_preco,'/ ', pesquisa2_quarta_loja,'/ ', pesquisa2_quarta_descricao)
print(pesquisa2_quinto_preco,'/ ', pesquisa2_quinta_loja,'/ ', pesquisa2_quinta_descricao)
print(pesquisa2_sexto_preco,'/ ', pesquisa2_sexta_loja,'/ ', pesquisa2_sexta_descricao)
print(pesquisa2_setimo_preco,'/ ', pesquisa2_setima_loja,'/ ', pesquisa2_setima_descricao)
print('______________________________________________________________________________________________________________________')



#__________________________________________________HELT STROKE_______________________________________________________________________
#HELT STROKE
driver.get("https://www.google.com.br/")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("jaqueta helt stroke tamanho g")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#click em shopping
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a').click()


helt_primeiro_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
helt_primeira_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_primeira_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[1]/div[1]/div[2]/span/a/div[1]/h4').text

helt_segundo_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]').text
helt_segunda_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_segunda_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/span/a/div[1]/h4').text

helt_terceiro_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
helt_terceira_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_terceira_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[3]/div[1]/div[2]/span/a/div[1]/h4').text

helt_quarto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
helt_quarta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_quarta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[4]/div[1]/div[2]/span/a/div[1]/h4').text

helt_quinto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
helt_quinta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_quinta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[5]/div[1]/div[2]/span/a/div/h4').text

helt_sexto_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
helt_sexta_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_sexta_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[6]/div[1]/div[2]/span/a/div[1]/h4').text

helt_setimo_preco = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[2]/span/span/span[1]/span').text
helt_setima_loja = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/div[2]/span/div[1]/a[1]/div[3]').text
helt_setima_descricao = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div/div[7]/div[1]/div[2]/span/a/div/h4').text

print("")
print('Pesquisa: JAQUETA HELT STROKE')
print(helt_primeiro_preco,'/ ', helt_primeira_loja,'/ ', helt_primeira_descricao)
print(helt_segundo_preco,'/ ', helt_segunda_loja,'/ ', helt_segunda_descricao)
print(helt_terceiro_preco,'/ ', helt_terceira_loja,'/ ', helt_terceira_descricao)
print(helt_quarto_preco,'/ ', helt_quarta_loja,'/ ', helt_quarta_descricao)
print(helt_quinto_preco,'/ ', helt_quinta_loja,'/ ', helt_quinta_descricao)
print(helt_sexto_preco,'/ ', helt_sexta_loja,'/ ', helt_sexta_descricao)
print(helt_setimo_preco,'/ ', helt_setima_loja,'/ ', helt_setima_descricao)
print('_______________________________________________________________________________________________________________________')




driver.close()


