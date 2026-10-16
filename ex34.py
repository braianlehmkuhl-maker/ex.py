#ex34.py
#Braian Matheus Couto
#Objetivo:Aprovação com frequência 

#aqui o sistema le oque o usuário digitar e armazena na variável
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
f = float(input("Digite a frequência em %:"))

#aqui o sistema faz a fórmula da média
media = (n1 + n2) // 2 

#aqui o sistema ve as notas e a frequência e moostra o resultado ao usuário
if f < 75 and media < 7.0:
    print("Reprovado")
elif f < 75 and media >= 7.0:
    print("Reprovado por falta")
elif f >= 75 and media < 7.0:
    print("Reprovado por nota")
else:
    print("Aprovado")