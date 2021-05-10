# Avaliação Sprint 1

## Escopo
- A aplicação acessa a API pública "Dog Facts" (https://kinduff.github.io/dog-api/), que possui "fatos" aleatórios sobre cães, por meio de um script Python
- Após acessar a API, o "fato" apresentado será exibido na tela e armazenado em uma variável
- O valor da variável (o fato) é enviado para uma base de dados local MongoDB, que passa a ser alimentado com os "fatos" a cada execução do script
- Por fim, a aplicação exibe em tela todos os "fatos" lidos e armazenados na base de dados

## Recursos técnicos utilizados
- Linguagem Python fazendo uso das seguintes bibliotecas:
  - Requests: Acessar e consumir dados de API's
  - Json: Transmitir dados entre servidores e aplicações, baseado em Java Script
  - Pymongo: Interagir com bases de dados hospedadas em MongoDB
- MongoDB: Gerenciador de base de dados utilizado, instalado localmente

## Entrega
- Script simples, com boa interação com o usuário por meio de mensagens na tela
- Acesso e conexão em API simples e pública
- Atribuição de conteúdo obtido pelo consumo da API a variavel
- Acesso a base de dados MongoDB local, com gravação de dados
- Apresentação de todos os dados da base de dados na tela da aplicação

## Lições aprendidas
- Sempre se atentar a instalar bibliotecas do Python no ambiente virtual correto
- Atentar se o banco de dados está hospedado em Cloud ou localmente, pois apesar da facilidade de se criar e hospedar o banco MongoDB na nuvem, a maioria dos tutoriais apresentam sintaxe para a conexão em base de dados local
- Os principais tutoriais e demais fontes de conteúdo para o tema estão em lingua inglesa


