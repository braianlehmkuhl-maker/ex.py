#ex30.py
#Braian Matheus Couto
#Objetivo:Ano bissexto 

#aqui o sistema le oque o usuário digitar
ano = int(input("Digite um ano:"))

#aqui o sistema ve se o ano é bissexto ou não e mostra o resultado ao usuário
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Não é bissexto")