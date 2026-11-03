# Construa uma funcao capaz de calcular o consumo de combustivel de um carro, sendo que o usuario deve informar a distancia percorrida em km e a quantidade de combustivel. O programa deve imprimir o consumo do carro em km/l.
def consumo_combustivel(distancia, combustivel):
    consumo = distancia / combustivel
    print("O consumo do carro é:", consumo, "km/l")

distancia = float(input("Informe a distância percorrida em km: "))
combustivel = float(input("Informe a quantidade de combustível consumido em litros: "))
consumo_combustivel(distancia, combustivel)