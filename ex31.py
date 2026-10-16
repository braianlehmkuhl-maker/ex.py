#ex31.py
#Braian Matheus Couto
#Objetivo:Tipo de triângulo 

#aqui o sistema le oque o usuário digitar e armazena o valor na variável
l1 = int(input("Digite o primeiro lado do triângulo:"))
l2 = int(input("Digite o segundo lado do triângulo:"))
l3 = int(input("Digite o terceiro lado do triângulo:"))

#aqui o sistema verifica se ele é ou não é um triângulo 
if l1 > (l2+l3) or l2 > (l1+l3) or l3 > (l2+l1) :
    print("Esses lados não formam um triângulo")

#aqui o sistema verifica o tipo dele e mostra ao usuário
else:
    if l1 == l2 and l1 == l3:
      print("Equilátero")
    elif l1 != l2 and l2 != l3 and l1 != l3:
      print("Escaleno")
    else:
      print("Isóceles")