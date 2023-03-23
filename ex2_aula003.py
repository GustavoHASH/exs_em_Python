# Exercício 2 - aula003 - ler o
# comprimento dos 3 lados de um triângulo e
# indicar a sua classificação com base na igualdade entre os lados

# Leia o comprimento dos 3 lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se o triângulo é equilátero
if lado1 == lado2 == lado3:
  print("Triângulo Equilátero(3 lados iguais)")
# Se não for equilátero, verifique se o triângulo é isósceles
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
  print("Triângulo Isósceles(2 lados iguais)")
# Se não for equilátero ou isósceles, o triângulo é escaleno
else:
  print("Triângulo Escaleno(3 lados diferentes)")
