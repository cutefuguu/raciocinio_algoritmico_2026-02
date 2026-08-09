# 5. Calcule o consumo médio de um automóvel (km/l).

distancia = float(input("Digite a distância total percorrida (em KM): "))
litros_consumidos = float(input("Digite o volume de combustível consumido (em litros): "))

consumo_medio = distancia / litros_consumidos

print(f"O consumo médio do seu automóvel é de {consumo_medio:.2f} km/l.")