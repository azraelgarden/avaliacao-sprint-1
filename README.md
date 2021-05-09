# Avaliação Sprint 1
<p align="center"><img src = "https://live.staticflickr.com/1951/30234801997_86f8232201_b.jpg"></p>

## 🚀 SPACEX API - Dados dos foguetes
- Todos os dados serão capturados através da API da [SpaceX](https://www.spacex.com/);
- [GitHub da SpaceX](https://github.com/r-spacex/SpaceX-API) com a documentação;

## 🗒 Descrição do projeto
A ideia deste projeto é capturar os dados através de uma API da SpaceX, utilizando Python e OOP, inserir no banco MongoDB, e fazer uma consulta inteligente.

## 🔎 Consultas feitas
- Nome da empresa
- Fundador da empresa
- Ano de nascimento da empresa
- Valor da empresa
- Localização da empresa
- Porcentagem de lançamentos bem sucedidos
- O launchpad mais utilizado
- A localidade do launchpad mais utilizado
- O percentual de utilização do launchpad
- Nome dos foguetes
- Custos dos foguetes
- Nome dos foguetes versus Custos dos foguetes
- Tipo do motor dos foguetes
- Layout dos motores
- Custo por Voo versus Quantidade de combustível
- Custo por Voo versus Peso da Dragon2

## 🛠 Tecnologias 
- Python3
- MongoDB
- API da SpaceX

## 📈 Fluxo de trabalho
- 1. Capturar os dados da API
- 2. Inserir no banco MongoDB
- 3. Visualizar esses dados no Python3

## 📁 Classes e funções
- **Database**: <br>
-- configurar database - __init __(self, hostname, db) <br>
-- criar collection - criarCollection(self, collection) <br>
-- inserir um registro - inserirUmRegistro(self, query) <br>
-- inserir vários registros - inserirVariosRegistros(self, query) <br>
-- achar um registro - acharUm(self, query) <br>
-- achar vários registros - acharVariosSemQuery(self) <br>
- **API**: <br>
-- configurar API - __init __(self) <br>
-- retornar lista com informações da API - retornaLista(self, url) <br>



## 📣 Disclaimer
- Não estarei utilizando a biblioteca SpaceX-Py para produzir os requests!

## 👨‍🚀 Autor

 <b>[João Victor Palhares Barbosa](https://github.com/vicpb)</b>
