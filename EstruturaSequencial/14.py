peso_peixe = float(input("INSIRA O PESO DOS PEIXES: "))
multa = 0

if peso_peixe > 50:
    excesso = peso_peixe - 50
    multa_total = excesso*4
    print("SUA MULTA É DE R$",multa_total, "COM", excesso,"kg A MAIS DO REGULAMENTO.")
else:
    print("JOÃO NÃO PRECISARÁ PAGAR NENHUMA MULTA.")