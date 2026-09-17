import os
os.system("cls")
print("===========================================")
print("      POSTO DE COMBUSTÍVEL - DESCONTOS     ")
print("===========================================")
print("  TIPO       | ATÉ 25 LITROS | ACIMA 25 LITROS")
print("-------------------------------------------")
print("  A-Álcool   | 10% de desc.  | 20% de desc.   ")
print("  G-Gasolina | 15% de desc.  | 30% de desc.   ")
print("===========================================\n")

PRECO_ALCOOL = 3.79
PRECO_GASOLINA = 6.59

tipo_combustivel = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ").strip().upper()
litros = float(input("Digite a quantidade de litros vendidos: "))

dados_validos = True

if tipo_combustivel == "A":
    preco_base = PRECO_ALCOOL
    if litros <= 25:
        desconto = 0.10  # 10%
    else:
        desconto = 0.20  # 20%
elif tipo_combustivel == "G":
    preco_base = PRECO_GASOLINA
    if litros <= 25:
        desconto = 0.15  # 15%
    else:
        desconto = 0.30  # 30%
else:
    dados_validos = False

if dados_validos:
    valor_com_desconto = preco_base * (1 - desconto)
    total_a_pagar = litros * valor_com_desconto
    
    print(f"\n--- RECIBO DE PAGAMENTO ---")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")
else:
    print("\nErro: Tipo de combustível inválido! Use 'A' ou 'G'.")
