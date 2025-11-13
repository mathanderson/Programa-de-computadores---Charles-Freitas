'''
   Exemplo 01: Programa para contar quantas vogais existem em uma string 
   fornecida pelo usuário.
'''

def contar_vogais(texto):
    """Conta o número de vogais (a, e, i, o, u) em uma string,
    ignorando a diferença entre maiúsculas e minúsculas."""

    # 1. Converte o texto para minúsculas para simplificar a comparação
    texto_minusculo = texto.lower()

    # 2. Define o conjunto de vogais
    vogais = "aeiou"

    # 3. Inicializa o contador
    contador = 0

    # 4. Itera sobre cada caractere do texto
    for caractere in texto_minusculo:
        # 5. Verifica se o caractere é uma vogal
        if caractere in vogais:
            contador += 1 # Incrementa o contador

    return contador

# Solicita a entrada do usuário
entrada = input("Digite uma frase ou palavra: ")

# Chama a função e armazena o resultado
total_vogais = contar_vogais(entrada)

# Exibe o resultado
print(f"A string '{entrada}' possui {total_vogais} vogais.")