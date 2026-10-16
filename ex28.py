#ex28.py
#Braian Matheus Couto
#Objetivo:Vogal ou consoante

#aqui o sistema ve oque o usuário digitar e armazena na varivel letra
letra = str(input("Digite uma letra:"))

#aqui o sistema ve se a letra é vogal ou consoante e mostra o resultado ao usuário
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante")