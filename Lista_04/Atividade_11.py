# Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do usuário (sem repetição) e indique quantos acertos ele teve

import random
print("Seja Bem-vindo ao Gerador da Mega-Sena!")

# Gerar 6 números aleatórios
sorteio = ""
qnt_sorteados = 0

while qnt_sorteados < 6:
    num_aleatorio = random.randit(1, 60)
    num_text = f"{num_aleatorio}"

    if num_text not in sorteio:
        sorteio = sorteio + num_text
        qnt_sorteados += 1

print(f'Números sorteados: {sorteio}')

# Obter a aposta do usuário
aposta = ""
qnt_apostados = 0

print("Hora de Apostar!")

while qnt_apostados < 6:
    num_aposta = int(input(f'Digite o {qnt_apostados + 1}º número: '))

    if num_aposta < 1 or num_aposta > 60:
        print('Número inválido! Digite outro número de 1 à 60')
    
    else:
        num_text = f"{num_aposta}"
        if num_text in aposta:
            print("Número já apostado! Digite outro número de 1 à 60")

        else:
            aposta = aposta + num_text
            qnt_apostados += 1

            if num_text in sorteio:
                acertos += 1

print(f"Sua aposta: {aposta}")
print(f'Total de acertos: {acertos}')
