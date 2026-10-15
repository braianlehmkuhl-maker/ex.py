#ex02.py
#Braian Matheus Couto
#Objetivo: Ler 2 números e mostrar adição nSubtração e nMultiplicação

#aqui o sistema le oque o usuário escrever e define a variável
n1 = float(input("Digite um número:"))
n2 = float(input("Digite outro número:"))

#aqui o sistema faz as variáveis das contas 
adi = n1 + n2
sub = n1 - n2
mul = n1 * n2

#e aqui o sistema mostra o resultado ao usuário
print("Adição:",adi)
print("Subtração:",sub)
print("Multiplicação:",mul)