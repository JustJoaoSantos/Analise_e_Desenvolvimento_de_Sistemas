class Paciente:
    # Construtor da classe
    def __init__(self, nome, idade, telefone):
        self.nome = nome 
        self.idade = idade
        self.telefone = telefone 

    # Getters
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_telefone(self):
        return self.telefone
    
def verificarDados(dado, isInt):
    # se o dado for testado como numerico, e o dado inserido for numerico 0-9, retorne true
    if isInt and dado.isnumeric():
        return True
    
    if len(dado) > 3:
        return True

    # se o dado for testado como numerico mas nao ser, retorna false
    # se o dado for testado como str mas for menor que 3 ou null, retorna false
    return False

    

lista_pacientes = {}
op = -1

while op != '0':
    print("="*10 + " Sistema Clínica Vida+ " + "="*10)
    print("Digite a Operacao:")
    print("0 - Para encerrar o programa")
    print("1 - Para cadastrar um paciente")
    print("2 - Ver Estatisticas")
    print("3 - Buscar Paciente")
    print("4 - Listar Pacientes Registrados")
    op = input("> ")


    match op:
        case '0':
            print("Encerrando programa!")

        case '1':
            print("="*10 + " Cadastro de Paciente " + "="*10)
            nome = input("Nome do Paciente: ")
            idade = input("Idade do Paciente: ")
            telefone = input("Telefone do Paciente: ")

            if verificarDados(nome, False) and verificarDados(idade, True) and verificarDados(telefone, False):
                # adiciona dados verificados e validos em uma nova instancia de paciente
                p = Paciente(nome, int(idade), telefone)

                # Verifica se o Paciente Cadastrado ja existe na lista de Pacientes
                if p.get_nome() in lista_pacientes:
                    print("Nome já está em uso, tente outro nome!")
                else:
                    # Se nao existir ele sera adicionado a lista de Pacientes
                    lista_pacientes[p.get_nome()] = p 

                    # Verifica se foi adicionado com sucesso
                    if p.get_nome() in lista_pacientes:
                        print("Cadastro realizado com sucesso!")

                    else:
                        print("Erro Inesperado!")
            else:
                print("Dados inválidos, tente novamente.")

        case '2':
            print()
            print("="*10 + " Estatisticas " + "="*10)

            # se a lista nao estiver vazia
            if len(lista_pacientes) > 0:
                # variaveis para calculo
                soma = 0
                maior = 0
                menor = -1
                menor_nome = ''
                maior_nome = ''

                # iteracao da lista
                for p in lista_pacientes.values():
                    if (menor == -1):
                        menor = p.get_idade()
                        menor_nome = p.get_nome()

                    soma += p.get_idade()

                    if p.get_idade() > maior:
                        maior = p.get_idade()
                        maior_nome = p.get_nome()

                    if p.get_idade() < menor:
                        menor = p.get_idade()
                        menor_nome = p.get_nome()

                print(f"Numero total de Pacientes Cadastrados: {len(lista_pacientes)}")
                print(f"Media de idade dos pacientes cadastrados: {soma / len(lista_pacientes):.2f} anos.")
                print(f"O Paciente Mais velho é {maior_nome} com {maior} anos.")
                print(f"O Paciente Mais novo é {menor_nome} com {menor} anos.\n")
            
            else:
                print("Numero de cadastrados é 0, faca um cadastro primeiro!")


        case '3':
            print("="*10 + " Busca de Pacientes " + "="*10)
            find = False
            busca = str(input("Digite o Nome do paciente a ser pesquisado: ")).lower()
            
            # Percorre lista de pacientes (valores) e se o nome digitado corresponde com um dos nomes existentes na lista, os dados encontrados seram listados
            for p in lista_pacientes.values():
                if busca in p.get_nome().lower():
                    print("Paciente encontrado, Listando Dados")
                    print('-'*15)
                    print(f"Nome: {p.get_nome()}")
                    print(f"Idade: {p.get_idade()}")
                    print(f"Telefone: {p.get_telefone()}")
                    print('-'*15)
                    find = True 

            if not find:
                print("Este nome não foi encontrado no banco de dados, porfavor digite novamente!\n")
            
        case '4':
            print("="*10 + " Lista de Pacientes " + "="*10)
            # percorre e lista todos os dados (valores) da lista (lista_pacientes)
            for nome, data in lista_pacientes.items():
                print(f"Nome: {nome}")
                print(f"Idade: {data.get_idade()}")
                print(f"Telefone: {data.get_telefone()}")
                print('-'*20)
            
        case _:
            print("Operaçao não aceita, tente novamente!")
