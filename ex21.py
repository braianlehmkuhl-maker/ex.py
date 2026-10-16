#ex21.py
#Braian Matheus Couto
#Objetivo: Faixa etária 

#aqui o sistema le oque o usuario digitar e gurda na variável i 
i = int(input("Digite sua idade:"))

#aqui o sistema ve o valo da idade i e compara e mostra ao usuario a resposta
if i < 0 or i >= 150:
    print("Idade inválida")
elif i <= 12:
    print("Criança")
elif i <= 17:
    print("Adolescente")
elif i <= 59:
    print("Adulto")
else:
    print("Idoso")