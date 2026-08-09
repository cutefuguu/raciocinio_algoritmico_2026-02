# 4. Receba o valor de um produto e calcule formas de pagamento.

valor_produto = float(input("Digite o valor do produto: R$ "))

# À vista com 5% de desconto
valor_a_vista = valor_produto * 0.95 

# Valor da parcela em 2x (sem juros)
parcela_2x = valor_produto / 2

# Valor da parcela em 3x com acréscimo de 5% no total
valor_total_3x = valor_produto * 1.05
parcela_3x = valor_total_3x / 3

print("\n--- Opções de Pagamento ---")
print(f"1. À vista (5% de desconto): R$ {valor_a_vista:.2f}")
print(f"2. Em 2x: Duas parcelas de R$ {parcela_2x:.2f} (Total: R$ {valor_produto:.2f})")
print(f"3. Em 3x (5% de acréscimo): Três parcelas de R$ {parcela_3x:.2f} (Total: R$ {valor_total_3x:.2f})")