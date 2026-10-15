#ex12.py
#Braian Matheus Couto
#Objetivo: Divisão segura 

#aqui o sistema le oque o usuario digitar e armazena na varivel
dividendo = float(input("Digite o dividendo:"))
divisor = float(input("Digite o divisor:"))

#aqui o sistema ve se o divisor for igual a zero e 
# caso seja mostra erro mas caso não seja faz a formula 
# do resultado e mostra o resultado ao usuario
if divisor == 0 :
    print("erro não existe divisão por 0")
else:
    resultado = dividendo / divisor 
    print(f"Resultado:{resultado}")