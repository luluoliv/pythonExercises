altura = float(input("Insira sua altura: "))
sexo = input("Qual é seu sexo?\nMulher: 1\nHomem: 2\n")

if sexo == 2:
    peso_ideal = (72.7*altura)-58
else:
    peso_ideal = (62.1*altura)-44.7


print("Seu peso ideal é:",peso_ideal)