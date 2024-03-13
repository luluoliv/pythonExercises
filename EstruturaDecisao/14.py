n1 = float(input("Insira sua nota de matemática: "))
n2 = float(input("Insira sua nota de português: "))

media =  (n1+n2)/2

if media >= 0 and media <= 4:
    conceito = "E"
elif media > 4 and media <= 6:
    conceito = "D"
elif media > 6 and media <= 7.5:
    conceito = "C"
elif media > 7.5 and media <= 9:
    conceito = "B"
elif media > 9 and media <= 10:
    conceito = "A"

aprovado = ["A","B","C"]

if conceito in aprovado:
    mensagem = "Parabéns! Você foi aprovado. 🎉🥳"
else:
    mensagem = "Infelizmente, você não foi aprovado. 😔 Continue tentando!"

print(f"""\nNota de matemática: {n1}
Nota de português: {n2}
Média: {media}\n""")

print(f"""Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E\n""")

print(mensagem)



