#ex26.py
#Braian Matheus Couto
#Objetivo:Desconto progressivo 
#Valor da compra (R$) 
#Leia o valor de uma compra e aplique o desconto da faixa correspondente.
#Mostre o valor do desconto e o valor final. 

#aqui o sistema ve oque o usuário digitar e armazena a variável
valor = float(input("Digite o valor da compra:"))

#aqui o sistema ve se tem desconto e faz a fórmula do desconto
if valor <= 50 :
    desconto = 0
else:
    if valor <= 100:
        desconto = valor * 0.05
    elif valor <= 200:
        desconto = valor * 0.10
    elif valor > 200 :
        desconto = valor * 0.15

#aqui o sistema faz a fórmula do final
final = valor - desconto

#aqui o sistema mostra o resultado final ao usuário
print(f"valor final de R${final} apos o desconto de R${desconto}")