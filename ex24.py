#ex24.py
#Braian Matheus Couto
#Objetivo:Calculadora de IMC 
#IMC 
#Leia o peso (kg) e a altura (m) de uma pessoa.
#Calcule o IMC = peso ÷ (altura × altura) e mostre a 
#classificação. 

#aqui o sistema le oque o usuário digitar e armazena na variável
kg = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura:"))

#aqui o sistema faz a fórmula do IMC
imc = kg / (altura*altura)

#Aqui o sistema verifica o imc e calcula o peso e mostra o resultado ao usuário
if imc <= 18.5:
    print(f"imc:{imc} Abaixo do peso")
elif imc <= 25:
    print(f"IMC:{imc} Peso normal")
elif imc <= 30:
    print(f"IMC:{imc} sobrepeso")
else:
    print(f"IMC:{imc} obesidade")