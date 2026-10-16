#ex32.py
#Braian Matheus Couto
#Objetivo:Login com usuário e senha 

#aqui o sistema le oque o usuário digitar e salva nas variáveis
usuario = input("Digite seu usuário:")
senha = input("Digite sua senha:")

#aqui o sistema verifica o usuario e mostra o resultado
if usuario != "aluno":
    print("usuário não encontrado")
else:

    #aqui o sistema verifica se a senha esta correta e mostra o resultado
    if senha != "1234":
        print("Senha incorreta")
    else:
        print("Login realizado com sucesso")