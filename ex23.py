#ex23.py
#Braian Matheus Couto
#Objetivo:  Cardápio da cantina 
#Mostre o cardápio abaixo na tela, leia o código do produto e a quantidade, 
#e mostre o total a pagar. Se o 
#código não existir, mostre Código inválido.

#aqui o sistema mostra ao usuário a tebela 
print("1 Pão de queijo...R$ 4.50")
print("2 Coxinha.........R$ 6.00")
print("3 Pastel..........R$ 7.00")
print("4 Suco............R$ 5.00")
print("5 Cafe............R$ 3.00")

#aqui o sistema pede o código
codigo = int(input("Digite o código:"))

#aqui o sistema ve se o código é valido 
if codigo > 5 or codigo < 1:
    print("Código inválido")
else:

    #aqui o sistema le a quatidade digitada pelo usuario
    quantidade = int(input("Digite a quantidade:"))

    ##aqqui o sistema ve o codigo e determina o preço
    if codigo == 1 :
        preco = 4.50
    elif codigo == 2:
        preco = 6.00
    elif codigo == 3 :
        preco = 7.00
    elif codigo == 4 :
       preco = 5.00
    elif codigo == 5 :
        preco = 3.00

    #aqui o sistema mostra o resultado final ao usuário
    total = preco * quantidade
    print(f"Total:R${total}")