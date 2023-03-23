# Exercício 1 - aula003 - acesso com senha númerica


# Defina a senha pré-cadastrada
senha = "1234"

# Solicita ao usuário que digite sua senha
user_password = input("Digite sua senha numérica: ")

# Verifique se a entrada é numérica e tem o mesmo comprimento da senha pré-cadastrada
if user_password.isnumeric() and len(user_password) == len(senha):
     # Se a entrada for válida e corresponder à senha pré-cadastrada, imprima "ACESSO PERMITIDO"
     if user_password == senha:
         print("ACESSO PERMITIDO!!!")
     # Caso contrário, imprima "ACESSO NEGADO"
     else:
         print("ACESSO NEGADO!!!")
else:
     print("Formato de senha inválido.");
