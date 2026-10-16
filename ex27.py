#ex27.py
#Braian Matheus Couto
#Objetivo:Número no intervalo 
#Leia um número inteiro e informe se
#ele está entre 1 e 100, incluindo o 1 e o 100.

#aqui o sistema le oque o usuário digitar 
n = int(input("Digite um número inteiro:"))

#aqui o sistema ve se o N é maior que 100 ou menor 
#que 1 e mostra o resultado ao usuário
if n > 100 or n < 1:
    print("Fora do intervalo")
else:
    print("Dentro do intervalo")