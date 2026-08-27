numero = 0
qnt_pares = 0
qnt_impares = 0

while numero < 10:
    numero = int(input('Informe um numero:'))
    if numero % 2 == 0:
        qnt_pares += 1
    numero += 1
    else:
        qnt_impares += 1
print(f'Pares:{qnt_pares} / Impares:{qnt_impares}')