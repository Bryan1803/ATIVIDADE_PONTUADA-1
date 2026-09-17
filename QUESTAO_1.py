import os

os.system("cls")

# Entrada de dados
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

if (A + B) < C:
    print("A soma de A + B é menor que C.")
elif (A + B) == C:
    print("A soma de A + B é igual a C.")
else:
    print("A soma de A + B é maior que C.")