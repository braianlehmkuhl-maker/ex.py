#ex07.py
#Braian Matheus Couto
#Objetivo: Maior ou menor de idade

#aqui o sistema le oque o usuário digitar
idade = int(input("Digite sua idade:"))

#aqui o sistema verifica se o usuário tem a idade superior a 18 e caso tenha mostra maior idade caso não menor de idade
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")