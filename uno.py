#BIBLIOTECAS
#------------
import random
from rich.console import Console

#VARIAVEIS INICIAIS
#------------------- 
BARALHO = ["1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", "+2 vermelho", 
"1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo", "+2 amarelo",
"1 azul", "2 azul", "3 azul", "4 azul", "5 azul", "6 azul", "7 azul", "8 azul", "9 azul", "+2 azul",
"1 verde", "2 verde", "3 verde", "4 verde", "5 verde", "6 verde", "7 verde", "8 verde", "9 verde", "+2 verde",

"bloquear vermelho", "bloquear amarelo", "bloquear azul", "bloquear verde",
"retornar vermelho", "retornar amarelo", "retornar azul", "retornar verde",

"escolhe cor", "escolhe cor", "escolhe cor", "escolhe cor", "+4 coringa", "+4 coringa", "+4 coringa", "+4 coringa",

"1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", "+2 vermelho", 
"1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo", "+2 amarelo",
"1 azul", "2 azul", "3 azul", "4 azul", "5 azul", "6 azul", "7 azul", "8 azul", "9 azul", "+2 azul",
"1 verde", "2 verde", "3 verde", "4 verde", "5 verde", "6 verde", "7 verde", "8 verde", "9 verde", "+2 verde",

"bloquear vermelho", "bloquear amarelo", "bloquear azul", "bloquear verde",
"retornar vermelho", "retornar amarelo", "retornar azul", "retornar verde",

"escolhe cor", "escolhe cor", "escolhe cor", "escolhe cor", "+4 coringa", "+4 coringa", "+4 coringa", "+4 coringa"]

