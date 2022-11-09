# Coloque aqui o código do teu cliente em Python

#Passo 1:
# Buscar de uma fila de pedidos de empréstimo
# Fila está disponível por GET em:
#https://us-central1-emf-teacher.cloudfunctions.net/function-aulas-getclient
#Parâmetro qtde permite buscar mais de um cliente da fila
# Exibir em tela os clientes da fila


#Passo 2:
# Chamar o teu micro serviço cognitivo
# Exibir em tela a resposta do teu serviço de crédito



# Extra: Opcional
# Gravar em arquivo CSV sequencial

import requests
import pandas as pd

if __name__ == "__main__":
    # Prepara chamada
    url = "http://localhost:8080/modelo02"
    headers = {'Content-Type': 'application/json'}
    conteudo = requests.request("GET", 'https://us-central1-emf-teacher.cloudfunctions.net/function-aulas-getclient?qtde=8', headers=headers)

    #Chama API
    response = requests.request("POST", url, headers=headers, data=conteudo)
    print("Resposta da API de Regressão:")
    print(response.text.encode('utf8').decode())

    pass

