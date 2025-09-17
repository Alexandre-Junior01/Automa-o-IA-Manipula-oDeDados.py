
import pyautogui 
import time

pyautogui.PAUSE= 0.5 


# abrir  o navegador chrome
pyautogui.press("win")
pyautogui.write("chrom")
pyautogui.press("ent")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("ent")

# o site pode  demorar para carregar
time.sleep(2) # apenas nesse lugar eu quero que espere


# 2. Fazer login
# preciso usar o comando pyoutogui.posicion,para pegar a posição da barra e clicar no campo email.
pyautogui.click(x=815, y=365)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste 256")
pyautogui.press("tab")
pyautogui.press("ent")

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
    pyautogui.press("ent") # cadastra o produto (botao enviar)
    pyautogui.scroll(5000) # preciso usar o comando pyoutogui.scroll para voltar para inicio tela
     # Passo 5: Repetir o processo de cadastro até o fim
   




# 5- repetir isso tudo ate acabar a lista de produtos
