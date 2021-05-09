Análise Exploratória das Expansões de Hearthstone

Autor: Victor Balbino Araujo
Avaliação Compasso

Bibliotecas utilizadas
    requests
    pymongo
    matplotlib.pyplot
    collections
    numpy

Abordagem
    Uso do request para resgatar a informação da url da API;
    Tratamento do JSON;
    Inicialização do Banco de Dados MongoDB utilizando como base o JSON;
    Análise exploratória com matplotlib, Counter e numpy;
    Entrega ao usuário em forma de gráficos e estatística.

A partir da Hearthstone API, esse projeto tem o intuito de realizar uma análise exploratória utilizando a biblioteca matplotlib para tal fornecendo gráficos tanto em barra quanto em linhas de um input do usuário e em alguns casos, análise estatística utilizando a biblioteca numpy.

Primeiramente, o usuário informa se quer visualizar todas as expansões ou apenas uma específica escolhida por ele, após
ele tem a opção de escolher entre uma das informações que ele vai visualizar (custo das cartas, vida das criaturas, ataque das criaturas, raça das criaturas, tipo das cartas e a raridade), após ele irá receber dados como valor mínimo, valor máximo, média, variância, desvio padrão, gráfico de barras analisando a quantidade de cartas daquela seção dentro da expansão ou de todas as expansões, gráfico de linha exibindo a variação da média da seção escolhida.

As funções presentes ajudam a tornar o código mais legível e para ter um controle melhor do que se é feito em cada funcionalidade.
    begin() é apresentado ao usuário primeiro e é quem dá início ao código.

    show_expansions() e show_info() são responsáveis por apresentar o que o usuáio pode selecionar em expansão e em seção, respectivamente.

    choice_global() é chamada caso o usuário queira visualizar determinada seção de todas as expansões presentes.

    choice_one() é chamada caso o usuário queira visualizar apenas uma expansão.

    make_list() responsável por criar uma lista de uma expansão a partir do input do usuário e da busca feita pelo programa na base dados para assim utilizar nos gráficos e análise estatística.

    numpy_statistics() responsável pela amostra das estatísticas citadas, utiliza numpy para facilitar o cálculo, devido a seu enorme poder em trabalhar com operações matemáticas.

    make_bar() responsável por criar gráfico de barras utilizando matplotlib.

    global_list() responsável por criar uma lista global, ou seja, de todas as expansões para se trabalhar nas outras funções.

    global_mean_plot() responsável por criar o gráfico de linhas com todas as expansões, exibindo a média de determinada seção, ajuda a visualizar possíveis mudanças no balanceamento das cartas conforme o tempo.

