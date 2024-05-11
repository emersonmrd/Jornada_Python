# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # Link do sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Para instalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab)


# Abrir o navegador (Opera)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(3)
# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=1134, y=353)
pyautogui.write("testepython@gmail.com")

pyautogui.press("tab") # passou para o campo de senha
pyautogui.write("Sua senha aqui")

pyautogui.press("tab") # passou para o botão de logar
pyautogui.press("enter")

time.sleep(3) # sleep para garantir que o site carregou

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar um produto
# str = string = texto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"]) # -> string
    # clicar no campo do codigo do produto
    pyautogui.click(x=828, y=239)
    #preencher o codigo
    pyautogui.write(codigo)
    # passar pro proximo campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # passar pro proximo campo
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    # passar pro proximo campo
    pyautogui.press("tab")
    #apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# 5. Repetir isso tudo até acabar a lista de produtos

