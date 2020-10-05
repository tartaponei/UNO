#BIBLIOTECAS
#------------
import random

#VARIAVEIS INICIAIS
#-------------------
#"+4 coringa", "+4 coringa", "+4 coringa", "+4 coringa", 
BARALHO = ["1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", 
"1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo",
"1 azul", "2 azul", "3 azul", "4 azul", "5 azul", "6 azul", "7 azul", "8 azul", "9 azul",
"1 verde", "2 verde", "3 verde", "4 verde", "5 verde", "6 verde", "7 verde", "8 verde", "9 verde"]

#CLASSES
#-----------
class Mesa():
    carta = ""
    def __init__(self, descarte):
        self.descarte = descarte

    def escolhe_carta_mesa(self):
        i = 0 #inicializador pra teste
        while i == 0: #enquanto inicializador for 0
            for p in range(len(self.descarte)):
                carta_atual = self.descarte[p].split() #pega a carta de índice p e separa em duas (número / cor)
                        
                if carta_atual[0] != "+4": #se a carta não for especial
                    i = 1
                    return self.descarte[p] #retorna a carta atual

    def excluir_carta_descarte(self, carta):
        if self.descarte[0] == carta: #se a carta atual for a mesma que tem que excluir
            self.descarte.pop(0) #carta excluída do baralho

class Jogador(): #pai de bot
    def __init__(self, cartas):
        self.cartas = cartas

    def vez(self, carta_mesa, descarte):
        carta = "errada" #carta inicialmente sendo errada
        e = "ab" #iniciada assim pra entrar no if a primeira vez

        print("\nSUA VEZ DE JOGAR, escolha sua carta de acordo com o índice (começando do 0):")
        print("SEU BARALHO: ", self.cartas)
        print("SE QUISER COMPRAR UMA CARTA, DIGITE 'comprar':")

        while len(e) > 1 and e != "comprar": #se algo inválido for digitado
            e = input("SUA ESCOLHA: ") #jogador escolhe o índice da carta ou escolhe comprar

        print("\n====================================================")

        if e == "comprar": #se o jogado escolher comprar
            return self.comprar_carta(descarte, carta_mesa) #executar função de comprar carta

        else:
            escolha = int(e) #índice da carta

            while carta == "errada": #enquanto a carta for errada
                carta_certa = self.carta_possivel(self.cartas, escolha, carta_mesa) #executa a função pra ver se a carta é certa

                if carta_certa == False: #se não for certa
                    print("\nVOCÊ ESCOLHEU", self.cartas[escolha])
                    print("Essa carta não pode ser escolhida. ESCOLHA OUTRA!")
                    print(self.cartas)
                    escolha = int(input("")) #jogador escolhe outra
                else:
                    #print("Essa carta pode ser escolhida")
                    carta = "certa"
                    carta_escolhida = self.cartas[escolha]
                    print("\nVOCÊ ESCOLHEU", carta_escolhida)

                    for i in range(len(self.cartas)):
                        if self.cartas[i] == carta_escolhida: #se a carta atual for a mesma que ele escolheu
                            self.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog
                            break

                    return carta_escolhida #retorna a carta que ele escolheu

    def carta_possivel(self, cartas, indice, carta_mesa):
        carta = self.cartas[indice].split() #pega a carta escolhida e separa em duas (numero / cor)
        #print(carta)
        carta_mesa = carta_mesa.split() #separa a carta da mesa em duas (numero / cor)

        if carta[0] == carta_mesa[0] or carta[1] == carta_mesa[1]: #se os números ou as cores forem iguais
            return True
        else:
            return False

    def comprar_carta(self, descarte, carta_mesa):
        carta_comprada = descarte[0] #pega a primeira carta do descarte
        print("\nCARTA COMPRADA: ", carta_comprada)

        carta_comprada_s = carta_comprada.split() #separa em numero/cor
        carta_mesa_s = carta_mesa.split() #separa em numero/cor

        if carta_comprada_s[0] == carta_mesa_s[0] or carta_comprada_s[1] == carta_mesa_s[1]: #se for jogável
            print("CARTA COMPRADA FOI JOGADA")
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_comprada #retorna a carta comprada
        else:
            print("\nCARTA COMPRADA NÃO PODE SER JOGADA\nPORQUE A CARTA DA MESA É {}\nA CARTA COMPRADA FOI ADD AO SEU BARALHO" .format(carta_mesa))
            self.cartas.append(carta_comprada) #carta comprada é adicionada ao baralho do jogador
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_mesa #retorna a carta da mesa (carta da mesa não muda)


