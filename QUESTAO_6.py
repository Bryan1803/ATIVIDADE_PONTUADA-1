import os
os.system("cls")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


print(f"Média: {media:.1f}")

if media >= 6.0:
    print("Parabéns! Você foi aprovado!")
elif media >= 4.0:
    print("Aluno em recuperação.")
else:
    print("Aluno reprovado.")
