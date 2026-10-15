#ex09.py
#Braian Matheus Couto
#Objetivo: Par ou ímpar

#aqui o sistema le oque o usuario escreve
n = int(input("Digite um numero inteiro:"))

#Aui o sistema verifica se o número é divisível por 1 é igual a zero 
#entao caso seja o número é par e mostra o resultado ao usuário
if n % 2 == 0 :
    print("Numero par")
else:
    print("Impar")