#init(autoreset=True) #todas as mudanças de cor vão ser resetadas quando acabar a linha

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
                        
                if carta_atual[0] != "+4" and carta_atual[0] != "+2" and carta_atual[0] != "retornar" and carta_atual[0] != "bloquear" and carta_atual[0] != "escolhe": #se a carta não for especial
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

        console.print("\n====================================================\n\n[bold light_pink3]-->>> SUA VEZ DE JOGAR <<<--[bold light_pink3]\nEscolha sua carta de acordo com o índice (começando do 0):")
        print("SEU BARALHO:", end=' ')
        baralho_colorido(self.cartas) #colocar carta colorida
        print("\nSE QUISER COMPRAR UMA CARTA, DIGITE 'comprar':")

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
                    console.print("\n[bold]VOCÊ ESCOLHEU[/bold]", end=' ')
                    baralho_colorido(self.cartas[escolha]) #colocar carta colorida
                    console.print("Essa carta não pode ser escolhida. [bold]ESCOLHA OUTRA![/bold]")
                    baralho_colorido(self.cartas) #colocar carta colorida
                    escolha = int(input("DIGITE: ")) #jogador escolhe outra
                else:
                    carta = "certa"
                    carta_escolhida = self.cartas[escolha]
                    console.print("\n[bold]VOCÊ ESCOLHEU[/bold]", end=' ')
                    baralho_colorido(self.cartas[escolha]) #colocar carta colorida

                    for i in range(len(self.cartas)):
                        if self.cartas[i] == carta_escolhida: #se a carta atual for a mesma que ele escolheu
                            self.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog
                            break
                    
                    carta_escolhida_s = carta_escolhida.split()

                    if carta_escolhida == "escolhe cor": #se for coringa
                        carta_escolhida = self.escolher_cor(carta_mesa) #executar função de escolher cor

                    elif carta_escolhida_s[0] == "+2":
                        compra_por_carta(2, "jog")
                        carta = self.vez(carta_escolhida, descarte)
                        carta_escolhida = carta
                    
                    elif carta_escolhida_s[0] == "+4":
                        compra_por_carta(4, "jog")
                        carta = self.vez(carta_escolhida, descarte)
                        carta_escolhida = carta

                    return carta_escolhida #retorna a carta que ele escolheu
    
    def carta_possivel(self, cartas, indice, carta_mesa):
        carta = self.cartas[indice].split() #pega a carta escolhida e separa em duas (numero / cor)
        #print(carta)
        carta_mesa = carta_mesa.split() #separa a carta da mesa em duas (numero / cor)

        if carta[0] == carta_mesa[0] or carta[1] == carta_mesa[1] or carta_mesa[0] == "+4" or carta[0] == "+4" or carta[0] == "escolhe": #se os números ou as cores forem iguais ou for carta especial
            return True
        else:
            return False

    def comprar_carta(self, descarte, carta_mesa):
        carta_comprada = descarte[0] #pega a primeira carta do descarte
        console.print("\n[bold]CARTA COMPRADA[/bold]:", end=' ')
        baralho_colorido(carta_comprada) #colocar carta colorida

        carta_comprada_s = carta_comprada.split() #separa em numero/cor
        carta_mesa_s = carta_mesa.split() #separa em numero/cor

        if carta_comprada_s[0] == carta_mesa_s[0] or carta_comprada_s[1] == carta_mesa_s[1] or carta_comprada_s[1] == "cor": #se for jogável
            console.print("[bold]CARTA COMPRADA FOI JOGADA[/bold]")
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte

            if carta_comprada == "escolhe cor": #se for coringa
                carta_comprada = self.escolher_cor(carta_mesa) #executar função de escolher cor

            elif carta_comprada_s[0] == "+2":
                compra_por_carta(2, "jog")

                print("\nVOCÊ JOGOU UM +2")
                console.print("[bold]SUA VEZ DE NOVO[/bold]")
                baralho_colorido(self.cartas) #colocar carta colorida
                escolha = int(input("ESCOLHA A CARTA: ")) #jogador escolhe outra

                carta_certa = self.carta_possivel(self.cartas, escolha, carta_mesa) #executa a função pra ver se a carta é certa

                if carta_certa == False: #se não for certa
                    console.print("\n[bold]VOCÊ ESCOLHEU[/bold]", end=' ')
                    baralho_colorido(self.cartas[escolha]) #colocar carta colorida
                    console.print("Essa carta não pode ser escolhida. [bold]ESCOLHA OUTRA![/bold]")
                    baralho_colorido(self.cartas) #colocar carta colorida
                    escolha = int(input("")) #jogador escolhe outra
                else:
                    carta_comprada = self.cartas[escolha]
                    console.print("\n[bold]VOCÊ ESCOLHEU[/bold]", end=' ')
                    baralho_colorido(self.cartas[escolha]) #colocar carta colorida
            
            elif carta_comprada_s[0] == "+4":
                compra_por_carta(4, "jog")

                print("\nVOCÊ JOGOU UM +4")
                console.print("[bold]SUA VEZ DE NOVO[/bold]")
                baralho_colorido(self.cartas) #colocar carta colorida
                escolha = int(input("ESCOLHA A CARTA: ")) #jogador escolhe outra

                carta_comprada = self.cartas[escolha]

            return carta_comprada #retorna a carta comprada
        else:
            console.print("\nCARTA COMPRADA NÃO PODE SER JOGADA\nPORQUE A CARTA DA MESA É", end = ' ', style="bold")
            baralho_colorido(carta_mesa) 
            console.print("\nA CARTA COMPRADA FOI ADICIONADA AO SEU BARALHO", style="bold")
            self.cartas.append(carta_comprada) #carta comprada é adicionada ao baralho do jogador
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_mesa #retorna a carta da mesa (carta da mesa não muda)

    def escolher_cor(self, carta_mesa):
        console.print("\nVOCÊ JOGOU UMA CARTA CORINGA DE ESCOLHER COR\n\nDIGITE O NÚMERO CORRESPONDENTE À COR:[red]\n1- VERMELHO[/red]\n[yellow]2- AMARELO[/yellow]\n[blue]3- AZUL[/blue]\n[green]4- VERDE[/green]")
        escolha = int(input("DIGITE: "))

        if escolha == 1:
            console.print("\nVOCÊ ESCOLHEU [red]VERMELHO[/red]")
            return "coringa vermelho"
        elif escolha == 2:
            console.print("\nVOCÊ ESCOLHEU [yellow]AMARELO[/yellow]")
            return "coringa amarelo"
        elif escolha == 3:
            console.print("\nVOCÊ ESCOLHEU [blue]AZUL[/blue]")
            return "coringa azul"
        elif escolha == 4:
            console.print("\nVOCÊ ESCOLHEU [green]VERDE[/green]")
            return "coringa verde"

