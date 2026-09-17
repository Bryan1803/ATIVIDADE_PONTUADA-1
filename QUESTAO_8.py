import os
os.system("cls")
print("==================================")
print("     TABELA DE PREÇOS (CD's)      ")
print("==================================")
print("  COR        |  PREÇO             ")
print("----------------------------------")
print("  Verde      |  R$ 10,00          ")
print("  Azul       |  R$ 20,00          ")
print("  Amarelo    |  R$ 30,00          ")
print("  Vermelho   |  R$ 40,00          ")
print("==================================\n")

cor = input("Digite a cor do CD: ")

cor_padronizada = cor.strip().lower()


if cor_padronizada == "verde":
    preco = 10.00
elif cor_padronizada == "azul":
    preco = 20.00
elif cor_padronizada == "amarelo":
    preco = 30.00
elif cor_padronizada == "vermelho":
    preco = 40.00
else:
    preco = None

if preco is not None:
    print(f"\nO preço do CD {cor.capitalize()} é: R$ {preco:.2f}")
else:
    print("\nCor inválida! Por favor, escolha uma cor da tabela.")
