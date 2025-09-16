# Passo a passo do projeto

# 1- abrir o sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pyautogui,biblioteca de automização, permite automatizar teclado,mouse,monitor e etc.
#Para instalar pip install pyautogui
import pyautogui # type: ignore
import time

pyautogui.PAUSE= 0.5 # uma pausa de 0.5 segundos a cada comando do pyautogui,
                     # e garante que um comando não vai atropelar o outro.

#pyautogui.click # clicar com o botão do mouse  (clicks= 2) (button= "left", ou rigth, ou middle)
#pyautogui.write # escrever um textp
#pyautogui.press # pressionar uma tecla do teclado, enter, tab, esc...
#pyautogui.hotkey # apertar um conjunto de teclas
#pyoutogui.posicion #  captura a posição do mouse

# abrir  o navegador chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# o site pode  demorar para carregar
time.sleep(2) # apenas nesse lugar eu quero que espere


# 2. Fazer login
# preciso usar o comando pyoutogui.posicion,para pegar a posição da barra e clicar no campo email.
pyautogui.click(x=815, y=365)
pyautogui.write("testealgumacoisa@gmail.com")
pyautogui.press("tab")
pyautogui.write("qualquer coisa 123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2) # garantir que o site carregue

# 3- abrir/importar a base de dados de produtos para cadastrar
#  pandas, biblioteca feita para trabalhar com base de dados, pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv("produtos.csv") # read, ler, ler a tabela produtos.csv

print(tabela)


# 4- cadastrar os produtos
for linha in tabela.index: # se eu quiser pegar a lista com todas colunas,tabela.columns,e linhas usa index
    codigo = str (tabela.loc[linha, "codigo"])
    pyautogui.click(x=532, y=257)   # clicar no campo de código
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    pyautogui.scroll(5000) # preciso usar o comando pyoutogui.scroll para voltar para inicio tela
     # Passo 5: Repetir o processo de cadastro até o fim
   




# 5- repetir isso tudo ate acabar a lista de produtos
