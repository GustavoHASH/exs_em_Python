#Aula 002  - INPUT/OUTPUT -  Exercício 3 -
#monitoramentos de parâmetros de movimento cinemático dos veículos



#lista com as distâncias de cada trecho em metros
distancias = [100, 200, 150, 300]

#lista com os tempos de percurso de cada trecho em segundos
tempos = [20, 30, 25, 40]

#cálculo a velocidade média de cada trecho em m/s
velocidades = [distancias[i] / tempos[i] for i in range(len(distancias))]

#cálculo da velocidade média total em m/s
velocidade_media_total = sum(distancias) / sum(tempos)

#cálculo da aceleração entre dois trechos cons em m/s^2
aceleracoes = [(velocidades[i+1] - velocidades[i]) / tempos[i+1] for i in range(len(velocidades)-1)]

#print dos resultados
print("Velocidades médias de cada trecho:", velocidades)
print("Velocidade média total:", velocidade_media_total)
print("Acelerações entre trechos consecutivos:", aceleracoes)










