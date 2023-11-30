'''
Exercício 2: Pesquisa sobre persistência de dados.
● Este exercício já foi implementado no módulo anterior, utilizando C++.
Vejamos agora como ficaria uma versão feita em Python: Crie um dicionário
para armazenar dados (nome, sobrenome, ano de nascimento, RG, ano de
admissão, salário) de empregados de uma empresa. Leia as informaçõies
sobre os funcionários de um arquivo e guarde numa lista.
○ Faça uma função chamada “Reajusta_dez_porcento( )” que receba
por parâmetro a lista de empregados e atualize o salário de cada
empregado em 10%.
○ Crie um aplicativo para testar a função. Pode reproduzir a estrutura
utilizada no exercício anterior.
'''

# Função para reajustar os salários em 10%
def Reajusta_dez_porcento(lista_funcionarios):
    for funcionario in lista_funcionarios:
        salario_atual = funcionario['salario']
        novo_salario = (salario_atual * 10)/100 # Aumento de 10%
        funcionario['salario'] = round(novo_salario, 2)

# Função para ler dados dos funcionários de um arquivo
def ler_dados_funcionarios(nome_arquivo):
    lista_funcionarios = []
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
            dados = linha.strip().split(';')
            nome, ano_nascimento, rg, ano_admissao, salario = dados
            salario = float(salario)
            funcionario = {
                'nome': nome,
                'ano_nascimento': int(ano_nascimento),
                'rg': rg,
                'ano_admissao': int(ano_admissao),
                'salario': salario
            }
            lista_funcionarios.append(funcionario)
    return lista_funcionarios

# Função para imprimir os dados dos funcionários
def imprimir_funcionarios(lista_funcionarios):
    for funcionario in lista_funcionarios:
        salario_anterior = funcionario['salario']
        novo_salario = salario_anterior * 1.1  # Novo salário após reajuste
        print(f"Nome: {funcionario['nome']}, Salário Anterior: R${salario_anterior}, Salário Atualizado: R${novo_salario}")


def main():
    nome_arquivo = 'PP-P003/funcionarios.txt'  # Arquivo com os dados dos funcionários
    funcionarios = ler_dados_funcionarios(nome_arquivo)

    print("-------------------------------------------------------------------------------------------")
    print("Salários antes e depois do reajuste:")
    print("-------------------------------------------------------------------------------------------\n")
    imprimir_funcionarios(funcionarios)
    print("-------------------------------------------------------------------------------------------\n")

    Reajusta_dez_porcento(funcionarios)

if __name__ == "__main__":
    main()
