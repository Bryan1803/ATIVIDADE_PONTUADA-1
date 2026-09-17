import os
os.system("cls")

nome = input("Digite seu nome: ")
sexo = input("Digite o seu sexo de registro: ").upper()
estado_civil = input("Digite seu estado civil: ").lower()

# Inicializa a variável caso não entre no IF
anos_casada = "Não aplicável"

# PROCESSAMENTO E VALIDAÇÃO
if sexo == "F" and estado_civil == "casada":
    anos_casada = input("Digite o tempo de casada (em anos): ")

# EXIBIÇÃO DOS DADOS INFORMADOS
print("DADOS")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil.capitalize()}") # Deixa a primeira letra maiúscula
print(f"Tempo de casada: {anos_casada}")

# SAÍDA FINAL
print("\n--- Fim do algoritmo ---")