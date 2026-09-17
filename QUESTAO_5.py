import os
os.system ("cls")

operacao = input("Digite a operação (+, -, *, /): ")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    if B == 0:
        resultado = "Erro: Divisão por zero!"
    else:
        resultado = A / B
else:
    resultado = "Operação inválida"

print(f"Resultado: {resultado}")
