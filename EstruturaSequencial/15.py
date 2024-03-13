salario_hora = float(input("Quanto você ganha por hora? "))
horas_mes = float(input("Quantas horas você trabalha por mês? "))

salario_bruto = salario_hora*horas_mes

imposto_renda = (11/100)*salario_bruto

inss = (8/100)*salario_bruto

sindicato = (5/100)*salario_bruto

salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("+ SALÁRIO BRUTO: R$", salario_bruto)
print("- IR: R$", imposto_renda)
print("- INSS: R$", inss)
print("- SINDICATO: R$", sindicato)
print("= SALÁRIO LÍQUIDO: R$", salario_liquido)
