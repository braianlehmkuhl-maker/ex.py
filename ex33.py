#ex33.py
#Braian Matheus Couto
#Objetivo: Voto obrigatório 

#aqui o sistema le oque o usuário digitar e armazena na variável
idade = int(input("Digite sua idade:"))

#aqui o sistema ve a idade e calcula o voto e mostra ao usurio o resultado
if idade < 16 :
    print("Não pode votar")
elif idade <= 17 or idade > 70:
    print("Voto faculvativo")
elif idade < 70:
    print("Voto Obrigatório")