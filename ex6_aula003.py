# Exercício 6   - aula003 - Converter temperatura em Celsius

# Função para converter as temperaturas em Celsius
def converter_temp(temp, unidade):
    if unidade == 'F':
        return (temp - 32) * 5/9
    elif unidade == 'K':
        return temp - 273.15
    elif unidade == 'R':
        return (temp - 491.67) * 5/9
    elif unidade == 'Re':
        return temp * 5/4
    else:
        return None

# Entrada da temperatura e da unidade escolhida
temp = float(input('Digite a temperatura: '))
unidade = input('Digite a unidade de temperatura (F, K, R, Re): ')

# A função converter_temp recebe esses dois parâmetros e verifica a unidade para # determinar a fórmula correta para realizar a conversão e armazena na variável temp_c
temp_c = converter_temp(temp, unidade) 

# Print da temperatura com casa 2 casas decimais 
if temp_c is not None:
    print('A temperatura convertida para Celsius é:', round(temp_c,2), '°C')
else:
    print('Unidade de temperatura inválida!')

