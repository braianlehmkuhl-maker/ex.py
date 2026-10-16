#ex35.py
#Braian Matheus Couto
#Objetivo:Calculadora 

#aqui o sistema le oque o usuário digitar e armazena na variável
n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
operador = input("digite o operador:")

#aqui o sistema ve se a divisao é por zero ou não
if n2 == 0 :
    print("Erro:Divisão por zero")
    operado = False
else:
        
        #aqui o sistema faz as contas
        if operador == "+":
            resultado = n1 + n2
            operado = True
        elif operador == "-":
            resultado = n1 - n2
            operado = True
        elif operador == "*":
            resultado = n1 * n2
            operado = True
        elif operador == "/":
            resultado = n1 / n2
            operado = True
        else:
            print("Operador inválido")
            operado = False

#aqui o sistema mostra o resultado caso tenha
if operado:
     print(f"Resultado:{resultado}")