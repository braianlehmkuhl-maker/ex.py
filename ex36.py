#ex36.py
#Braian Matheus Couto
#Objetivo:Pedra, papel e tesoura 

#aqui o sistema le a jogada dos jogadores
j1 = input("jogador 1 digite pedra, papel ou tesoura:")
j2 = input("jogador 2 digite pedra, papel ou tesoura:")

#aqui o sistema vai ver quem ganhou e mostra o resultado
if j1 == "pedra" and j2 == "tesoura":
    print("jogador 1 venceu")
elif j1 == "pedra" and j2 == "papel":
    print("jogador 2 venceu")
elif j1 == "pedra" and j2 == "pedra":
    print("empate")
elif j1 == "papel" and j2 =="tesoura":
    print("jogador 2 venceu")
elif j1 == "papel" and j2 =="pedra":
    print("jogador 1 venceu")
elif j1 == "papel" and j2 =="papel":
    print("empate")
elif j1 == "tesoura" and j2 =="pedra":
    print("jogador 2 venceu")
elif j1 == "tesoura" and j2 =="papel":
    print("jogador 1 venceu")
elif j1 == "tesoura" and j2 =="tesoura":
    print("empate")

##aqui é caso algum dos jogadores coloque uma opção inválida
else:
    print("jogada inválida")