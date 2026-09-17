import os
# LIMPA O TERMINAL
os.system("cls")

# ENTRADA (Lendo os valores de A e B)
A = int(input("Digite o primeiro número (A): "))
B = int(input("Digite o segundo número (B): "))

# PROCESSAMENTO
if A == B:
    C = A + B
else:
    C = A * B

# SAÍDA
print(f"\nO resultado final (C) é: {C}")
print("\n--- Fim do algoritmo ---")