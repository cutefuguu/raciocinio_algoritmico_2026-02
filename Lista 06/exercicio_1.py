# Escreva uma funcão que imprima os 100 primeiros números ímpares 
def impares():
    for i in range (100):
        if i %  2 == 1:
            print(i)

print("Os 100 primeiros números ímpares são:")
impares()