class Bot(Jogador):
    def __init__(self, cartas):
        super().__init__(cartas) #pega cartas do mesmo jeito que player
        self.carta_possivel
        self.vez
        self.comprar_carta
        self.escolher_cor

    def carta_possivel(self, carta_mesa, cartas_jog, descarte):
        carta_mesa = carta_mesa.split()

        if carta_mesa[0] == "+4":
            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "bloquear" or carta_atual[0] == "retornar": #se for carta de bloqueio ou retorno
                    return self.cartas[i] #joga essa carta primeiro

            for i in range(len(self.cartas)): #vê se tem +2 em todas as cartas da mão
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "+2": #se for +2
                    return self.cartas[i] #joga o +2

            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if carta_atual[0].isnumeric() == True: #se tiver carta normal
                    return self.cartas[i] #jogar

            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if(carta_atual[0] == "escolhe"): #se tiver coringa (escolhe cor)
                    return self.cartas[i] #joga a coringa

            for i in range(len(self.cartas)): #vê se tem +4 em todas as cartas da mão
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "+4": #se for um +4
                    return self.cartas[i] #joga o +4

            #self.comprar_carta(descarte, carta_mesa)
            return "comprar"

        #ordem de prioridade das escolhas = ordem dos for de cima pra baixo
        for i in range(len(self.cartas)):
            carta_atual = self.cartas[i].split()

            if carta_atual[1] == carta_mesa[1]:
                if carta_atual[0] == "bloquear" or carta_atual[0] == "retornar": #se for carta de bloqueio ou retorno da cor da mesa
                    return self.cartas[i] #joga essa carta primeiro

        if len(cartas_jog) <= 3:
            for i in range(len(self.cartas)): #vê se tem +4 em todas as cartas da mão
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "+4": #se for um +4
                    return self.cartas[i] #joga o +4
            
            for i in range(len(self.cartas)):#vê se tem +2 em todas as cartas da mão
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "+2" and carta_atual[1] == carta_mesa[1]: #se for +2 da cor da mesa
                    return self.cartas[i] #joga o +2

            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == carta_mesa[0] or carta_atual[1] == carta_mesa[1]: #se tiver carta normal
                    return self.cartas[i] #jogar
            
            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if(carta_atual[0] == "escolhe"): #se tiver coringa (escolhe cor)
                    return self.cartas[i] #joga a coringa

            #self.comprar_carta(descarte, carta_mesa)
            return "comprar"

        else:
            for i in range(len(self.cartas)): #vê se tem +2 em todas as cartas da mão
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "+2" and carta_atual[1] == carta_mesa[1]: #se for +2 da cor da mesa
                    return self.cartas[i] #joga o +2

            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == carta_mesa[0] or carta_atual[1] == carta_mesa[1]: #se tiver carta normal
                    return self.cartas[i] #jogar

            for i in range(len(self.cartas)):
                carta_atual = self.cartas[i].split()

                if(carta_atual[0] == "escolhe"): #se tiver coringa (escolhe cor)
                    return self.cartas[i] #joga a coringa

            for i in range(len(self.cartas)): #vê se tem +4 em todas as cartas da mão
                carta_atual = self.cartas[i].split()

                if carta_atual[0] == "+4": #se for um +4
                    return self.cartas[i] #joga o +4

            #self.comprar_carta(descarte, carta_mesa)
            return "comprar"

    def vez(self, carta_mesa, descarte):
        console.print("\n====================================================\n\n[bold light_pink3]-->>> VEZ DO BOT <<<--[/bold light_pink3]")
        print(self.cartas)
        
        carta_escolhida = self.carta_possivel(carta_mesa, jog.cartas, mesa.descarte) #executa a função pra ver se a carta é certa

        if carta_escolhida == "comprar":
            carta_escolhida = self.comprar_carta(descarte, carta_mesa)
        else:
            console.print("O BOT ESCOLHEU", end=' ', style="bold")
            baralho_colorido(carta_escolhida) #colocar carta colorida

            for i in range(len(self.cartas)):
                if self.cartas[i] == carta_escolhida: #se a carta atual for a mesma que ele escolheu
                    self.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog
                    break

        carta_escolhida_s = carta_escolhida.split()

        if carta_escolhida == "escolhe cor": #se for coringa
            carta_escolhida = self.escolher_cor(carta_mesa, self.cartas) #executar função de escolher cor

        elif carta_escolhida_s[0] == "+2":
            compra_por_carta(2, "bot")
            carta = self.vez(carta_escolhida, descarte)
            carta_escolhida = carta
            
        elif carta_escolhida_s[0] == "+4":
            compra_por_carta(4, "bot")
            carta = self.vez(carta_escolhida, descarte)
            carta_escolhida = carta

        #return carta_escolhida #retorna a carta escolhida
        return carta_escolhida

    def comprar_carta(self, descarte, carta_mesa):
        carta_comprada = descarte[0] #pega a primeira carta do descarte
        console.print("\nBOT COMPROU UMA CARTA", style="bold")
        #baralho_colorido(carta_comprada) #colocar carta colorida

        carta_comprada_s = carta_comprada.split() #separa em numero/cor
        carta_mesa_s = str(carta_mesa).split() #separa em numero/cor

        if carta_comprada_s[0] == carta_mesa_s[0] or carta_comprada_s[1] == carta_mesa_s[1] or carta_comprada_s[1] == "cor" or carta_comprada[0] == "+4": #se for jogável
            console.print("BOT JOGOU A CARTA", end=' ', style="bold")
            baralho_colorido(carta_comprada)
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_comprada #retorna a carta comprada
        else:
            console.print("A CARTA NÃO PODE SER JOGADA E O BOT NÃO A JOGOU", style="bold")
            self.cartas.append(carta_comprada)
            mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_mesa #retorna a carta da mesa (carta da mesa não muda)

    def escolher_cor(self, carta_mesa, cartas):
        n_vermelho, n_amarelo, n_azul, n_verde = 0, 0, 0, 0 #contadores pra escolher a cor que o bot mais tem na mão

        for i in range(len(cartas)):
            carta_atual = cartas[i].split()

            if carta_atual[1] == "vermelho": #se a carta atual for vermelha
                n_vermelho += 1 #+1 no contador
            elif carta_atual[1] == "amarelo":
                n_amarelo += 1
            elif carta_atual[1] == "azul":
                n_azul += 1
            elif carta_atual[1] == "verde":
                n_verde += 1

        cores = [n_vermelho, n_amarelo, n_azul, n_verde]
        n_cor = max(cores) #maior número da lista com os contadores

        for i in range(len(cores)): #pra cada quantidade de cores
            if cores[i] == n_cor: #se a atual for igual a maior
                if cores[i] == n_vermelho: #e se essa atual for a mesma quantidade do vermelho
                    console.print("\nBOT ESCOLHEU [bold red]VERMELHO[/bold red]")
                    return "coringa vermelho" #retorna que é vermelho (mesma lógica pros outros)
                elif cores[i] == n_amarelo:
                    console.print("\nBOT ESCOLHEU [bold yellow]AMARELO[/bold yellow]")
                    return "coringa amarelo"
                elif cores[i] == n_azul:
                    console.print("\nBOT ESCOLHEU [bold blue]AZUL[/bold blue]")
                    return "coringa azul"
                elif cores[i] == n_verde:
                    console.print("\nBOT ESCOLHEU [bold green]VERDE[/bold green]")
                    return "coringa verde"

