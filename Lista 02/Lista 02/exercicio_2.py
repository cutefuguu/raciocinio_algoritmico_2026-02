# O cliente precisa informar a quntidade de copias que precisa imprimir
copias_imp = int(input('Quantas cópias vc precia imprimir?: '))

if copias_imp <= 100:
    valor_unt = 0.25

else:
    valor_unt = 0.20

valor_imp = copias_imp*valor_unt
print("O valor do seu material é R${valor_imp}")