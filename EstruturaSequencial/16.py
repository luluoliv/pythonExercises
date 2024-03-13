area_pintada = float(input("INSIRA O TAMANHO EM METROS DA ÁREA A SER PINTADA: "))

litros = area_pintada/3

latas = litros/18

if latas%18 != 0:
    latas=+1

tinta_preco = latas*80
print('Voce deverá comprar', latas, 'latas.')
print('O valor total é:', tinta_preco)

