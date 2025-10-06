#    Você deve criar um programa que calcule o quociente entre dois números inteiros 
# 	fornecidos pelo usuário. Durante o processo, é necessário tratar as seguintes exceções:

# 		- Caso o segundo número seja zero, o programa deve exibir uma mensagem 
# 		   informando que a divisão por zero não é permitida.

# 		- Caso o usuário insira um valor que não seja um número inteiro, o programa deve 
# 		  exibir uma mensagem solicitando que o usuário insira apenas números inteiros.

# 	Instruções:

# 		- Solicite ao usuário para inserir o primeiro número inteiro.

# 		- Solicite ao usuário para inserir o segundo número inteiro.

# 		- Calcule o quociente entre os dois números, tratando as exceções descritas acima.

import sys

try:
   intDividendo = int(input('Informe o Dividendo: '))
   intDivisor = int(input('Informe o Divisor..: '))
   quociente = intDividendo / intDivisor

except ZeroDivisionError:
   sys.exit('ERRO: Divisão por Zero não é permitida...')

except ValueError:
   sys.exit('ERRO: Informe apenas números inteiros...')

except Exception as strErro:
   sys.exit(f'EXCEÇÃO: {sys.exc_info()[0]} -> {strErro}')

else:
   print(f'{intDividendo} / {intDivisor} = {quociente:.2f}')
 
   # criar um programa que permita ao usuário calcular a raiz quadrada de um 
   # número inteiro. Entretanto, o programa deve cumprir os seguintes requisitos:

   # - Se o usuário inserir um número negativo, o programa deve lançar uma 
   #   exceção personalizada chamada "FloatingPointError" com uma mensagem
   #   apropriada;

   # - Se o usuário inserir um valor que não seja um número inteiro, o programa
   #   deve capturar a exceção "ValueError" e exibir uma mensagem informando
   #   que o valor inserido é inválido;

   # - Caso  o número for positivo ou zero, o programa deve calcular e exibir a 
   #   raiz quadrada do número com duas casas decimais.

   # Instruções:
   #    - Solicite ao usuário para inserir um número inteiro.

   #    - Implemente o tratamento de exceções conforme os requisitos acima.
      
   #    - Calcule e exiba a raiz quadrada do número, se aplicável.

try:
   intValor = int(input('Informe um valor inteiro: '))

   if intValor < 0:
      raise FloatingPointError

   fltRaizQuadrada = intValor ** 0.5

except FloatingPointError:
   sys.exit('ERRO: Não há Raiz Real para números negativos...')

except ValueError:
   sys.exit('ERRO: Informe apenas números inteiros...')

else:
   print(f'A raiz quadrada de {intValor} é {raizQuadrada:.2f}')
