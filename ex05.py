#ex05.py
#Braian Matheus Couto
#Objetivo: Minutos em horas 

#aqui o sistema le oque o usuario escreve e deixe armazenado na variavel min
min_i = int(input("Digite os minutos:"))

#aqui o sistema faz a fórmula das horas e m restantes
horas = min_i // 60
min_r = min_i % 60

#aqui o sistema mostra o resultado ao usuário
print(f"{horas} hora(s) e {min_r}")