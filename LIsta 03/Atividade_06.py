n = int(input('Digite um numero: '))
i = 0
qnt_numeros = 0

while not n == -1:
    n = int(input('Digite um numero: '))
    i = i + n
    qnt_numeros += 1

else:
    print(f'A media dos numeros e: {i/qnt_numeros}')