#FUNÇÕES
#-----------
def baralho_colorido(cartas):
    if type(cartas) == type([1, 2]): #se for uma lista
        for i in range(len(cartas)):
            carta_atual = cartas[i].split()

            if carta_atual[1] == "vermelho": #se for vermelho
                console.print("[bold red]" + cartas[i] + "[/bold red]", end ='\n' if i==len(cartas)-1 else ' - ') #carta aparece vermelha + separador se não for a última carta (mesma lógica nos outros)

            elif carta_atual[1] == "amarelo":
                console.print("[bold yellow]" + cartas[i] + "[/bold yellow]", end ='\n' if i==len(cartas)-1 else ' - ')

            elif carta_atual[1] == "azul":
                console.print("[bold blue]" + cartas[i] + "[/bold blue]", end ='\n' if i==len(cartas)-1 else ' - ')

            elif carta_atual[1] == "verde":
                console.print("[bold green]" + cartas[i] + "[/bold green]", end ='\n' if i==len(cartas)-1 else ' - ')

            elif carta_atual[1] == "cor" or carta_atual[1] == "coringa":
                console.print("[reverse]" + cartas[i] + "[/reverse]", end ='' if i==len(cartas)-1 else ' - ')

    else: #se não for lista (ou seja, se for uma carta só)
        carta_atual = cartas.split()

        if carta_atual[1] == "vermelho": #se for vermelha
            console.print("[bold red]" + cartas + "[/bold red]") #vai aparecer vermelha (mesma lógica nos outros)

        elif carta_atual[1] == "amarelo":
            console.print("[bold yellow]" + cartas + "[/bold yellow]")

        elif carta_atual[1] == "azul":
            console.print("[bold blue]" + cartas + "[/bold blue]")

        elif carta_atual[1] == "verde":
            console.print("[bold green]" + cartas + "[/bold green]")

        elif carta_atual[1] == "cor" or carta_atual[1] == "coringa":
            console.print("[reverse]" + cartas + "[/reverse]")

