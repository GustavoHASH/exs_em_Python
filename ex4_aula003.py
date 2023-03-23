# Exercício 4   - aula003 - Ler dois números inteiros e informar:
# Se o  primeiro é divisível pelo segundo

# Leia os dois números inteiros
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo número: "))

# Verifica se o primeiro número é divisível pelo segundo
if num1 % num2 == 0:
      print(num1, "é divisível por", num2)
else:
      print(num1, "não é divisível por", num2)