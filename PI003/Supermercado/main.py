def inserir_produto(produtos):
    codigo = input("Digite o codigo do produto (13 digitos): ")
    nome = input("Digite o nome do produto (começando com letra maiuscula): ")
    preco = float(input("Digite o preco do produto: "))

    produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")

def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")

    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!\n")
            return

    print("Produto não encontrado.\n")

def listar_produtos(produtos):
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    print("\n")

def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")

    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}\n")
            return

    print("Produto não encontrado.\n")