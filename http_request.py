# Importa a biblioteca requests, que facilita a realização de solicitações HTTP em Python
import requests

# Define a URL do endpoint para fazer a solicitação HTTP
url = "https://tranquil-rex-405218.rj.r.appspot.com/hashCodeServer"

# Define os dados a serem enviados na solicitação POST
params = {
    'nome': 'Luiz Eduardo Pereira de Lima',
    'email': 'email@gmail.com',
    'cpf': '111.111.111-00' 
}

# Envia os dados diretamente na URL como parâmetros
response = requests.post(url, params=params)

print(f'Código de status: {response.status_code}')
print(f'Resposta completa: {response.text}')

# Verifica se a resposta HTTP foi bem-sucedida (código 200)
if response.status_code == 200:
    try:
        # Converte a resposta JSON para um dicionário Python
        json_response = response.json()
        
        # Extrai o código hash e a pergunta do dicionário
        codigo_hash = json_response['codigo']
        pergunta = json_response['pergunta']
        
        # Exibe ou utiliza o código hash e a pergunta conforme necessário
        print(f'Código Hash: {codigo_hash}')
        print(f'Pergunta: {pergunta}')

    except KeyError as e:
        # Se uma chave estiver ausente, imprime uma mensagem de erro
        print(f'Erro: Chave ausente no dicionário JSON - {e}')
else:
    # Em caso de erro na solicitação, exibe o código de status da resposta
    print(f'Erro na requisição. Código de status: {response.status_code}')
