import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
import time
import datetime
import pyautogui

# URL do site de cotações
url = 'https://cotricampo.com.br/'

# Obter a data atual
data_atual = datetime.datetime.now()
data = data_atual.strftime("%d/%m/%Y %H:%M:%S")

telefones = ["+55Numeros_envio", "+55Numeros_envio"]

# Faça a requisição ao site
response = requests.get(url)

# Verifique se a requisição foi bem-sucedida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar a div com o ID 'home_cotacoes'
    div_cotacoes = soup.find('div', id='home_cotacoes')
    
    if div_cotacoes:

        agricolas = div_cotacoes.find_all('div', class_='card_cotacao')

        mensagem = f"Cotações do dia: {data}\nRetiradas automaticamente do site {url}\n\n"

        for item in agricolas:
            titulo = item.find('div', class_='card_coluna_1').text.strip()
            preco = item.find('div', class_='card_coluna_2').text.strip()
            print(f"{titulo}: {preco}")
            mensagem += f"{titulo}: {preco}\n"
            time.sleep(1)

    for indice, telefone in enumerate(telefones):

        hora = datetime.datetime.now().hour
        minuto = datetime.datetime.now().minute +1
        if minuto == 60:
            minuto -= 60

        kit.sendwhatmsg(telefone, mensagem, hora, minuto, close_time=2)
        time.sleep(10)  # Aguarda 5 segundos (ajuste conforme necessário)
        pyautogui.hotkey('ctrl', 'w')

