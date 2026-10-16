#ex22.py
#Braian Matheus Couto
#Objetivo:  Termômetro da Serra 
#Leia a temperatura do dia em °C (pode ter casas decimais) 
#e mostre a mensagem conforme a tabela. 

c = float(input("Digite a temperatura:"))

if c < 0:
    print("Abaixo de zero — risco de geada!")
elif c <= 10:
    print("Muito frio — capriche no agasalho ")
elif c <= 18:
    print("Frio")
elif c <= 25:
    print("Agradável ")
else:
    print("Calor")