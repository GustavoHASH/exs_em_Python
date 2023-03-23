#Aula002 - INPUT/OUTPUT - Exercício 1 - Calcular IMC

#input da massa e altura em valores reais
massa = float(input("Digite a sua massa corporal em kg: "))
print(50 * ("*"))
altura = float(input("Digite a sua altura em metros: "))

#fórmula de cálculo do imc
imc = massa / (altura**2)
print(50 * ("*"))
#print usando round para delimitar a quantidade de casas decimais para 2
print("Seu IMC é:", round(imc, 2))
