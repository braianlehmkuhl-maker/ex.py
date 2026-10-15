#ex06.py
#Braian Matheus Couto
#Objetivo: Compra na cantina 

#aqui o sistema le oque o usuário digitar
preco = float(input("DIgite o preço do produto:"))
quantidade = int(input("Digite a quantidade:"))
pago = float(input("Valor pago:"))

#aqui o sistema faz a formula do total e do troco
total = preco * quantidade
troco = pago - total

#aqui o sistema mostra o total e o troco ao usuário
print(f"Total:{total}")
print(f"Troco:{troco}")