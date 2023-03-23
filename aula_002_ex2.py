#Aula 002  - INPUT/OUTPUT -  Exercício 2 - Converter m/s para km/h

#input do valor a ser convertido
metros = float(input("digite o valor em m/s a ser convertido em km/h: "))
print(50 * ("*"))
#conversão de m/s por km/h
km_hora = metros * 3.6

#print do resultado da conversão
print("o valor da conversão de m/s por kh/h é: ", round(km_hora, 2), "km/h")
