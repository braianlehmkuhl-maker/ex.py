#ex18.py
#Braian Matheus Couto
#Objetivo: Maior ou iguais 

#aqui o sistema le oque o usuário digitar e armazena nas variaveis
n1 = int(input("Digite um número inteiro:"))
n2 = int(input("Digite outro número inteiro:"))

#aqui o sistema verifica qual é maior e mostra o reusltado 
if n1 > n2:
    print(f"Maior:{n1}")
elif n2 > n1:
    print(f"Maior:{n2}")
else:
    print("Numeros iguais")