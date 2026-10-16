#ex38.py
#Braian Matheus Couto
#Objetivo:Equação do 2º grau

##aqui o sistema mostra a equação
print("ax² + bx + c = 0")

#aqui o sistema le oque o usuario diz
a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

#aqui o sistema ve se a = 0
if a == 0:
    print("Não é uma equação de 2° grau")

#aqui o sistema faz a conta do delta
else:
    delta = b ** 2 - 4 * a * c

    ##aqui o sistema verifica a(s) raiz(s) real(s)
    if delta < 0:
        print("não xistem raízes reias")

    elif delta ==0:
            raiz = -b / (2*a)
            print(f"Uma raiz real: {raiz}")
    else:
        raiz_1 = (-b + delta ** 0.5) / (2*a)
        raiz_2 = (-b - delta ** 0.5) / (2*a)
        print(f"duas raizes reias {raiz_1} e {raiz_2}")    