#Implemente um programa em Python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1.Sendo N lido do teclado
N = int(input("Digite o valor de N: "))
somatorio = 0
i = 1

# Executa o laço enquanto o contador for menor ou igual a N
while i <= N:
    somatorio += i
    i += 1        

print(f"O somatório dos primeiros {N} números é: {somatorio}")