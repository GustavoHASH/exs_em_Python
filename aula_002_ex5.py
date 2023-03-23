#Aula002 - INPUT/OUTPUT - Exercício 5 - distância linear entre pontos(reta)


#lendo as coordenadas de origem e destino, lembre-se de usar vírgulas
origem = input("Digite as coordenadas de origem (x,y): ")
destino = input("Digite as coordenadas de destino (x,y): ")

#verificando se foram digitadas duas coordenadas separadas por vírgula
if "," not in origem or "," not in destino:
    print("Coordenadas inválidas. Digite as coordenadas no formato x,y.")
else:
    x1, y1 = map(float, origem.split(","))
    x2, y2 = map(float, destino.split(","))

    # Calculando a distância linear - fato interessante, 0.5 é o mesmo que calcular a raiz quadrada
    distancia = ((x2-x1)**2 + (y2-y1)**2)**0.5

    # Imprimindo o resultado
    print("A distância linear entre os pontos é:", distancia)
