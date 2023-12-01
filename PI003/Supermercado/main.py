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