nota1 = int(input("Insira sua primeira nota: "))
nota2 = int(input("Insira sua segunda nota: "))

media = (nota1+nota2)/2

if media >= 7:
    print("Aprovado com", media, "de média.")
elif media < 7:
    print("Reprovado com", media, "de média.")
elif media == 10:
    print("Aprovado com Distinção com", media, "de média.")

