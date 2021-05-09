# Consumindo a API do YouTube
Esse projeto tem como objetivo consumir a API do YouTube e armazenar o resultado no banco de dados mongo.

## Pré requisitos
* Python3
* pip
* Mongo DB ()
* pymongo
* Sua IDE/Editor de texto favorito

## Obtendo uma chave da API do YouTube

### Criando um projeto no google cloud

link: https://cloud.google.com

* Vá até à página da Google cloud e no canto superior direito, clique na opção Console;


* No canto superior, vai haver uma opção para selecionar ou criar um projeto do Google Cloud;

* Após criar um projeto, no menu do canto esquerdo, selecione APIs e serviços e depois Credenciais;

* Nessa página, terá uma opção de criar uma credencial, nessa opção, deve selecionar Chave de API. Essa opção irá gerar uma chave de API para ser usada em seu projeto.


### Validando a Chave de API

* Selecione a opção de biblioteca no canto esquerdo da página e no campo de busca que se abrir, digite YouTube;

* Dentre as opções que aparecer, selecione YouTube Data API v3 e clique em habilitar para poder ter acesso à API.

## Criando arquivo de configuração

* Crie um arquivo na raiz do projeto chamado config.ini seguindo a estrutura abaixo, apenas modificando o que for necessário.

```ini
[YOUTUBE_API]
apiKey = <<Aqui vai a sua chave gerada do google cloud>>
url = https://www.googleapis.com/youtube/v3/search
```

## Rodando o projeto

* O primeiro passo é instalar o pymongo, caso não tenha instalado ainda, pode fazer isso executando o seguindo comando

```sh
python -m pip install pymongo
```
* A biblioteca requests é responsável por enviar requisições HTTP com o Python, caso não você não a tenha instalado, basta executar o comando no terminal:

```sh
pip install requests
```

* Finalmente, basta rodar o projeto

```sh
python main.py
```

# Aprendendo com o código

Aqui vamos falar um pouco sobre o conhecimento necessário para entender o código.

## Consumindo a API com o Python 3

### Requisição HTTP utilizando o método GET

* O primeiro passo é fazer a importação do request no nosso código: 
```py
import requests
```
* Após isso, vamos criar uma variável para guardar a nossa chave da API, para podermos utilizá-la de uma maneira mais fácil

```py
# A chave de API não deve ser compartilhada
key = "SUA CHAVE DE API"
```

* Para que possamos aos dados da API, precisamos utilizar da biblioteca requests para enviar uma requisição get

```py
request = requests.get()
```
* Dentro do nosso get, vamos passar dois parâmetros, a url base que processa dados da API, e a chave de API. Como estamos lidando com dados JSON, temos que passar um decodificador json.

```py
# O parametro key recebe como valor a nossa variavel que criamos para armazenar a chave de API
request = requests.get(
    'https://www.googleapis.com/youtube/v3/search',
    params={'key': key}
).json()
```

### Buscando resultados da API com o python

Para buscar resultados da API do youtube com o python, temos que passar mais alguns parâmetros.

* O primeiro parâmetro é o **part**, que especifica uma lista separada por vírgulas de uma ou mais propriedades de recurso search. Vamos passar a propriedade **snippet** que através dela podemos identificar o título, descrição e entre outros resultados.

```py
request = requests.get(
    'https://www.googleapis.com/youtube/v3/search',
    params={'key': key, 'part': 'snippet'}
).json()
```

* O próximo parâmetro, é o **q**, que especifica o termo de consulta a ser pesquisado.
* O valor desse parâmetro é algo que digitamos no search do YouTube. Para ficar mais dinâmico, vamos criar uma váriavel para que possamos digitar o que queremos que receber de resultado da API.

```py
pesquisar = str(input('Qual sua pesquisa?: '))
```

* Agora sim, vamos passar o último parâmetro que iremos utilizar.

```py
request = requests.get(
    'https://www.googleapis.com/youtube/v3/search', 
    params={'key': key, 'part': 'snippet', 'q': pesquisar}
).json()
```

Existe muitos outros parâmetros que podem ser passados, como por exemplo o parâmetro **maxResults**, que irá especificar o número máximo de itens que serão retornados como resultado da pesquisa. Por padrão, o número de itens que é retornado como resultado é 5, mas podemos retornar até 50 itens. Para mais informações, consultar a documentação oficial.

