def carregar_dados_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = [linha.strip().split(',') for linha in arquivo]
        return [
            {
                'nome': linha[0],
                'sobrenome': linha[1],
                'ano_nascimento': int(linha[2]),
                'rg': linha[3],
                'ano_admissao': int(linha[4]),
                'salario': float(linha[5])
            }
            for linha in dados
        ]
    except FileNotFoundError:
        return []


def salvar_dados_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        for empregado in dados:
            linha = (
                f"{empregado['nome']},{empregado['sobrenome']},"
                f"{empregado['ano_nascimento']},{empregado['rg']},"
                f"{empregado['ano_admissao']},{empregado['salario']:.2f}\n"
            )
            arquivo.write(linha)


def reajustar_salarios_dez_porcento(empresa):
    for empregado in empresa:
        empregado['salario'] *= 1.1


def listar_empregados(empresa):
    print("\nLista de empregados:")
    for i, empregado in enumerate(empresa, 1):
        print(
            f"{i}. Nome: {empregado['nome']} {empregado['sobrenome']}, "
            f"Ano de Nascimento: {empregado['ano_nascimento']}, "
            f"RG: {empregado['rg']}, Ano de Admissão: {empregado['ano_admissao']}, "
            f"Salário: R${empregado['salario']:.2f}"
        )


def main():
    nome_arquivo = "empregados.txt"
    empresa = carregar_dados_arquivo(nome_arquivo)

    while True:
        print("Empresa - Menu:")
        print("1. Listar empregados")
        print("2. Reajustar salários em 10%")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_empregados(empresa)
        elif opcao == '2':
            reajustar_salarios_dez_porcento(empresa)
            print("Salários reajustados em 10%.")
        elif opcao == '0':
            print("Finalizado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

        salvar_dados_arquivo(nome_arquivo, empresa)
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
