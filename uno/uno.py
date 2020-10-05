#BIBLIOTECAS
#------------
import random

#VARIAVEIS INICIAIS
#-------------------
BARALHO = ["+4 coringa", "+4 coringa", "+4 coringa", "+4 coringa", "1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", "1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo",]

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
                    return self.descarte[p] #retorna a carta atual
                    i = 1


class Jogador(): #pai de  bot
    def __init__(self, cartas):
        self.cartas = cartas
        self.numero_cartas = len(cartas)

    def vez(self, carta_mesa, descarte):
        carta = "errada" #carta inicialmente sendo errada

        print("\nSUA VEZ DE JOGAR, escolha sua carta de acordo com o índice (começando do 0):")
        print("SE QUISER COMPRAR UMA CARTA, DIGITE 'comprar':")
        print(self.cartas)
        e = input("") #jogador escolhe o índice da carta ou escolhe comprar

        if e == "comprar":
            carta_comprada = self.comprar_carta(descarte)
            #self.cartas.append(carta_comprada)
            print("CARTA COMPRADA: ", carta_comprada)

            if carta_comprada[0] == carta_mesa[0] or carta_comprada[1] == carta_mesa[1]:
                return carta_comprada
        else:
            escolha = int(e) #jogador escolhe o índice da carta

            while carta == "errada": #enquanto a carta for errada
                carta_certa = self.carta_possivel(self.cartas, escolha, carta_mesa) #executa a função pra ver se a carta é certa

                if carta_certa == False: #se não for certa
                    print("Essa carta não pode ser escolhida. ESCOLHA OUTRA!")
                    print(self.cartas)
                    escolha = int(input("")) #jogador escolhe outra
                else:
                    #print("Essa carta pode ser escolhida")
                    carta = "certa"
                    print("VOCÊ ESCOLHEU", self.cartas[escolha])

                    for i in range(len(self.cartas)-1):
                        if self.cartas[i] == self.cartas[escolha]: #se a carta atual for a mesma que ele escolheu
                            self.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog

                    return self.cartas[escolha] #retorna a carta que ele escolheu

    def carta_possivel(self, cartas, indice, carta_mesa):
        carta = self.cartas[indice].split() #pega a carta escolhida e separa em duas (numero / cor)
        #print(carta)
        carta_mesa = carta_mesa.split() #separa a carta da mesa em duas (numero / cor)

        if carta[0] == carta_mesa[0] or carta[1] == carta_mesa[1]: #se os números ou as cores forem iguais
            return True
        else:
            return False

    def comprar_carta(self, descarte):
        return descarte[0]

class Bot(Jogador):
    def __init__(self, cartas):
        super().__init__(cartas) #pega cartas do mesmo jeito que player
        self.carta_possivel
        self.vez
        self.comprar_carta

    def vez(self, carta_mesa, descarte):
        print("\nVEZ DA CPU")
        print(self.cartas)
        
        for i in range(len(self.cartas)): #corre o baralho do bot (primeira carta possível será a escolhida)
            carta_certa = self.carta_possivel(self.cartas, i, carta_mesa) #executa a função pra ver se a carta é certa

            if carta_certa == True: #se a carta for possível de ser jogada
                print("O CPU ESCOLHEU", self.cartas[i])
                return self.cartas[i] #retorna a carta escolhida

#MAIN
#-----------
random.shuffle(BARALHO) #embaralha as cartas

n = int(input("numero de cartas pra cada jogador: "))

#---DISTRIBUIÇÂO DAS CARTAS---
jog = Jogador(BARALHO[0:n]) #primeiras n cartas separadas pro jog
bot = Bot(BARALHO[n:n*2]) #as próximas n cartas pro bot

descarte = BARALHO[n*2:-1] #restante das cartas pro descarte

print("JOGADOR:", jog.cartas)
print("BOT:", bot.cartas)
#print("DESCARTE:", descarte)

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

#---VEZ DO JOGADOR---
mesa.carta = jog.vez(mesa.carta, mesa.descarte) #carta da mesa vira a que foi escolhida pelo jog

'''for i in range(len(jog.cartas)-1):
    if jog.cartas[i] == mesa.carta: #se a carta atual for a mesma que ele escolheu
        jog.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog'''

print("\nSEU BARALHO ATUALIZADO:", jog.cartas)
print("\nNOVA CARTA DA MESA:", mesa.carta)

#---VEZ DO BOT---
mesa.carta = bot.vez(mesa.carta, mesa.descarte)

for i in range(len(bot.cartas)-1):
    if bot.cartas[i] == mesa.carta: #se a carta atual for a mesma que o bot escolheu
        bot.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do bot

print("\nBARALHO ATUALIZADO DO BOT:", bot.cartas)
print("\nNOVA CARTA DA MESA:", mesa.carta)