def compra_por_carta(n, jogad):
    if jogad == "jog":
        for i in range(n):
            bot.cartas.append(mesa.descarte[i])
            mesa.descarte.pop(i)
        console.print("\nBOT TEVE QUE COMPRAR", n, "CARTA(S)", style="bold u")

    elif jogad == "bot":
        for i in range(n):
            jog.cartas.append(mesa.descarte[i])
            mesa.descarte.pop(i)
        console.print("\nVOCÊ TEVE QUE COMPRAR", n, "CARTA(S)", style="bold u")

#MAIN
#-----------
console = Console()

console.print("\n[u bold red]>>>> UNO EM PYTHON PLAYER VS CPU <<<<[/u bold red]")
console.print("\n[i bold violet]>> ESSE PROJETO FOI FEITO POR GITHUB.COM/TARTAPONEI <<[/i bold violet]\n[i bold pink3]>> DIVIRTA-SE :)) <<[/i bold pink3]")
random.shuffle(BARALHO) #embaralha as cartas

n = int(input("\nNÚMERO DE CARTAS PRA CADA JOGADOR: "))

#print("\033[H\033[J") #limpa a tela

#---DISTRIBUIÇÂO DAS CARTAS---
jog = Jogador(BARALHO[0:n]) #primeiras n cartas separadas pro jog
bot = Bot(BARALHO[n:n*2]) #as próximas n cartas pro bot

descarte = BARALHO[n*2:-1] #restante das cartas pro descarte

console.print("\n[bold u reverse]O JOGO COMEÇOU![/bold u reverse]\n")

