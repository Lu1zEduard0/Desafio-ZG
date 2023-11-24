# Desafio-ZG
 Acelera ZG 5.0 - 2023
**Desafio de Requisição HTTP para o Endereço** "https://tranquil-rex-405218.rj.r.appspot.com/hashCodeServer"

###Objetivo:
Realizar uma requisição HTTP do tipo POST para o endereço fornecido, contendo os parâmetros "nome," "email," e "cpf." Receber uma mensagem de sucesso com um código hash, uma pergunta, e fornecer código, pergunta e resposta.

**Endereço da Requisição:**
`https://tranquil-rex-405218.rj.r.appspot.com/hashCodeServer?nome=Exemplo&email=XXX@gmail.com&cpf=XXX.XXX.XXX-XX`

**Resposta Recebida:**

`{"hashCode":"04cc1c1f40ba64e8514675718121818e855a846a","status":200,"mensagem":"Hash code já existente, referente ao cpf: XXX.XXX.XXX-XX ou ao e-mail: email@gmail.com","pergunta":"P3 - Escreva um Algoritmo (sequência de passos) que leia um valor e identifique se é par ou ímpar."}`

**Estratégia Utilizada:**

1. Definição da URL e Parâmetros: Determinei a URL do serviço e os parâmetros necessários para a requisição (nome, e-mail e CPF).
2. Construção da Requisição: Utilizei a função requests.post() para enviar uma requisição do tipo POST para a URL, incluindo os parâmetros no corpo da solicitação.
3. Manipulação da Resposta: Examinei o código de status da resposta para verificar se a requisição foi bem-sucedida. Em caso de sucesso, analisei o conteúdo da resposta, que geralmente estava no formato JSON.
4. Tratamento do JSON: Utilizei a biblioteca json para analisar o conteúdo JSON da resposta. Extraí informações relevantes, como o código hash, a pergunta e a mensagem.
5. Exibição dos Resultados: Exibi os resultados na saída padrão, incluindo o código de status, o conteúdo completo da resposta e, se disponível, o código hash, a pergunta e a mensagem.

**Dificuldades Encontradas:**

Durante o teste, o código hash já existia, referente ao CPF ou e-mail fornecidos. Isso gerou uma mensagem indicando que o hash code já existia.

##Código Desenvolvido:

```python
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
```

####Resultado Inserido no README:
Insira abaixo o código hash que recebeu após realizar a requisição HTTP.

`04cc1c1f40ba64e8514675718121818e855a846a`

Qual foi a pergunta que você recebeu junto ao hashcode?

P3 - Escreva um Algoritmo (sequência de passos) que leia um valor e identifique se é par ou ímpar.

Compartilhe conosco qual foi sua estratégia para resolver ao desafio.

Minha estratégia envolveu a definição clara dos parâmetros, a construção da requisição HTTP, a manipulação cuidadosa da resposta JSON e a exibição adequada dos resultados. Lidei com mensagens de erro e exceções para garantir um fluxo suave mesmo em condições inesperadas.

