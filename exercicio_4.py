# Implemente uma funcao para verificar se um vetor passado como argumento para uma funcao contem um determinado valor tambem passado como argumento. 
import random
def verificar_valor(vetor, valor):
    if valor in vetor:
        return True
    else:
        return False

# Exemplo de uso
vetor = [random.randint(1, 10) for _ in range(10)]
valor = random.randint(1, 10)

resultado = verificar_valor(vetor, valor)

print("O valor", valor, "está no vetor?", resultado)
print("Vetor:", vetor)
print("Valor a ser verificado:", valor)