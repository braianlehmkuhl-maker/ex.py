#ex20.py
#Braian Matheus Couto
#Objetivo: Dia da semana 

#aqui o sistema verifica oque o usuário digitar 
dia = int(input("Digite o dia da semana:"))

#aqui o sistema ve o dia corespondente ao dia na semana
#e mostra o resultado ao usuario
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("terça")
elif dia == 4:
    print("quarta")
elif dia == 5:
    print("quinta")
elif dia == 6:
    print("sexta")
elif dia == 7:
    print("sabado")
else:
    print("Dia inválido")