O projeto consiste de uma ferramenta que consome os dados da API PokéAPI afim de gerar times de até 6 pokemons, exibir todos os times cadastrados no banco de dados local,
ou simplesmente consultar informações sobre qualquer pokemon.

através de algumas funções da biblioteca request é possivel consumir os dados da API na linguagem python (que foi utilizada no desenvolvimento do projeto)

ao iniciar a aplicação havera um menu inicial com as opções de criar um time, consultar os times existentes, checar a pokedex (checar as informações de um pokemon especifico) e a
opção sair.

começando pela opção da pokedex, nela é utilizado o metodo checar.

o metodo checar é responvael por consumir a API e encontrar os dados do pokemon especificado no imput inicial da função, imprimindo para o usuario os dados nome, id e tipos do
pokemon pesquisado, gerando uma variavel para o nome, que é usado por outros metodos.

a opção de criar time acessa a classe Monta_Time e utiliza varios metodos para criar o time

começando pelo metodo montar, uma lista é criada para armazenar os pokemons do time e logo em seguida uma estrutura for é usada para que sejam adicionados até 6 pokemons na lista,
dentro desta estrutura é chamado o metodo add_pkm, que chama o metodo checar que após obter os dados, guarda o nome do pokemonpesquisado em uma variavel e a envia de volta para o
metodo add_pkm, onde é perguntado se o usuario realmente deseja adicionar o pokemon ao time, caso a resposta seja sim, o nome do pokemon é adicionado a lista do metodo montar,
caso não, o metodo checar é chamado novamente, depois de adicionar um pokemon, é feita uma pergunta se o usuario deseja adicionar outro (permitindo times com menos de 6 pokemon),
quando o limite maximo de 6 é atingido ou o usuario diz que não quer mais adicionar, é impresso o nome do time e a lista gerada no metodo montar, esses dados então são salvos no
mongodb(dentro de uma base criada pelo proprio projeto) atraves dos metodos da biblioteca pymongo, e uma mensagem é exibida indicando o sucesso da operação.

por fim, a opção de consultar os times existentes, que acessa o banco de dados mongo através da função find da biblioteca pymongo, antes desse acesso é perguntado se o usuario
deseja ver todos os times cadastrados ou apenas um, no primeiro caso um acesso é realizado e todos os times gerados são impressos para o usuario, enquanto no segundo caso é 
perguntado o nome do time a ser consultado e atraves de uma query esse time é buscado e exibido também pela função find.

concluindo, a api escolhida veio de uma afinidade com a franquia e a sugestão da api por um dos colegas, embora o projeto seja capaz de realizar tudo que foi solicitado ainda
existe a possibilidades de melhorias futuras, vindo em mente a melhor formatação da exibição dos tipos no metodo checar, que apesar de compreensivel ainda tem um visual bem cru,
com aspectos bem visiveis do arquivo json de onde os dados foram retirados, mas felizmente sendo o unico campo que apresenta tal problema, outra melhoria seria a implantação de
uma nova função no menu principal ou dentro da opção de consulta, que seria a opção de editar times ja existentes. Apesar do choque inicial acredito que o projeto atende as
expectativas, por mais que tenha sido um processo cansativo não houveram grandes impedimentos.
