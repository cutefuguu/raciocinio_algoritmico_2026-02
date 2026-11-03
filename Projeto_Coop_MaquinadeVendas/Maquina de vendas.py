produtos = [
    [1, "Coca Cola", 375, 2],
    [2, "Pepsi", 367, 5],
    [3, "Monster", 995, 1],
    [4, "Café", 125, 100],
    [5, "Red Bull", 1399, 2]
]

def exibir_produtos():
    print("==== MÁQUINA DE BEBIDAS ====")
    for produto in produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R$ {produto[2] / 100:.2f} | Estoque: {produto[3]}")
    print("=============================")

estoque_notas = {20000: 10, 10000: 20, 5000: 20, 2000: 20, 1000: 20}
estoque_moedas = {100: 10, 50: 20, 25: 50, 10: 50, 5: 50, 1: 50}

def calcular_troco(troco):
    valores_centavos = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
    temp_notas = estoque_notas.copy()
    temp_moedas = estoque_moedas.copy()
    troco_a_dar = []

    # Passo 1: Simula o troco para ver se é possível
    for valor in valores_centavos:
        if troco == 0:
            break
        quantidade = troco // valor
        
        if quantidade > 0:
            if valor >= 200:
                if valor in temp_notas and temp_notas[valor] >= quantidade:
                    temp_notas[valor] -= quantidade
                    troco_a_dar.append((quantidade, "nota(s)", valor))
                    troco = troco % valor
            else:
                if valor in temp_moedas and temp_moedas[valor] >= quantidade:
                    temp_moedas[valor] -= quantidade
                    troco_a_dar.append((quantidade, "moeda(s)", valor))
                    troco = troco % valor

    # Passo 2: Verifica se sobrou valor sem notas disponíveis
    if troco > 0:
        print("Erro: A máquina não tem notas ou moedas suficientes para o troco.")
        return False

    # Passo 3: Efetiva o desconto no estoque real
    for quantidade, tipo, valor in troco_a_dar:
        if tipo == "nota(s)":
            estoque_notas[valor] -= quantidade
        else:
            estoque_moedas[valor] -= quantidade
        
    return True

def processar_pagamento(preco_produto):
    valor_inserido = float(input("Insira o valor em reais (ex: 5.00): R$ ")) * 100
    while valor_inserido < preco_produto:
        falta = preco_produto - valor_inserido
        print(f"Valor insuficiente. Faltam R$ {falta / 100:.2f}.")
        valor_inserido += float(input("Insira mais dinheiro: R$ ")) * 100
    return valor_inserido

def comprar_produto(id_produto):
    if id_produto < 1 or id_produto > len(produtos):
        print("Erro: ID de produto inválido.")
        return

    indice = id_produto - 1
    nome_produto = produtos[indice][1]
    preco_produto = produtos[indice][2]
    estoque_produto = produtos[indice][3]

    if estoque_produto <= 0:
        print(f"Desculpe, o produto '{nome_produto}' está esgotado.")
        return

    print(f"Você selecionou: {nome_produto} | Preço: R$ {preco_produto / 100:.2f}")

    valor_inserido = processar_pagamento(preco_produto)
    troco = valor_inserido - preco_produto

    if troco > 0:
        print(f"Pagamento realizado! Calculando troco de R$ {troco / 100:.2f}...")
        sucesso = calcular_troco(troco)
        if not sucesso:
            print("Venda cancelada. Seu dinheiro foi devolvido.")
            return # Interrompe antes de descontar o produto
    else:
        print("Valor exato inserido. Não há troco a ser devolvido.")

    # Só atualiza a quantidade se o pagamento e o troco deram certo
    produtos[indice][3] -= 1
    print("Compra finalizada! Muito Obrigado 😉")

def iniciar_maquina():
    while True:
        exibir_produtos()
        try:
            produto_escolhido = int(input("Digite o ID do produto (ou 0 para sair): "))
        except ValueError:
            print("Erro: digite um ID numérico válido.")
            print("="*30)
            continue

        if produto_escolhido == 0:
            print("Encerrando a máquina de vendas...")
            break

        comprar_produto(produto_escolhido)

iniciar_maquina()