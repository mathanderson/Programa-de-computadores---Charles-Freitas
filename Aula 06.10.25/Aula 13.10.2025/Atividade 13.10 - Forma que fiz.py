'''
   Crie um programa que calcula o salário semanal de um funcionário.
   
   O programa deve solicitar o número de horas trabalhadas na semana e o 
   valor que ele recebe por hora. A jornada de trabalho padrão é de 40 horas 
   semanais. Horas trabalhadas acima de 40 devem ser pagas com um adicional 
   de 50% (o valor da hora extra é 1.5 vezes o valor da hora normal). 
   
   O programa deve exibir o salário total. 
   
   Garanta que o programa trate o caso de o usuário digitar valores não 
   numéricos.
'''
try:
    horas = float(input('Horas trabalhadas na semana'))
    valor_hora = float(input('Valor recebido por hora'))

    if horas <= 40:
        salario = horas *valor_hora
    
    else:
        extras = horas - 40
        salario = (40*valor_hora) + (extras * valor_hora * 40)

        print (f'salario total da semana: R$ (salario:2f')

except ValueError:

    print ('Erro: digite apenas números válidos')
