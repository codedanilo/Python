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