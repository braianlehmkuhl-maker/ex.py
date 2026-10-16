#ex29.py
#Braian Matheus Couto
#Objetivo: O maior de três 

#Aqui o sistema vai ler oque o usuário digitar e armazenar na variável
n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segndo número inteiro:"))
n3 = int(input("Digite o terceiro número inteiro:"))

#aqui o sistema vai verificar o maior e mostrar o resultado ao usuário
if n1 > n2 and n1 > n3:
    print(f"Maior:{n1}")
elif n2 > n1 and n2 > n3:
    print(f"Maior:{n2}")
else:
    print(f"Maior:{n3}")