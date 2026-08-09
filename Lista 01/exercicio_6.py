# 6. Quantidade e valor de latas de tinta para um tanque cilíndrico.
import math

altura = float(input("Digite a altura do cilindro (em metros): "))
raio = float(input("Digite o raio do cilindro (em metros): "))

# Calcular a área total do cilindro
area_cilindro = 2 * math.pi * raio * (raio + altura)

# Calcular a capacidade de pintura de 1 lata // Se 1 litro pinta 3 m² e 1 lata tem 5 litros:
metros_por_lata = 5 * 3  # 1 lata pinta 15 m²

# Calcular quantidade de latas necessárias

quantidade_latas = math.ceil(area_cilindro / metros_por_lata)

# Passo 4: Calcular o valor total
preco_lata = 50.00
valor_total = quantidade_latas * preco_lata

print("\n--- Orçamento da Pintura ---")
print(f"Área total do cilindro: {area_cilindro:.2f} m²")
print(f"Quantidade de latas necessárias: {quantidade_latas}")
print(f"Custo total: R$ {valor_total:.2f}")