'''
   Exemplo 02: Programa para contar quantas palavras existem em uma frase
   fornecida pelo usuário.
'''

def contar_palavras(frase):
    """Conta o número de palavras em uma frase usando o método split()."""

    # 1. Remove espaços extras no início e fim da frase (se houver)
    frase_limpa = frase.strip()

    # Verifica se a frase não está vazia após a limpeza
    if not frase_limpa:
        return 0

    # 2. Divide a frase em uma lista de palavras.
    # Por padrão, split() usa espaços (e múltiplas ocorrências deles) como delimitador.
    lista_de_palavras = frase_limpa.split()

    # 3. O número de palavras é o tamanho da lista
    return len(lista_de_palavras)

# Solicita a entrada do usuário
entrada = input("Digite uma frase: ")

# Chama a função e armazena o resultado
total_palavras = contar_palavras(entrada)

# Exibe o resultado
print(f"A frase '{entrada}' possui {total_palavras} palavras.")