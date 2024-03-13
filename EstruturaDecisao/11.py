print("""\nAs Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
        lhe contraram para desenvolver o programa que calculará os reajustes.\n""")

salario = float(input("Olá colaborador! Insira seu salário: "))

percentual = 0
salario_reajuste = 0


if salario > 0 and salario <= 280:
    percentual = 0.2
    salario_reajuste = salario + (salario*percentual)

elif salario > 280 and salario <= 700: 
    percentual = 0.15
    salario_reajuste = salario + (salario*percentual)

elif salario > 700 and salario <= 1500: 
    percentual = 0.1
    salario_reajuste = salario + (salario*percentual)

elif salario > 1500: 
    percentual = 0.05
    salario_reajuste = salario + (salario*percentual)

else:
    print("Salário inválido.")

print(f"""Salário antes do reajuste: R${salario}
          Percentual aplicado: {percentual*100}%
          Valor de aumento: {percentual*salario}
          Salário c/ reajuste: R${salario_reajuste}""")

