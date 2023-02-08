Blackjack em Python

O código define quatro classes:

Card representa uma carta individual, com atributos suit (naipe) e rank (valor).
O método __str__ retorna a representação da carta como uma string.
Deck representa um baralho, com uma lista de cartas cards. 
O método __init__ inicializa o baralho com uma lista de cartas com base em quatro naipes e valores de cartas. 
O método shuffle embaralha as cartas usando o módulo random, e o método deal remove e retorna uma quantidade especificada de cartas.
Hand representa uma mão de cartas, com atributos cards (uma lista de cartas), value (o valor da mão), e dealer (uma flag indicando se esta mão é da casa). 
O método add_card adiciona cartas a mão, o método calculate_value calcula o valor total da mão, considerando se há um ás na mão, o método get_value retorna o valor da mão, o método is_blackjack retorna se a mão tem um valor de 21, e o método display exibe a mão na tela.
Game representa a instância do jogo, com o método play que contém a lógica do jogo, pedindo ao jogador quantos jogos eles desejam jogar, criando um baralho, distribuindo cartas para o jogador e para a casa, e realizando a lógica do jogo (hit ou stand) até chegar ao fim do jogo. 
O método check_winner verifica se há um vencedor no final do jogo.
