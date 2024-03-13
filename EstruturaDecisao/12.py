salario_bruto = float(input("Olá colaborador! Insira seu salário: "))


#DESCONTO IR
if salario_bruto > 0 and salario_bruto <= 900:
    desconto = 0

elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto = 0.05
    ir = salario_bruto*desconto

    salario_final = salario_bruto - ir

elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto = 0.1
    ir = salario_bruto*desconto

    salario_final = salario_bruto - ir

elif salario_bruto > 2500:
    desconto = 0.2
    ir = salario_bruto*desconto

    salario_final = salario_bruto - ir

else:
    print("Salário inválido!")

ir = salario_bruto*desconto
fgts = salario_bruto*0.11
descontos = ir + fgts

print(f"""Salário Bruto: R${salario_bruto}
          Imposto de Renda: R${ir}
          FGTS: R${fgts}
          Total descontos: R${descontos}
          Salário Liquido: R${salario_final}""")