import os

# LIMPA O TERMINAL
os.system("cls")

# EXIBIÇÃO DA TABELA DE PREÇOS
menu = '''
+---------+-----------------+-----------------+
| Fruta   | Até 5 Kg        | Acima de 5 Kg   |
|---------+-----------------+-----------------|
| Morango | R$ 2,50 por Kg  | R$ 2,20 por Kg  |
| Maçã    | R$ 1,80 por Kg  | R$ 1,50 por Kg  |
+---------+-----------------+-----------------+
'''
print(menu)

# ENTRADA DE DADOS
kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))


# PROCESSAMENTO: VALOR DO MORANGO
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

# PROCESSAMENTO: VALOR DA MAÇÃ
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

peso_total = kg_morango + kg_maca
valor_total = preco_morango + preco_maca

if peso_total >= 10 or valor_total > 15.00:
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
else:
    valor_final = valor_total

# SAÍDA DE DADOS
print("          EXTRATO DA COMPRA")
print(f"Total de Morangos: {kg_morango:.2f} Kg -> R$ {preco_morango:.2f}")
print(f"Total de Maçãs:    {kg_maca:.2f} Kg -> R$ {preco_maca:.2f}")
print(f"Peso Total:        {peso_total:.2f} Kg")
print(f"Valor Bruto:       R$ {valor_total:.2f}")

if peso_total >= 10 or valor_total > 15.00:
    print(f"Desconto (10%):   -R$ {desconto:.2f}")

print(f"VALOR A PAGAR:     R$ {valor_final:.2f}")