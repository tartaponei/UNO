#BIBLIOTECAS
#------------
import random

#FUNÇÕES
#---------
def escolhe_carta_mesa(descarte):
    i = 0 #inicializador pra teste
    while(i == 0): #enquanto inicializador for 0
        carta_atual = descarte[i].split() #pega a carta de índice i e separa em duas
                   
        if(carta_atual[0] != "+4" and carta_atual[0] != "+2" and carta_atual[0] != "escolhe"): #se a carta não for especial
            return descarte[i] #retorna a carta atual
        i = 1

#VARIAVEIS INICIAIS
#-------------------
baralho = ["+4", "+4", "+4", "+4", "1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho",
"1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo",]


#=============================================================================


#MAIN
#-----------
random.shuffle(baralho) #embaralha as cartas

n = int(input("numero de cartas pra cada jogador: "))

#DISTRIBUIÇÂO DAS CARTAS
cartas_jog = baralho[0:n] #primeiras n cartas separadas pro jog
cartas_bot = baralho[n:n*2] #as próximas n cartas pro bot
descarte = baralho[n*2:-1] #restante das cartas pro descarte

print("JOGADOR: ", cartas_jog)
print("BOT: ", cartas_bot)
print("DESCARTE: ", descarte)

carta_mesa = escolhe_carta_mesa(descarte) #escolhe a carta da mesa

print("CARTA DA MESA: ", carta_mesa)

#EXCLUI A CARTA DA MESA DO DESCARTE
i = 0 #inicializador pra teste
while(i == 0): #enquanto o inicializador for0
    if(descarte[i] == carta_mesa): #se a carta atual for a mesma da mesa
        del(descarte[i]) #carta atual é excluída
        i = 1 #inicializador passa a ser 1

print("DESCARTE: ", descarte)
























