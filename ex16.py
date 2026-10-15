#ex16.py
#Braian Matheus Couto
#Objetivo: Saque no caixa eletrônico 

#aqui o sistema le oque o usuário digitar e salva
saldo = float(input("Digite seu saldo:"))
sacar = float(input("quanto quer sacar:"))


#aqui o sistema mostra o resultado ao usário
if saldo > sacar:
    saldo = saldo - sacar
    print(f"Saldo atual:{saldo}")
else:
    print("Saldo insuficiente")