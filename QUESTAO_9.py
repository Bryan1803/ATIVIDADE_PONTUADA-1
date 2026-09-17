import os
os.system("cls")
renda_mensal = float(input("Digite a renda mensal do cliente: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))


valor_prestacao = valor_emprestimo / num_prestacoes

limite_total_emprestimo = renda_mensal * 10
limite_prestacao = renda_mensal * 0.30

if valor_emprestimo <= limite_total_emprestimo and valor_prestacao <= limite_prestacao:
    print("\nEmpréstimo CONCEDIDO!")
else:
    print("\nEmpréstimo NÃO CONCEDIDO.")
