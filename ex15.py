#ex15.py
#Braian Matheus Couto
#Objetivo: Desconto na compra

#aqui o sistema ve oque o usuário digitar
valor = float(input("Digite o Valor da compra:"))

#aqui o sistema ve o valor e define o desconto
if valor > 100:
    desconto = valor * 0.10
else:
    desconto = 0

#aqui o sistema faz a formula final
final = valor - desconto

#aqui o sistema mostra o resultado final ao usuário
print(f"Desconto:{desconto}")
print(f"valor final da compra:{final}")