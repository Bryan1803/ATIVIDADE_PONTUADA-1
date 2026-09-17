import os
os.system ("cls")
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quantidade * preco_unitario

if quantidade <= 5:
    porcentagem_desconto = 0.02
elif quantidade <= 10:
    porcentagem_desconto = 0.03
else:
    porcentagem_desconto = 0.05

desconto = total * porcentagem_desconto
total_a_pagar = total - desconto

print(f"\nProduto: {nome_produto}")
print(f"Total: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
