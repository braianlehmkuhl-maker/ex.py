#ex17.py
#Braian Matheus Couto
#Objetivo: Positivo, negativo ou zero

#aqui o sistema le oque o usuário digitar
n = int(input("Digite um número inteiro:"))

#aqui o sistema verifiva o número para ver se é posistivo, negativo ou zero
#e mostra o resultado ao usuário
if n == 0:
    print("Zero")
elif n < 0:
    print("Negativo")
else:
    print("Positivo")