link: https://developers.google.com/youtube/v3/docs/search/list?hl=pt-br

## Armazenando resultados da API no MongoDB
### Pymongo

O MongoDB possui um driver para que possamos fazer a comunicação com o python. Essa comunicação vai nos permitir armazenar dados no mongo e até buscar resultados que ja estão armazenados no mongo.

* Agora vamos fazer a importação do MongoClient.

```py
from pymongo import MongoClient
```

* Agora precisamos conectar o mongo ao host e a porta padrão, para isso vamos criar uma váriavel chamada client e passar o localhost e a porta padrão do servidor do mongo que é **27017**

```py
client = MongoClient("localhost", 27017)
```

Também podemos fazer nossa conexão com o host e a porta do servidor do mongo utilizando uma string de conexão

```py
client = MongoClient("mongodb://localhost:27017/")
```

* Agora para obter um banco de dados, so precisamos criar coleção de dados para que depois seja possível adicionar, excluir e buscar itens dentro do mongo

```py
db = client.YoutubeResultados
```

* Pronto, agora é so fazer os inserts no banco de dados.
```py
db.resultado.insert_many(
    [
        {
            'resultadoBusca' : request
        }
    ]
)
```

* O resultado que irá obter, vai ser um objeto que dentro dele, terá um atributo items, que o valor é um dicionário de 5 objetos. Esses 5 objetos são os resultados de nossa pesquisa na API do YouTube, que trouxe para nós 5 resultados.

* Caso queira que cada resultado encontrado na API execute um insert no banco de dados, é necessário criar um laço de repetição, onde cada resultado será uma variável item e assim executar um insert.

```py
for item in request['items']:
    db.resultados.insert_many(
        [
            {
                'cacheKey': pesquisar,
                'Thumbnail' : item['snippet']['thumbnails']['default']['url'],
                'TituloDoVideo' : item['snippet']['title'],
                'Descricao' : item['snippet']['description'],
                'TituloDoCanal' : item['snippet']['channelTitle']                    
            }
        ]
    )
```

### Checando se já existe dados no mongo

Podemos agora, quando digitarmos o que queremos pesquisar, fazer uma checagem no mongo antes de procurar na API do YouTube. Se já tiver o resultado que queremos no mongo, vamos trazer direto de lá, se não, vamos buscar na API e salvar no mongo em seguida, tudo isso de maneira automática

* Para isso, vamos criar uma nova chave para a nossa coleção, chamada cacheKey. O valor dessa chave nada mais vai ser do que nossa váriavel pesquisar, que criamos anteriormente. Ou seja, supondo que você quer buscar resultados sobre star wars. Essa string vai ficar armazenada como valor da cacheKey.

```py
db.resultados.insert_many(
    [
        {
            'cacheKey': pesquisar,
            'Thumbnail' : item['snippet']['thumbnails']['default']['url'],
            'TituloDoVideo' : item['snippet']['title'],
            'Descricao' : item['snippet']['description'],
            'TituloDoCanal' : item['snippet']['channelTitle']
                        
        }
    ]
)

```

* Agora vamos fazer a busca no mongo. Para isso, vamos criar uma váriavel resultadoDoBanco, que será igual ao método .find() do mongodb, passando como parâmetro para pesquisa, a cacheKey

```py
resultadoDoBanco = db.resultados.find({'cacheKey': pesquisar})
```

* O resultado que vamos obter dessa busca, é um objeto, e dentro dele possui um cursor com vários dados. O cursor é uma ferramenta para iterar os resultados de consulta do MongoDB. Se você printar esse objeto na tela, vai ver vários dados que a coleção do mongo possui.

```py
if resultadoDoBanco.count() > 0:
    for item in resultadoDoBanco:
        print(item)
        
else: 
    request = requests.get(
        'https://www.googleapis.com/youtube/v3/search', 
        params={'key': key, 'part': 'snippet', 'q': pesquisar}).json()
    for item in request['items']:
        
        db.resultados.insert_many(
            [
                {
                    'cacheKey': pesquisar,
                    'Thumbnail' : item['snippet']['thumbnails']['default']['url'],
                    'TituloDoVideo' : item['snippet']['title'],
                    'Descricao' : item['snippet']['description'],
                    'TituloDoCanal' : item['snippet']['channelTitle']
                        
                }
            ]
        )
        print(item)
```