'''
   Desenvolva um programa que calcula o IMC de uma pessoa. 
   
   O programa deve pedir o peso em quilogramas (ex: 70.5) e a 
   altura em metros (ex: 1.75). 
   
   A fórmula do IMC é: peso / (altura * altura). 
   
   Após calcular o IMC, o programa deve exibir o valor e a 
   classificação correspondente, de acordo com a tabela:

      - Abaixo de 18.5: Abaixo do peso
      - 18.5 a 24.9: Peso ideal
      - 25.0 a 29.9: Sobrepeso
      - 30.0 a 34.9: Obesidade Grau I
      - Acima de 35.0: Obesidade Grau II

   O programa deve tratar entradas inválidas (não numéricas) e 
   também verificar se a altura informada é maior que zero para evitar 
   um erro de divisão.      
'''
try:
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    if altura <= 0:
        print("Erro: a altura deve ser maior que zero.")
    else:
        imc = peso / (altura * altura)
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif imc < 25:
            print("Classificação: Peso ideal")
        elif imc < 30:
            print("Classificação: Sobrepeso")
        elif imc < 35:
            print("Classificação: Obesidade Grau I")
        else:
            print("Classificação: Obesidade Grau II")

except ValueError:
    print("Erro: por favor, digite apenas números válidos.")


    

    