# Mostrar matriz com os produtos da máquina de vendas:
produtos = [
    [1, "Coca Cola", 375, 2],
    [2, "Pepsi", 367, 5],
    [3, "Monster", 995, 1], 
    [4, "Café", 125, 100],
    [5, "Red Bull", 1399, 2]
]

# Função para exibir o menu
def exibir_produtos():
    print("==== MÁQUINA DE BEBIDAS ====")
    for produto in produtos:
        print("ID:", produto[0], "| Nome:", produto[1], "| Preço: R$", produto[2] / 100, "| Estoque:", produto[3])
    print("=============================")

# Estoque de Notas e Moedas da máquina
estoque_notas = {20000: 10, 10000: 20, 5000: 20, 2000: 20, 1000: 20}
estoque_moedas = {1: 50, 5: 50, 10: 50, 25: 50, 50: 20, 100: 10}

# Função pra calcular troco
def calcular_troco(troco):
    
    valores_centavos = [20000,10000, 5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 1]

    for valor in valores_centavos:
        quantidade = troco // valor
        troco = troco % valor

        if quantidade > 0:
            if valor >= 200:
                tipo = "nota(s)"
                estoque_notas[valor] -= quantidade
            else:
                tipo = "moeda(s)"
                estoque_moedas[valor] -= quantidade
            print(f"{quantidade} {tipo} de R$ {valor / 100:.2f}")
        # Atualizar o estoque de notas e moedas
        if valor >= 200:
            estoque_notas[valor] -= quantidade
        if estoque_moedas[valor] < 0:
            print(f"Erro: Estoque de {tipo} para R$ {valor / 100:.2f} insuficiente.")
            print("Venda cancelada.")
            return

# Função para realizar pagamento
def processar_pagamento(preco_produto):
    valor_inserido = float(input("Insira o valor em reais (ex: 5.00): R$ ")) * 100  # Convertendo para centavos

    while valor_inserido < preco_produto:
        falta = preco_produto - valor_inserido
        print(f"Valor insuficiente. Faltam R$ {falta / 100:.2f}.")
        valor_inserido += float(input("Insira mais dinheiro: R$ ")) * 100

    # Atualizar o estoque de notas e moedas
    for valor in estoque_notas.keys():
        quantidade = valor_inserido // valor
        estoque_notas[valor] += quantidade
    for valor in estoque_moedas.keys():
        quantidade = valor_inserido // valor
        estoque_moedas[valor] += quantidade

    return valor_inserido

# Função da venda completa
def comprar_produto(id_produto):
    if not isinstance(id_produto, int) or id_produto < 1 or id_produto > len(produtos):
        print("Erro: ID de produto inválido.")
        return

    indice = id_produto - 1
    nome_produto = produtos[indice][1]
    preco_produto = produtos[indice][2]
    estoque_produto = produtos[indice][3]

    if estoque_produto <= 0:
        print(f"Desculpe, o produto '{nome_produto}' está esgotado.")
        return

    print(f"Você selecionou: {nome_produto} - Preço: R$ {preco_produto / 100:.2f}")

    valor_inserido = processar_pagamento(preco_produto)
    troco = valor_inserido - preco_produto
    print(f"Pagamento realizado com sucesso! Troco: R$ {troco / 100:.2f}")

    if troco > 0:
        print("Seu troco é de R$", troco / 100)
        calcular_troco(troco)
    else:
        print("Não há troco a ser devolvido.")

    # Atualizar quantidade do estoque
    produtos[indice][3] -= 1
    print("Compra finalizada! Muito Obrigado 😉")

# Rodar a maquina de vendas:
def iniciar_maquina():
    while True:
        exibir_produtos()
        try:
            produto_escolhido = int(input("Digite o ID do produto que deseja comprar (ou 0 para sair): "))
        except ValueError:
            print("Erro: digite um ID numérico válido.")
            continue

        if produto_escolhido == 0:
            print("Encerrando a máquina de vendas...")
            break

        comprar_produto(produto_escolhido)

# Função para administrar os produtos da máquina
def administrar_produtos():
    print("==== ADMINISTRAÇÃO DE PRODUTOS ====")
    exibir_produtos()

    print("Escolha uma opção: 1. Adicionar produto | 2. Remover produto | 3. Atualizar estoque | 4. Atualizar preço | 5. Sair")
    escolha = int(input("Digite a opção desejada: "))

    if escolha == 1:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto (ex: 5.00): R$ ")) * 100  # Convertendo para centavos
        estoque = int(input("Digite a quantidade em estoque: "))
        novo_id = len(produtos) + 1
        produtos.append([novo_id, nome, int(preco), estoque])
        print(f"Produto '{nome}' adicionado com sucesso!")

    elif escolha == 2:
        id_remover = int(input("Digite o ID do produto que deseja remover: "))
        if 1 <= id_remover <= len(produtos):
            produto_removido = produtos.pop(id_remover - 1)
            print(f"Produto '{produto_removido[1]}' removido com sucesso!")
            # Atualizar IDs dos produtos restantes
            for i in range(len(produtos)):
                produtos[i][0] = i + 1
        else:
            print("Erro: ID de produto inválido.")
    elif escolha == 3:
        id_atualizar = int(input("Digite o ID do produto que deseja atualizar o estoque: "))
        if 1 <= id_atualizar <= len(produtos):
            nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
            produtos[id_atualizar - 1][3] = nova_quantidade
            print(f"Estoque do produto '{produtos[id_atualizar - 1][1]}' atualizado para {nova_quantidade}.")
        else:
            print("Erro: ID de produto inválido.")
    elif escolha == 4:
        id_atualizar = int(input("Digite o ID do produto que deseja atualizar o preço: "))
        if 1 <= id_atualizar <= len(produtos):
            novo_preco = float(input("Digite o novo preço do produto (ex: 5.00): R$ ")) * 100  # Convertendo para centavos
            produtos[id_atualizar - 1][2] = int(novo_preco)
            print(f"Preço do produto '{produtos[id_atualizar - 1][1]}' atualizado para R$ {novo_preco / 100:.2f}.")
        else:
            print("Erro: ID de produto inválido.")
    elif escolha == 5:
        print("Saindo do administrador de produtos...")
        return

iniciar_maquina()