#BIBLIOTECAS
#------------
import random

#VARIAVEIS INICIAIS
#-------------------
baralho = ["+4 coringa", "+4 coringa", "+4 coringa", "+4 coringa", "1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", "1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo",]

#FUNÇÕES
#---------
def escolhe_carta_mesa(descarte):
    i = 0 #inicializador pra teste
    while i == 0: #enquanto inicializador for 0
        for p in range(len(descarte)):
            carta_atual = descarte[p].split() #pega a carta de índice p e separa em duas (número / cor)
                    
            if carta_atual[0] != "+4": #se a carta não for especial
                return descarte[p] #retorna a carta atual
                i = 1

def carta_possivel(mao, indice, carta_mesa):
    carta = mao[indice].split() #pega a carta escolhida e separa em duas (numero / cor)
    #print(carta)
    carta_mesa = carta_mesa.split() #separa a carta da mesa em duas (numero / cor)

    if carta[0] == carta_mesa[0] or carta[1] == carta_mesa[1]: #se os números ou as cores forem iguais
        return True
    else:
        return False

def vez_jogador(cartas):
    carta = "errada" #carta inicialmente sendo errada
    print("\nSUA VEZ DE JOGAR, escolha sua carta de acordo com o índice (começando do 0):")
    print(cartas)
    escolha = int(input("")) #jogador escolhe o índice da carta

    while carta == "errada": #enquanto a carta for errada
        carta_certa = carta_possivel(cartas_jog, escolha, carta_mesa) #executa a função pra ver se a carta é certa

        if carta_certa == False: #se não for certa
            print("Essa carta não pode ser escolhida. ESCOLHA OUTRA!")
            print(cartas)
            escolha = int(input("")) #jogador escolhe outra
        else:
            #print("Essa carta pode ser escolhida")
            carta = "certa"
            print("VOCÊ ESCOLHEU", cartas[escolha])
            return cartas[escolha] #retorna a carta que ele escolheu

def vez_bot(cartas):
    print("\nVEZ DA CPU")
    print(cartas)
    
    for i in range(len(cartas)): #corre o baralho do bot (primeira carta possível será a escolhida)
        carta_certa = carta_possivel(cartas, i, carta_mesa) #executa a função pra ver se a carta é certa

        if carta_certa == True: #se a carta for possível de ser jogada
            print("O CPU ESCOLHEU", cartas[i])
            return cartas[i] #retorna a carta escolhida

#===================================================================================================


#MAIN
#-----------
random.shuffle(baralho) #embaralha as cartas

n = int(input("numero de cartas pra cada jogador: "))

#---DISTRIBUIÇÂO DAS CARTAS---
cartas_jog = baralho[0:n] #primeiras n cartas separadas pro jog
cartas_bot = baralho[n:n*2] #as próximas n cartas pro bot
descarte = baralho[n*2:-1] #restante das cartas pro descarte

print("JOGADOR:", cartas_jog)
print("BOT:", cartas_bot)
print("DESCARTE:", descarte)

#--ESCOLHE A CARTA DA MESA

carta_mesa = escolhe_carta_mesa(descarte) #escolhe a carta da mesa

print("\nCARTA DA MESA:", carta_mesa)

#---EXCLUI A CARTA DA MESA DO DESCARTE---
i = 0 #inicializador pra teste
while i == 0: #enquanto o inicializador for0
    if descarte[i] == carta_mesa: #se a carta atual for a mesma da mesa
        del(descarte[i]) #carta atual é excluída
        i = 1 #inicializador passa a ser 1

#print("DESCARTE: ", descarte)

#---VEZ DO JOGADOR---
carta_mesa = vez_jogador(cartas_jog) #carta da mesa vira a que foi escolhida pelo jog

for i in range(len(cartas_jog)-1):
    if cartas_jog[i] == carta_mesa: #se a carta atual for a mesma que ele escolheu
        cartas_jog.pop(i) #exclui carta escolhida pra mesa do baralho do jog

print("\nSEU BARALHO ATUALIZADO:", cartas_jog)
print("\nNOVA CARTA DA MESA:", carta_mesa)

#---VEZ DO BOT---
carta_mesa = vez_bot(cartas_bot)

for i in range(len(cartas_bot)-1):
    if cartas_bot[i] == carta_mesa: #se a carta atual for a mesma que o bot escolheu
        cartas_bot.pop(i) #exclui carta escolhida pra mesa do baralho do bot

print("\nBARALHO ATUALIZADO DO BOT:", cartas_jog)
print("\nNOVA CARTA DA MESA:", carta_mesa)