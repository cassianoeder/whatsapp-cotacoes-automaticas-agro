# Automação de Envio de Cotações via WhatsApp

Este script Python automatiza o processo de obtenção de cotações de um site específico e o envio dessas cotações para contatos pré-definidos via WhatsApp.

## Pré-requisitos

Antes de utilizar este script, certifique-se de ter instalado os seguintes pacotes Python:

- requests
- BeautifulSoup (bs4)
- pywhatkit
- pyautogui

Você pode instalá-los utilizando o pip:


Além disso, é necessário ter uma conexão com a internet para fazer as requisições HTTP ao site de cotações e para enviar mensagens pelo WhatsApp.


2. **Configuração:**

- Abra o arquivo `enviar_cotacoes.py` e configure as seguintes variáveis:
  - `url`: URL do site de onde as cotações serão obtidas.
  - `telefones`: Lista de números de telefone para os quais as mensagens serão enviadas.

3. **Execução:**

- Execute o script Python `enviar_cotacoes.py`:

  ```
  python enviar_cotacoes.py
  ```

- O script irá:
  - Fazer uma requisição ao site especificado (`url`).
  - Extrair as cotações disponíveis na página.
  - Formatar uma mensagem com as cotações e a data atual.
  - Enviar a mensagem formatada para cada número de telefone na lista `telefones` via WhatsApp.
  - Fechar a aba do navegador ou janela ativa após cada envio de mensagem.

4. **Observações:**

- Certifique-se de que o WhatsApp Web esteja aberto e conectado antes de executar o script, pois ele utiliza o PyAutoGUI para interagir com a interface do navegador.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma melhoria para sugerir, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.



## Como Usar

1. **Clone o repositório:**

   Clone este repositório para sua máquina local usando o seguinte comando:

