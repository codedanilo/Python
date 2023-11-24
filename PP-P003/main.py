'''
Exercício 1: Estruturando um código com funções.
● Este exercício já foi implementado no módulo anterior, utilizando C++.
Vejamos agora como ficaria uma versão feita em Python: Faça um programa
para um supermercado que permita a consulta de preço de produtos. O
programa deverá armazenar de cada produto o seu código, seu nome e seu
preço.
○ Ao utilizar o programa o usuário deve poder:
1. Inserir um novo produto
2. Excluir um produto cadastrado
3. Listar todos os produtos com seus respectivos códigos e preços
4. Consultar o preço de um produto através de seu código.
O código deve ser formado de uma string numérica de 13 caracteres (pode
conter zeros a esquerda, então não pode ser um número)
O nome pode ter qualquer tamanho e deve começar sempre com uma letra
maiúscula.
O preço deve ser apresentado com duas casas decimais
O sistema deve listar os produtos na tela, 10 produtos de cada vez em ordem
crescente de preço.
● O código deve ser implementado numa pasta Supermercado e o programa
principal deve ser implementado no arquivo main.py.
● Pode utilizar como modelo o arquivo main.py disponível na postagem da
atividade. Pesquise sobre esta estrutura e para que ela serve.
● Cada uma das funcionalidades do menu de opções deve ser implementada
numa função específica.
● Já que não temos structs em Python vamos usar dicionários para armazenar
cada produto.
● Vamos armazenar os produtos numa lista de dicionários
'''


# Função para inserir um novo produto
def inserir_produto(produtos):
    # Cadastra o produto
    codigo = input("Digite o código do produto (13 caracteres numéricos): ")
    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    preco = float(input("Digite o preço do produto: "))

    # Validar se o código já existe na lista de produtos
    codigos_existentes = [produto['codigo'] for produto in produtos]
    if codigo in codigos_existentes:
        print("Código já existe. Não é possível inserir o produto.")
    else:
        # Validar se o código tem 13 caracteres numéricos
        if len(codigo) == 13 and codigo.isdigit():
            # Validar se o nome começa com letra maiúscula
            if nome[0].isupper():
                            
            # Adicionar o novo produto à lista de produtos
                novo_produto = {'codigo': codigo, 'nome': nome, 'preco': round(preco, 2)}
                produtos.append(novo_produto)
                print("Produto adicionado com sucesso!")
            
            if nome[0].islower():

             print("O nome do produto deve começar com letra maiúscula.")
        else:
            print("Código inválido. Deve ter 13 caracteres numéricos.")

# Função para excluir um produto cadastrado
def excluir_produto(produtos):
    codigo = input("Digite o código do produto que deseja excluir: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

# Função para listar todos os produtos com seus respectivos códigos e preços
def listar_produtos(produtos):
    for i, produto in enumerate(produtos, start=1):
        print("-------------------------------------------------------------------------------------------")
        print(f"{i}. Código: {produto['codigo']} - Nome: {produto['nome']} - Preço: R${produto['preco']}")
        print("-------------------------------------------------------------------------------------------")

# Função para consultar o preço de um produto através do código
def consultar_preco(produtos):
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print("-------------------------------------------------------------------------------------------")
            print(f"O preço do {produto['nome']} é R${produto['preco']}")
            print("-------------------------------------------------------------------------------------------")
            return
    print("Produto não encontrado.")

def main():
    produtos = []  # Lista de dicionários para armazenar os produtos
    while True:
        print("\n=========== MENU ==============")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            inserir_produto(produtos)
        elif opcao == '2':
            excluir_produto(produtos)
        elif opcao == '3':
            listar_produtos(produtos)
        elif opcao == '4':
            consultar_preco(produtos)
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
