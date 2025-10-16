import math

# Função para calcular o ângulo usando a lei dos cossenos
def calcula_angulo(a, b, c):
    # a, b são lados adjacentes, c é o lado oposto ao ângulo que queremos
    # fórmula: cos(theta) = (a² + b² - c²) / (2ab)
    cos_theta = (a**2 + b**2 - c**2) / (2 * a * b)
    # arccos para encontrar o ângulo em radianos, depois converte para graus
    angulo = math.degrees(math.acos(cos_theta))
    return angulo

# Recebendo os lados do triângulo
lado1 = float(input("Digite o comprimento do lado 1: "))
lado2 = float(input("Digite o comprimento do lado 2: "))
lado3 = float(input("Digite o comprimento do lado 3: "))

# Verificando se os lados formam um triângulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Calculando os ângulos
    anguloA = calcula_angulo(lado2, lado3, lado1)
    anguloB = calcula_angulo(lado1, lado3, lado2)
    anguloC = calcula_angulo(lado1, lado2, lado3)

    # Classificação quanto aos lados
    if lado1 == lado2 == lado3:
        tipo_lados = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo_lados = "Isósceles"
    else:
        tipo_lados = "Escaleno"

    # Classificação quanto aos ângulos
    if any(abs(angulo - 90) < 1e-5 for angulo in [anguloA, anguloB, anguloC]):  # verifica se algum ângulo é 90
        tipo_angulos = "Retângulo"
    elif any(angulo > 90 for angulo in [anguloA, anguloB, anguloC]):
        tipo_angulos = "Obtuso"
    else:
        tipo_angulos = "Agudo"

    # Mostrando resultados
    print(f"\nOs ângulos do triângulo são: {anguloA:.2f}°, {anguloB:.2f}°, {anguloC:.2f}°")
    print(f"Classificação quanto aos lados: {tipo_lados}")
    print(f"Classificação quanto aos ângulos: {tipo_angulos}")

else:
    print("Não é possível formar um triângulo com esses lados.")
