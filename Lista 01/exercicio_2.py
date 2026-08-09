# 2. Leia o ano de nascimento e calcule a idade no final de 2026.

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_ref = 2026

idade = ano_ref - ano_nascimento

print(f"Até o final de {ano_ref}, você completará {idade} anos.")