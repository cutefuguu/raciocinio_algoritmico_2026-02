'''Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um número que ele gostaria de
pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is) posição(ões) ele foi encontrado e quantas ocorrências
foram detectadas.'''

# Ler 10 números e suas posições
print('Digite 10 números inteiros:')

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))
n5 = int(input("Digite o 5º número: "))
n6 = int(input("Digite o 6º número: "))
n7 = int(input("Digite o 7º número: "))
n8 = int(input("Digite o 8º número: "))
n9 = int(input("Digite o 9º número: "))
n10 = int(input("Digite o 10º número: "))

# Pesquisar número nesse vetor

pesquisa = int(input("Digite o número que gostaria de pesquisar: "))


# Verificar em que posição e quantas ocorrências

ocorrencia = 0
posicao = ""

if pesquisa == n1:
    posicao = "nº1"
    ocorrencia += 1
    