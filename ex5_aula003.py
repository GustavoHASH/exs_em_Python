# Exercício 5   - aula003 - media da média final usando o cálculo da média ponderada

# Recebe as notas e pesos das provas
nota_prova1 = float(input("Digite a nota da prova 1: "))
peso_prova1 = float(input("Digite o peso da prova 1: "))
nota_prova2 = float(input("Digite a nota da prova 2: "))
peso_prova2 = float(input("Digite o peso da prova 2: "))

# Calcula a média ponderada
media_final = (nota_prova1 * peso_prova1 + nota_prova2 * peso_prova2) / (peso_prova1 + peso_prova2)

# Imprime as notas e pesos das provas
print("Nota da prova 1: ", nota_prova1)
print("Peso da prova 1: ", peso_prova1)
print("Nota da prova 2: ", nota_prova2)
print("Peso da prova 2: ", peso_prova2)

# Imprime a mensagem correspondente à média final
if media_final < 5:
    print("REPROVADO")
elif media_final >= 5 and media_final < 8:
    print("APROVADO")
elif media_final >= 8 and media_final < 9:
    print("PARABÉNS O DESEMPENHO FOI MUITO BOM")
else:
    print("PARABÉNS, VOCÊ FOI APROVADO COM LOUVOR")

# Imprime a média final
print("Média final: ", media_final)
