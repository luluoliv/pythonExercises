import math

a = float(input("Insira o primeiro valor: "))

if a == 0:
    print("\nPrograma encerrado.")
else:
    b = float(input("Insira o segundo valor: "))
    c = float(input("Insira o terceiro valor: "))

    delta = (b**2)-4*a*c

    xUm = ((-b) + (float(delta)**0.5))/(2*a)
    xDois = ((-b) - (float(delta)**0.5))/(2*a)

    if delta < 0:
        print("\nA equação não possui raizes reais. Programa encerrado.")
        print(f"O delta é: {delta}")
    elif delta == 0:
        print("\nA equação possui apenas uma raiz real. Programa encerrado.")
        print(f"O delta é: {delta}")
        print(f"""\nRESULTADO:
              X = """)

    elif delta > 0:
        print("\nA equação possui duas raiz reais. Programa encerrado.")
        print(f"\nO delta é: {delta}")
        print(f"""\nRESULTADOS: 
            Xi = {xUm}
            Xii = {xDois}""")
    

    
