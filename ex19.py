#ex19.py
#Braian Matheus Couto
#Objetivo: Situação do aluno 

#aqui o sistema verifica oque o usuário digitar e armazena na variavel
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

#aqui o sistema faz a formula da média 
media = (n1+n2) / 2

#aqui o sistema verifica se o aluno esta aprovado, de recuperação
#ou reprovado e mostra o resultado ao usuário
if media > 7.0:
    print("Aprovado")
elif media > 5.0 and media < 7.0:
    print("Recuperação")
else:
    print("Reprovado")