#Aula 002  - INPUT/OUTPUT -  Exercício 4  - Trajetória Balística

#import da biblioteca numpy para fazer operações matemáticas com vetores
import numpy as np

#definindo os valores iniciais
V0 = 20 # velocidade inicial em m/s
q = np.deg2rad(45) # ângulo de lançamento em radianos
g = 9.81 # aceleração da gravidade em m/s^2

#definindo o intervalo de tempo em segundos
delta_t = 0.1
tempo = np.arange(0, 10, delta_t)

#cálculo  das posições horizontais e alturas em função do tempo
x_pos = V0 * np.cos(q) * tempo
y_pos = V0 * np.sin(q) * tempo - 0.5 * g * tempo**2

#print dos resultados
print("Posição horizontal em função do tempo:", x_pos)
print("Altura em função do tempo:", y_pos)
