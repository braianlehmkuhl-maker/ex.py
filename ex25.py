#ex25.py
#Braian Matheus Couto
#Objetivo:Radar com tipo de infração 
#Leia o limite de velocidade da via e a velocidade 
#medida do carro. Calcule quantos por cento a velocidade 
#passou do limite e classifique conforme a tabela.

#aqui o sistema le oque o usuário digitar 
limite = float(input("Diite o limite da via:"))
velocidade = float(input("Digite a valocidade do carro:"))

#aqui o sistema ve se tem infração ou não
if velocidade < limite:
    print("Sem infração")
else:

    #aqui o sistema faz a fórmula do percentual
    percentual = ((velocidade - limite) / limite ) * 100

    #aqui o sistema ve o percentual e mostra o resultado ao usuário
    if percentual <= 20:
        print(f"Percentual:{percentual}, infração média")
    elif percentual<=50:
        print(f"percentual:{percentual} Infração grave")
    else:
        print(f"percentual:{percentual} Infração gravíssima")