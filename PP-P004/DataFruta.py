
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False
    
class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos na lista de nomes? "))
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        try:
            sorted_lista = sorted(self.__lista)
            tamanho = len(sorted_lista)
            if tamanho % 2 == 0:
                meio1 = sorted_lista[tamanho // 2 - 1]
                meio2 = sorted_lista[tamanho // 2]
                mediana = f"{meio1} e {meio2}"
            else:
                mediana = sorted_lista[tamanho // 2]
            print("Mediana:", mediana)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de nomes sejam strings.")

    def mostraMenor(self):
        print("Menor elemento:", min(self.__lista))

    def mostraMaior(self):
        print("Maior elemento:", max(self.__lista))

    def __str__(self):
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos na lista de datas? "))
        for _ in range(num_elementos):
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            nova_data = Data(dia, mes, ano)
            self.__lista.append(nova_data)

    
    def mostraMediana(self):
        try:
            sorted_lista = sorted(self.__lista, key=lambda data: (data.ano, data.mes, data.dia))
            tamanho = len(sorted_lista)
            if tamanho % 2 == 0:
                meio1 = sorted_lista[tamanho // 2 - 1]
                meio2 = sorted_lista[tamanho // 2]
                mediana = f"{meio1} e {meio2}"
            else:
                mediana = sorted_lista[tamanho // 2]
            print("Mediana:", mediana)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos Data.")
     
    def mostraMenor(self):
        try:
            menor_data = min(self.__lista, key=lambda data: (data.ano, data.mes, data.dia))
            print("Menor data:", menor_data)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos Data.")
    
    def mostraMaior(self):
        try:
            maior_data = max(self.__lista, key=lambda data: (data.ano, data.mes, data.dia))
            print("Maior data:", maior_data)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos Data.")
    
    def __str__(self):
        return str(self.__lista)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos na lista de salários? "))
        for _ in range(num_elementos):
            salario = float(input("Salário: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        try:
            sorted_lista = sorted(self.__lista)
            tamanho = len(sorted_lista)
            if tamanho % 2 == 0:
                mediana = (float(sorted_lista[tamanho // 2 - 1]) + float(sorted_lista[tamanho // 2])) / 2
            else:
                mediana = float(sorted_lista[tamanho // 2])
            print("Mediana:", mediana)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de salários sejam números.")

    def mostraMenor(self):
        try:
            menor_salario = min(self.__lista)
            print("Menor salário:", menor_salario)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de salários sejam números.")

    def mostraMaior(self):
        try:
            maior_salario = max(self.__lista)
            print("Maior salário:", maior_salario)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de salários sejam números.")
    
    def __str__(self):
        return str(self.__lista)

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        num_elementos = int(input("Quantos elementos na lista de idades? "))
        for _ in range(num_elementos):
            idade = int(input("Idade: "))
            self.__lista.append(idade)
    
    def mostraMediana(self):
        try:
            sorted_lista = sorted(self.__lista)
            tamanho = len(sorted_lista)
            if tamanho % 2 == 0:
                mediana = (sorted_lista[tamanho // 2 - 1] + sorted_lista[tamanho // 2]) / 2
            else:
                mediana = sorted_lista[tamanho // 2]
            print("Mediana:", mediana)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de idades sejam números.")  
    
    def mostraMenor(self):
        try:
            menor_idade = min(self.__lista)
            print("Menor idade:", menor_idade)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de idades sejam números.")
    
    def mostraMaior(self):
        try:
            maior_idade = max(self.__lista)
            print("Maior idade:", maior_idade)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de idades sejam números.")

    def __str__(self):
        return str(self.__lista)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    
    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
