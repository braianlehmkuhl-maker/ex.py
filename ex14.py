#ex14.py
#Braian Matheus Couto
#Objetivo: Radar de velocidade

#aqui o sistema ve oque o usuário digitar
velocidade = float(input("Digite a velocidade do carro:"))

#aqui o sistema ve se a velocidade está dentro do 
#limite e mostra o resultado ao usuario
if velocidade > 80:
    print("Multado você passou,",velocidade - 80," km/h do limite")
else:
    print(f"Velocidade:{velocidade}")
    print("Boa viagem")