# Avaliação Sprint 1

## Salvando usuarios a partir da API do github
Nesse Projeto foi utilizado algumas libs para o desenvolvimento do mesmo:

- pymongo
- requests
- pprint
- json
- VueJS
- CORS
- Express

![frontend](https://user-images.githubusercontent.com/66642358/117690531-53d87100-b191-11eb-86f9-1c2dc9f73c0b.png)
![Screenshot_2021-05-10_13-13-05](https://user-images.githubusercontent.com/66642358/117690695-82564c00-b191-11eb-95fc-7748b3f0a175.png)


### pymongo
O pymongo foi utilizado para poder estabelecer uma conexão com o banco de dados mongoDB e poder manipular a coleção

### requests
Requests foi utilizado para fazer a requisição para API e retornar as informações de resposta 

### JSON
A lib JSON foi utilizada para poder pegar essa resposta da API e transforma-la em JSON

### PPRINT
Já o pprint foi utilizado para consumir os dados armazenados no banco, mostrando ao usuario todas as informações salvar no mesmo

### VueJS
Foi utilizado para fazer a parte do frontend, recebendo as informacoes da api criada para se comunicar com o banco de dados

### Express
Utilizei para criar a rota de comunicação entre o banco e a aplicação

### CORS
Cors foi uma maneira de resolver o problema de conexao bloqueada pelo fato da requisição estar batendo em mais de uma rota, no caso a 3000 e a 27017

Leonardo Freire Russi
