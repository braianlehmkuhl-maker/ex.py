#ex10.py
#Braian Matheus Couto
#Objetivo: Aprovado ou reprovado 

#aqui o sistema le oque o usuário escrever
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

#aqui o sistema faz a formula da média
media = (n1 + n2) / 2

#aqui o sistema ve se a media é maior que 7 e caso seja mostra ao
#usuario aprovado e caso não seja mostra ao usuário reprovado
if media >= 7:
    print(f"Aprovado com a média de {media}")
else:
    print(f"Reprovado com a média de {media}")