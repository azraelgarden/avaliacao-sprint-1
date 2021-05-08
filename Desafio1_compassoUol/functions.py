# importando a Biblioteca 'requests' para acessar a api
import requests
# importando a Biblioteca pymongo para acessar o mongodb
import pymongo

# conectando ao servidor
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# conectando ao banco
mydb = myclient["SW_FAVORITES"]
print('Conexão estabelecida!')
# cria coleção
mycol = mydb["FAVORITES"]

# lista de menu
opcoes = ['do Filme', 'da Pessoa', 'do Planeta',
          'da Espécie', 'da Nave', 'do Veículo', 'ver Favoritos', 'Sair']
# lista de opções da API
options = ['films', 'people', 'planets',
           'species', 'starships', 'vehicles', 'exit']

# cria um menu de opções


def menu():
    print('Digite uma escolha para consulta:')
    for i in opcoes:
        print(f'[{opcoes.index(i)+1}] - Para escolha {i}')


# metodo de input e verificação de dados
def choices():
    # definindo nome de usuário
    user = str(input('Bem vindo, seja você! Qual seu nome?:\n ')).capitalize()

    while True:
        # para validar os inputs
        try:
            menu()
            opt = int(input(''))
            # verifica se está dentro de um range válido para a aplicação
            while opt > len(opcoes) or opt < 1:
                # caso fora do range, retorna com menu e input
                menu()
                opt = int(input('Opção fora do Range! Escolha outra opção! \n'))
        # validando se é opção válida
        except ValueError:
            print('Opção INVÁLIDA! Escolha outra opção\n')
        else:
            # visualiza opção de Favoritos
            if opt == (len(opcoes) - 1):
                unique_favorite = str(
                    input('Deseja visualizar os favoritos de um Usuários específico?\n[S]?\n')).upper()
                # visualiza apenas um usuário em específico
                if unique_favorite == 'S':
                    user_check = str(input('Digite o nome do usuário: \n'))
                    user_querry = {'Usuário': user_check}
                    favorites_search = mycol.find(user_querry)
                    for x in favorites_search:
                        print(x)
                    print('')
                else:
                    # visualiza todos os inputs
                    for x in mycol.find():
                        print(x)
                    print('')
            elif opt != len(opcoes):
                # input dos ids
                choice_id = input(f'Digite o id {opcoes[opt-1]} \n')

                # request na API, passando o ID escolhido
                sw_info = requests.get(
                    f'https://swapi.dev/api/{options[opt-1]}/{choice_id}/')

                # convertendo para string, para fazer a validação se o dado está presente na API
                sw_info_toString = str(sw_info)
                if sw_info_toString == '<Response [404]>':
                    print('Dados não encontrados\n')
                else:
                    # formatando as informações do id escolhido em json
                    choice_id = sw_info.json()

                    # caso a opção for 1, deve-se usar "title" para busca na API
                    if opt == 1:
                        opt_name = choice_id["title"]
                        print(f'"Nome" : {opt_name}')
                    # caso contrário, usar "name"
                    else:
                        opt_name = choice_id["name"]
                        print(f'"Nome" : {opt_name}')

                    # escolha de inserção
                    inserir = str(
                        input('Deseja inserir o valor como favoritos?\n[S]?\n')).upper()
                    # insere o valor
                    if inserir[0] == 'S':
                        # define a variável a ser inserida no banco
                        sw_dict = {'Usuário': user, options[opt-1]: opt_name}
                        # insere valor no banco, em um novo ID
                        mycol.insert_one(sw_dict)
                        print('Valor Inserido, Jovem Padawan!\n')

            #[6] - Sair
            else:
                print('Que a Força esteja com você!')
                break