class Bot(Jogador):
    def __init__(self, cartas):
        super().__init__(cartas) #pega cartas do mesmo jeito que player
        self.carta_possivel
        self.vez
        self.comprar_carta

    def vez(self, carta_mesa, descarte):
        print("\n====================================================\n\nVEZ DA CPU")
        print(self.cartas)
        
        carta_foi_escolhida = False
        for i in range(len(self.cartas)): #corre o baralho do bot (primeira carta possível será a escolhida)
            carta_certa = self.carta_possivel(self.cartas, i, carta_mesa) #executa a função pra ver se a carta é certa
            #print(carta_certa)
            if carta_certa == True: #se a carta for possível de ser jogada
                carta_escolhida = self.cartas[i]
                print("O BOT ESCOLHEU", carta_escolhida)
                carta_foi_escolhida = True

                for i in range(len(self.cartas)):
                    if self.cartas[i] == carta_escolhida: #se a carta atual for a mesma que ele escolheu
                        self.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog
                        break

                return carta_escolhida #retorna a carta escolhida

        if carta_foi_escolhida == False: #se nenhuma carta tiver sido escolhida
            return self.comprar_carta(descarte, carta_mesa) #executar compra de carta

    def comprar_carta(self, descarte, carta_mesa):
        carta_comprada = descarte[0] #pega a primeira carta do descarte
        print("\nCARTA COMPRADA PELO BOT: ", carta_comprada)

        carta_comprada_s = carta_comprada.split() #separa em numero/cor
        carta_mesa_s = carta_mesa.split() #separa em numero/cor

        if carta_comprada_s[0] == carta_mesa_s[0] or carta_comprada_s[1] == carta_mesa_s[1]: #se for jogável
            print("BOT JOGOU A CARTA")
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_comprada #retorna a carta comprada
        else:
            print("A CARTA NÃO PODE SER JOGADA E O BOT NÃO A JOGOU")
            self.cartas.append(carta_comprada)
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_mesa #retorna a carta da mesa (carta da mesa não muda)

#MAIN
#-----------
random.shuffle(BARALHO) #embaralha as cartas

n = int(input("NÚMERO DE CARTAS PRA CADA JOGADOR: "))

#---DISTRIBUIÇÂO DAS CARTAS---
jog = Jogador(BARALHO[0:n]) #primeiras n cartas separadas pro jog
bot = Bot(BARALHO[n:n*2]) #as próximas n cartas pro bot

descarte = BARALHO[n*2:-1] #restante das cartas pro descarte

print("\nJOGADOR:", jog.cartas)
print("BOT:", bot.cartas)

#---ESCOLHE A CARTA DA MESA---
mesa = Mesa(descarte)
mesa.carta = mesa.escolhe_carta_mesa() #escolhe a carta da mesa

print("\nCARTA DA MESA:", mesa.carta)

#---EXCLUI A CARTA DA MESA DO DESCARTE---
i = 0 #inicializador pra teste
while i == 0: #enquanto o inicializador for0
    if mesa.descarte[i] == mesa.carta: #se a carta atual for a mesma da mesa
        del(mesa.descarte[i]) #carta atual é excluída
        i = 1 #inicializador passa a ser 1

print("DESCARTE:", mesa.descarte)

#---PRIMEIRA RODADA---
quem_joga = random.randint(0, 1)

#---CONTINUAÇÃO DO JOGO---
while (len(jog.cartas) > 0 and len(bot.cartas) > 0): #enquanto nenhum dos dois bater
    if quem_joga == 0: #se quem jogou antes foi o jogador
        #---VEZ DO BOT---
        mesa.carta = bot.vez(mesa.carta, mesa.descarte)

        print("\nBARALHO ATUALIZADO DO BOT:", bot.cartas)
        print("\nNOVA CARTA DA MESA:", mesa.carta)

        if len(bot.cartas) == 1: #caso tenha uma carta
            print("\nBOT DISSE UNO!!")

        quem_joga = 1 #próximo a jogar é o jogador

    else:
        #---VEZ DO JOGADOR---
        mesa.carta = jog.vez(mesa.carta, mesa.descarte) #carta da mesa vira a que foi escolhida pelo jog

        print("\nSEU BARALHO ATUALIZADO:", jog.cartas)
        print("\nNOVA CARTA DA MESA:", mesa.carta)

        if len(jog.cartas) == 1: #caso tenha uma carta
            print("\nVOCÊ DISSE UNO!!")

        quem_joga = 0 #próximo a jogar é o bot

if len(jog.cartas) == 0:
    vencedor = "VOCÊ"
else:
    vencedor = "BOT"

print("\n====================================================\n{} VENCEU, PARABÉNS!!" .format(vencedor))
print("\n----->FIM DO JOGO!! :)<-----")