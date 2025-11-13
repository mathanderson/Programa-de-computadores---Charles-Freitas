
strFrase= input('Digite uma frase:').strip()
intContador = 0
for letra in strFrase:
    if letra == ' ':
        intContador +=1
print (f'Quantidade de Palavras = {intContador+1}')
