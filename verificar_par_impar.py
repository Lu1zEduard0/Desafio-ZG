def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Lê um valor do usuário
valor = int(input("Digite um número: "))

# Chama a função para verificar se é par ou ímpar
resultado = verificar_par_impar(valor)

# Mostra o resultado
print(f"O número {valor} é {resultado}.")