console.print("[bold]\nSEU BARALHO INICIAL:[/bold]", end=' ')
baralho_colorido(jog.cartas) #colocar carta colorida
print("\nBOT:", bot.cartas)

console.print("\nBOT TEM[bold] {} [/bold]CARTAS" .format(len(bot.cartas)))
console.print("VOCÊ TEM[bold] {} [/bold]CARTAS" .format(len(jog.cartas)))

#---ESCOLHE A CARTA DA MESA---
mesa = Mesa(descarte)
mesa.carta = mesa.escolhe_carta_mesa() #escolhe a carta da mesa

console.print("\n[bold u]CARTA DA MESA:[/bold u]", end=' ')
baralho_colorido(mesa.carta)

#---EXCLUI A CARTA DA MESA DO DESCARTE---
i = 0 #inicializador pra teste
while i == 0: #enquanto o inicializador for0
    if mesa.descarte[i] == mesa.carta: #se a carta atual for a mesma da mesa
        del(mesa.descarte[i]) #carta atual é excluída
        i = 1 #inicializador passa a ser 1

#print("DESCARTE:", mesa.descarte)

#---PRIMEIRA RODADA---
quem_joga = random.randint(0, 1)

#---CONTINUAÇÃO DO JOGO---
while (len(jog.cartas) > 0 and len(bot.cartas) > 0): #enquanto nenhum dos dois bater
    if quem_joga == 0: #se quem jogou antes foi o jogador
        #---VEZ DO BOT---
        mesa.carta = bot.vez(mesa.carta, mesa.descarte)

        #print("\nBARALHO ATUALIZADO DO BOT:", bot.cartas)

        console.print("\nBOT TEM[bold] {} [/bold]CARTAS" .format(len(bot.cartas)))
        console.print("VOCÊ TEM[bold] {} [/bold]CARTAS" .format(len(jog.cartas)))

        console.print("[bold u]\nNOVA CARTA DA MESA:[/bold u]", end=' ')
        baralho_colorido(mesa.carta) #colocar carta colorida

        if len(bot.cartas) == 1: #caso tenha uma carta
            console.print("[bold u]\nBOT DISSE UNO!![/bold u]")

        tipo_carta = mesa.carta.split()

        if tipo_carta[0] == "retornar" or tipo_carta[0] == "bloquear": #se for carta de bloqueio ou retorno
            quem_joga = 0 #repete a vez
        else:
            quem_joga = 1 #próximo a jogar é o jogador

    else:
        #---VEZ DO JOGADOR---
        mesa.carta = jog.vez(mesa.carta, mesa.descarte) #carta da mesa vira a que foi escolhida pelo jog

        console.print("[bold]\nSEU BARALHO ATUALIZADO:[/bold]", end=' ')
        baralho_colorido(jog.cartas) #colocar carta colorida

        console.print("\nBOT TEM[bold] {} [/bold]CARTAS" .format(len(bot.cartas)))
        console.print("VOCÊ TEM[bold] {} [/bold]CARTAS" .format(len(jog.cartas)))

        console.print("[bold u]\nNOVA CARTA DA MESA:[/bold u]", end=' ')
        baralho_colorido(mesa.carta) #colocar carta colorida

        if len(jog.cartas) == 1: #caso tenha uma carta
            console.print("[bold u]\nVOCÊ DISSE UNO!![/bold u]")

        tipo_carta = mesa.carta.split()

        #---BLOQUEIO / RETORNO---
        if tipo_carta[0] == "retornar" or tipo_carta[0] == "bloquear": #se for carta de bloqueio ou retorno
            quem_joga = 1 #repete a vez
        else:
            quem_joga = 0 #próximo a jogar é o bot

if len(jog.cartas) == 0:
    vencedor = "VOCÊ"
else:
    vencedor = "BOT"

console.print("\n====================================================\n[u bold red]{} VENCEU, PARABÉNS!![/u bold red]" .format(vencedor))
console.print("[u bold violet]\n----->FIM DO JOGO!! :)<-----[/u bold violet]")