mb = float(input("Insira o tamanho do arquivo (em MB): "))
mbps = float(input("Insira a velocidade da sua internet  (em Mbps): "))

tempo = mb/mbps

print("O tempo aproximado de download do arquivo é de", tempo, "minutos.")