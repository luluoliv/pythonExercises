n1 = float(input("Insira o preço do primeiro produto: R$"))
n2 = float(input("Insira o preço do segundo produto: R$"))
n3 = float(input("Insira o preço do terceiro produto: R$"))

if n1 < n2 and n1 < n3:
    produto_mais_barato = "Produto 1"
elif n2 < n1 and n2 < n3:
    produto_mais_barato = "Produto 2"
else:
    produto_mais_barato = "Produto 3"


print(f"O produto mais barato é: {produto_mais_barato}")