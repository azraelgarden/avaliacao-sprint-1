  
desafio1_compassoUol
Desafio de consumir API e integrar com MongoDB

Utilizei a bilbioteca de pymongo para utilizar o mongodb. Também utilizei a biblioteca requests para integração e requisição da API. API escolhida foi 'swapi' https://swapi.dev/ ,sendo uma API de Star Wars

O sistema funciona gerando um menu de opções para definir qual a categoria da API será verificada. Depois da escolha, é perguntado qual o ID da categoria deverá ser acessado. Só então, será perguntado se o escolhido deverá subir ao mongodb para uma database de favoritos.

Também pe possível a consulta do que já foi inserido no banco.

Como melhorias: Inclusão de listas na DB, pois nesta versão não será possível incluir mais de um dado de escolha por ID. Melhorias na interface para ficar mais amigável e intuitivo ao usuário.
