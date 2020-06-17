#BIBLIOTECAS
#------------
import random

#FUNÇÕES
#---------
def escolhe_carta_mesa(descarte):
    i = 0 #inicializador pra teste
    j = 0 #indice de contador
    
    while(i == 0): #enquanto inicializador for 0 (carta não for escolhida) 
        carta_atual = descarte[j].split() #pega a carta de índice j e separa em duas
                   
        if(carta_atual[0] != "+4" and carta_atual[0] != "+2" and carta_atual[0] != "escolhe"): #se a carta não for especial
            return descarte[i] #retorna a carta atual
            i = 1 #inicializador fica 1 (carta foi escolhida)
            
        else: #senão
            j = j + 1 #indice j aumenta +1 pra ir pra proxima carta 

#=======

def escolha_carta_bot(cartas_bot, carta_mesa, descarte):
    carta_mesa = carta_mesa.split() #separo tipo e cor da carta da mesa
    
    i = 0 #inicializador pra teste
    j = 0 #indice de contador
    
    while(i == 0 and j < len(cartas_bot)): #enquanto inicializador for 0 (carta não for escolhida) e ainda tiver carta pra analisar
        carta_atual = cartas_bot[j].split() #separa tipo e cor da carta atual

        if(carta_atual[0] == carta_mesa[0] or carta_atual[1] == carta_mesa[1]): #se tipo ou cor da carta atual for igual ao/à da mesa 
            return cartas_bot[j] #retorna carta atual
            carta_jogada_bot(cartas_bot[j]) #carta é excluída da mão
            i = 1 #inicializador fica 1 (carta foi escolhida)

        else: #senão
            j = j + 1 #indice j aumenta +1 pra ir pra proxima carta
            
           #caso de +4 (ver depois)
        """elif(carta_atual[0] == "+4"): #se a carta na mão é +4
            if(carta_mesa[0] == "+4"): #se a carta da mesa é +4
                return cartas_bot[j] #retorna carta atual
            i = 1 #inicializador fica 1 (carta foi escolhida)"""

        if(i == 0): #se nenhuma carta foi escolhida (nenhuma é possível)
            carta_comprada = compra_carta(carta_mesa, descarte) #compra carta

            if(carta_comprada[0] == carta_mesa[0] or carta_comprada[1] == carta_mesa[1]): #se a carta comprada for jogavel
                return carta_comprada #retorna a carta (escolhida)
                carta_comprada_jogada(carta_comprada, descarte) #executa a função de excluir ela do descarte
            else:
                carta_comprada_nao_jogada_bot(carta_comprada) #executa a função de add ela na mão
        

#=======

def carta_jogada_bot(carta):
    global cartas_bot #mao do bot declarada fora da função 
    i, j = 0
    
    while(i == 0):
        if(carta == cartas_bot[j]): #se a carta for a mesma analisada na mão
            del(cartas_bot[j]) #a carta é excluída
            i = 1
        else:
            j = j + 1

#=======

def compra_carta(carta_mesa, descarte):
    carta_comprada = descarte[0] #compra primeira carta do descarte
    return carta_comprada #retorna essa carta

#=======

def carta_comprada_jogada(carta):
    global descarte #descarte declarada fora da função 
    i, j = 0
    
    while(i == 0):
        if(carta == descarte[j]): #se a carta comprada for a mesma analisada no descarte
            del(descarte[j]) #a carta é excluída
            i = 1
            
#=======

def carta_comprada_nao_jogada_bot(carta):
    global cartas_bot

    cartas_bot.append(carta) #add carta comprada à mão do bot


def carta_comprada_nao_jogada_jog(carta):
    global cartas_jog

    cartas_bot.append(carta) #add carta comprada à mão do bot


#VARIAVEIS INICIAIS
#-------------------
baralho = ["+4", "1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho",
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
print("\n")

carta_mesa = escolhe_carta_mesa(descarte) #escolhe a carta da mesa

print("CARTA DA MESA: ", carta_mesa)

#EXCLUI A CARTA DA MESA DO DESCARTE
i = 0 #inicializador pra teste
while(i == 0): #enquanto o inicializador for0
    if(descarte[i] == carta_mesa): #se a carta atual for a mesma da mesa
        del(descarte[i]) #carta atual é excluída
        i = 1 #inicializador passa a ser 1

print("DESCARTE: ", descarte)

#DECIDE QUEM COMEÇA (depois faço)

#BOT COMEÇA
#while(cartas_jog > 0 and cartas_bot > 0): #enquanto os dois ainda tiverem cartas na mão
escolha = escolha_carta_bot(cartas_bot, carta_mesa, descarte)

print("CARTA ESCOLHIDA PELO BOT: ", escolha)
print("BOT: ", cartas_bot)
print("DESCARTE: ", descarte)

carta_mesa = escolha
print("CARTA DA MESA: ", carta_mesa)





















