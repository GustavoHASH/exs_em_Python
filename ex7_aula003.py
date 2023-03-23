# Exercício 7   - aula003 - Converter temperatura em Celsius

# Funções de conversão de temperatura
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 1.8

def celsius_to_reaumur(celsius):
    return celsius * 0.8

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

def fahrenheit_to_reaumur(fahrenheit):
    return (fahrenheit - 32) * 0.44444

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9 / 5 - 459.67

def kelvin_to_rankine(kelvin):
    return kelvin * 1.8

def kelvin_to_reaumur(kelvin):
    return (kelvin - 273.15) * 0.8

def rankine_to_celsius(rankine):
    return (rankine - 491.67) * 5 / 9

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

def rankine_to_kelvin(rankine):
    return rankine * 5 / 9

def rankine_to_reaumur(rankine):
    return (rankine - 491.67) * 4 / 9

def reaumur_to_celsius(reaumur):
    return reaumur * 1.25

def reaumur_to_fahrenheit(reaumur):
    return reaumur * 2.25 + 32

def reaumur_to_kelvin(reaumur):
    return reaumur * 1.25 + 273.15

def reaumur_to_rankine(reaumur):
    return (reaumur + 218.52) * 2.25

# Menu de Entrada e Saída de Escalas de Temperatura
while True:
    print("Selecione a escala de entrada e saída:")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    print("4 - Rankine")
    print("5 - Réaumur")
    print("0 - Sair")

    opcao_entrada = int(input("Opção de entrada: "))

    if opcao_entrada == 0:
        break
      
    # Temperatura de Entrada
    temperatura_entrada = float(input("Digite a temperatura: "))
  
   
    if opcao_entrada == 1:
        celsius = temperatura_entrada
    elif opcao_entrada == 2:
        celsius = fahrenheit_to_celsius(temperatura_entrada)
    elif opcao_entrada == 3:
        celsius = kelvin_to_celsius(temperatura_entrada)
    elif opcao_entrada == 4:
        celsius = rankine_to_celsius(temperatura_entrada)
    elif opcao_entrada == 5:
        celsius = reaumur_to_celsius(temperatura_entrada)

    print("Selecione a escala de saída:")
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    print("4 - Rankine")
    print("5 - Réaumur")

  # Temperatura de Saída
    opcao_saida = int(input("Opção de saída: "))
    
    if opcao_saida == 1:
        temperatura_saida = celsius
    elif opcao_saida == 2:
        temperatura_saida = celsius_to_fahrenheit(celsius)
    elif opcao_saida == 3:
        temperatura_saida = celsius_to_kelvin(celsius)
    elif opcao_saida == 4:
        temperatura_saida = celsius_to_rankine(celsius)
    elif opcao_saida == 5:
        temperatura_saida = celsius_to_reaumur(celsius)

    print("Temperatura convertida: {:.2f}".format(temperatura_saida))
