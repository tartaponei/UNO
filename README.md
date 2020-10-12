# "UNO"

#### _Meu projeto de tentativa de recriar um jogo de UNO Player vs CPU_



### > Antes de tudo:

- #### Para rodar o projeto você precisa ter a biblioteca `rich` instalada por causa da formatação;

- #### Para ver as cores e formatação exata do terminal, use o novo Windows Terminal (o clássico só tem 8 cores e vai bugar a formatação toda);

- #### Feito em Python 3.8.

  

------



- ### Sobre:

  - Um remake do UNO em uma aplicação simples em terminal formatado, onde você joga contra um "bot", que segue uma prioridade de escolhas (descritas no arquivo `prioridade-jogada.txt`), onde você pode recomeçar as partidas. O placar sempre vai aparecer no início de cada partida, e quem começa a partida é escolhido aleatoriamente.

    

- ### Regras:

  - #### As regras do jogo aqui nesse programa são as seguintes:

    - **Não pode jogar +2 em cima de +2 ou +4 em cima de +4**. Se a carta de +2 ou +4 for jogada, o adversário compra as cartas obrigatoriamente, já está programado assim;
    - **Quem compra as cartas por causa de uma carta +2 ou +4 não joga**, só na próxima rodada;
    - **Por enquanto, é possível jogar uma carta coringa (de escolher cor ou +4) por cima de uma outra carta coringa de escolher cor**. Por exemplo, se o bot joga uma coringa de escolher cor e escolhe a cor azul, eu posso tanto jogar cartas azuis quanto cartas coringas (pretendo mudar essa questão no futuro);
    - **Se uma carta de retorno ou bloqueio for jogada, quem jogou repete a vez** (porque aqui só tem 2 jogadores e usar essas cartas com apenas 2 pessoas só nos dá essa possibilidade);
    - Num jogo normal, caso a pessoa não fale "UNO" ao chegar a 1 carta só, ela é obrigada a comprar acho que 2 cartas. Por enquanto, **aqui o programa fala "UNO" por você e pelo bot automaticamente** (também pretendo mudar isso no futuro);
    - **Você pode "manipular" as rodadas quantas vezes você quiser e puder** (você pode jogar 6 cartas de bloqueio e bater de uma vez, nada te impede sem ser o próprio baralho);
    - **Se uma carta que pode ser jogada for comprada, ela automaticamente é jogada pela programação**. Você, nem o bot, tem a opção de guardar a carta para depois (também pretendo mudar isso no futuro).



