'''
data_valida = False
while not data_valida:
    dia = int(input('Digite o dia: '))
    mes = int(input('Digite o mes: '))
    ano = int(input('Digite o ano: '))

    if ano >= 1 and mes >= 1 and mes <= 12 and dia >= 1 and dia <= 31:
        data_valida = True
    else:
        print("Data invalida! Tente novamente.")

print(f'{dia}/{mes}/{ano}')
'''
dia = int(input('Digite o dia: '))
while dia >= 1 or dia <= 31:
    print(int(input('Erro. Digite o dia novamente: ')))

mes = int(input('Digite o mes: '))
while mes >= 1 or mes <= 12:
     print(int(input('Erro. Digite o mes novamente: ')))

ano = int(input('Digite o ano: '))
while ano >= 1