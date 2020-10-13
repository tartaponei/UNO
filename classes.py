#BIBLIOTECAS
#------------
from rich.console import Console
from time import sleep

import variaveis as var

console = Console()

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
    contador = 0
    def __init__(self, cartas):
        self.cartas = cartas
    
    def vez(self, carta_mesa, descarte):
        carta = "errada" #carta inicialmente sendo errada
        e = "ab" #iniciada assim pra entrar no if a primeira vez
        repetir = 1

        print("\n====================================================\n") ; sleep(1)
        console.print("[bold light_pink3]-->>> SUA VEZ DE JOGAR <<<--\nEscolha sua carta de acordo com o índice [reverse](de 1 a {})[/reverse]:\n" .format(len(self.cartas)))
        print("SEU BARALHO:", end=' ')
        baralho_colorido(self.cartas) #colocar carta colorida
        print("\nSE QUISER COMPRAR UMA CARTA, DIGITE 'comprar':")
        
        while repetir == 1:
            e = input("SUA ESCOLHA: ") #jogador escolhe o índice da carta ou escolhe comprar
            if e.isnumeric() == False and e != "comprar":
                console.print("\nVOCÊ DIGITOU ALGO INVÁLIDO, DIGITE DE NOVO", style="bold")
            elif e.isnumeric == True and (int(e) > len(self.cartas) or int(e)) == 0:
                console.print("\nVOCÊ DIGITOU UM NÚMERO INVÁLIDO, DIGITE DE NOVO", style="bold")
            else:
                repetir = 0
                break

        print("\n====================================================") ; sleep(0.4)

        if e == "comprar": #se o jogador escolher comprar
            return self.comprar_carta(descarte, carta_mesa) #executar função de comprar carta

        else:
            escolha = int(e)-1 #índice da carta

            while carta == "errada": #enquanto a carta for errada
                carta_certa = self.carta_possivel(self.cartas, escolha, carta_mesa) #executa a função pra ver se a carta é certa

                if carta_certa == False: #se não for certa
                    console.print("\n[bold]VOCÊ ESCOLHEU[/bold]", end=' ')
                    baralho_colorido(self.cartas[escolha]) #colocar carta colorida
                    console.print("\nEssa carta não pode ser escolhida porque a carta da mesa é", end=' ')
                    baralho_colorido(var.mesa.carta)
                    console.print("\n[bold]ESCOLHA OUTRA![/bold]")
                    baralho_colorido(self.cartas) #colocar carta colorida
                    escolha = int(input("DIGITE: "))-1 #jogador escolhe outra
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
                        if self.contador < 3 and len(self.cartas) > 0:
                            carta = self.vez(carta_escolhida, descarte)
                            carta_escolhida = carta
                    
                    elif carta_escolhida_s[0] == "+4":
                        compra_por_carta(4, "jog")
                        if len(self.cartas) > 0:
                            carta = self.vez(carta_escolhida, descarte)
                            carta_escolhida = carta

                    elif carta_escolhida_s[0] == "bloquear" or carta_escolhida_s[0] == "retornar":
                        if self.contador < 3 and len(self.cartas) > 0:
                            carta = self.vez(carta_escolhida, descarte)
                            carta_escolhida = carta
                            self.contador -= 1

                    return carta_escolhida #retorna a carta que ele escolheu
    
    def carta_possivel(self, cartas, indice, carta_mesa):
        carta = self.cartas[indice].split() #pega a carta escolhida e separa em duas (numero / cor)
        #print(carta)
        carta_mesa = carta_mesa.split() #separa a carta da mesa em duas (numero / cor)

        CONDICOES_JOG = [
            carta[0] == carta_mesa[0], #se números forem iguais
            carta[1] == carta_mesa[1], #se cores forem iguais
            carta_mesa[0] == "+4", #se a carta da mesa for um +4
            carta[0] == "+4", #se carta jogada for um +4
            carta[0] == "escolhe" #se a carta jogada for coringa de cor
        ] 

        if any(CONDICOES_JOG): #se pelo menos uma das condições de jogador forem true
            return True
        else:
            return False

    def comprar_carta(self, descarte, carta_mesa):
        carta_comprada = descarte[0] #pega a primeira carta do descarte
        console.print("\n[bold]CARTA COMPRADA[/bold]:", end=' ')
        baralho_colorido(carta_comprada) #colocar carta colorida

        carta_comprada_s = carta_comprada.split() #separa em numero/cor
        carta_mesa_s = carta_mesa.split() #separa em numero/cor

        CONDICOES_COMPRA_JOG = [
            carta_comprada_s[0] == carta_mesa_s[0], #se números forem iguais
            carta_comprada_s[1] == carta_mesa_s[1], #se cores forem iguais
            carta_comprada_s[1] == "cor", #se a carta comprada é coringa de cor
            carta_comprada_s[0] == "+4", #se a carta comprada é um +4
            carta_mesa_s[0] == "+4" #se a carta da mesa é um +4
        ]

        if any(CONDICOES_COMPRA_JOG): #se for jogável (se qualquer uma das condições de compra for true)
            console.print("[bold]CARTA COMPRADA FOI JOGADA[/bold]")
            var.mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte

            if carta_comprada == "escolhe cor": #se for coringa
                carta_comprada = self.escolher_cor(carta_mesa) #executar função de escolher cor

            elif carta_comprada_s[0] == "bloquear" or carta_comprada_s[0] == "retornar":
                if self.contador < 3 and len(self.cartas) > 0:
                    carta = self.vez(carta_comprada, descarte)
                    carta_comprada = carta
                    self.contador -= 1

            elif carta_comprada_s[0] == "+2":
                compra_por_carta(2, "jog")

                if self.contador < 3 and len(self.cartas) > 0:
                    carta = self.vez(carta_comprada, descarte)
                    carta_comprada = carta
                    self.contador -= 1

            elif carta_comprada_s[0] == "+4":
                compra_por_carta(4, "jog")
                if len(self.cartas) > 0:
                    carta = self.vez(carta_comprada, descarte)
                    carta_comprada = carta

            return carta_comprada #retorna a carta comprada
        else:
            console.print("\nCARTA COMPRADA NÃO PODE SER JOGADA\nPORQUE A CARTA DA MESA É", end = ' ', style="bold")
            baralho_colorido(carta_mesa) 
            console.print("\nA CARTA COMPRADA FOI ADICIONADA AO SEU BARALHO", style="bold")
            self.cartas.append(carta_comprada) #carta comprada é adicionada ao baralho do jogador
            var.mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
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
    contador = 0
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
        self.contador += 1
        console.print("\n====================================================\n\n[bold light_pink3]-->>> VEZ DO BOT <<<--[/bold light_pink3]\n")
        #print(self.cartas)
        
        carta_escolhida = self.carta_possivel(carta_mesa, var.jog.cartas, var.mesa.descarte) #executa a função pra ver se a carta é certa

        if carta_escolhida == "comprar":
            carta_escolhida = self.comprar_carta(descarte, carta_mesa)
        else:
            console.print("O BOT ESCOLHEU", end=' ', style="bold")
            baralho_colorido(carta_escolhida) ; sleep(2) #colocar carta colorida

            for i in range(len(self.cartas)):
                if self.cartas[i] == carta_escolhida: #se a carta atual for a mesma que ele escolheu
                    self.cartas.pop(i) #exclui carta escolhida pra mesa do baralho do jog
                    break

        carta_escolhida_s = carta_escolhida.split()

        if carta_escolhida == "escolhe cor": #se for coringa
            carta_escolhida = self.escolher_cor(carta_mesa, self.cartas) #executar função de escolher cor

        elif carta_escolhida_s[0] == "+2":
            compra_por_carta(2, "bot")
            if self.contador < 3 and len(self.cartas) > 0:
                carta = self.vez(carta_escolhida, descarte)
                carta_escolhida = carta
                self.contador -= 1
            
        elif carta_escolhida_s[0] == "+4":
            compra_por_carta(4, "bot")
            if len(self.cartas) > 0:
                carta = self.vez(carta_escolhida, descarte)
                carta_escolhida = carta

        elif carta_escolhida_s[0] == "bloquear" or carta_escolhida_s[0] == "retornar":
            if self.contador < 3 and len(self.cartas) > 0:
                carta = self.vez(carta_escolhida, descarte)
                carta_escolhida = carta
                self.contador -= 1

        self.contador = 0
        return carta_escolhida

    def comprar_carta(self, descarte, carta_mesa):
        carta_comprada = descarte[0] #pega a primeira carta do descarte
        console.print("BOT COMPROU UMA CARTA", style="bold") ; sleep(2)
        #baralho_colorido(carta_comprada) #colocar carta colorida

        carta_comprada_s = carta_comprada.split() #separa em numero/cor
        carta_mesa_s = str(carta_mesa).split() #separa em numero/cor

        CONDICOES_COMPRA_BOT = [
            carta_comprada_s[0] == carta_mesa_s[0], #se os numeros forem iguais
            carta_comprada_s[1] == carta_mesa_s[1], #se as cores forem iguais
            carta_comprada_s[1] == "cor", #se a carta comprada for coringa de cor
            carta_comprada_s[0] == "+4", #se a carta comprada é um +4
            carta_mesa_s[0] == "+4", #se a carta da mesa é um +4

        ]

        if any(CONDICOES_COMPRA_BOT): #se pelo menos uma das condições de compra forem true (se for jogável)
            console.print("BOT JOGOU A CARTA COMPRADA", end=' ', style="bold")
            baralho_colorido(carta_comprada) ; sleep(2)
            var.mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
            return carta_comprada #retorna a carta comprada
        else:
            console.print("A CARTA NÃO PODE SER JOGADA E O BOT NÃO A JOGOU", style="bold") ; sleep(2)
            self.cartas.append(carta_comprada)
            var.mesa.excluir_carta_descarte(carta_comprada) #executar função pra tirar carta comprada do descarte
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
                console.print("[bold medium_purple2]" + cartas[i] + "[/bold medium_purple2]", end ='' if i==len(cartas)-1 else ' - ')

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
            console.print("[bold medium_purple2]" + cartas + "[/bold medium_purple2]")

def compra_por_carta(n, jogad):
    if jogad == "jog":
        for i in range(n):
            var.bot.cartas.append(var.mesa.descarte[i])
            var.mesa.descarte.pop(i)
        console.print("\nBOT TEVE QUE COMPRAR", n, "CARTA(S)", style="bold orange1 u") ; sleep(1)

    elif jogad == "bot":
        for i in range(n):
            var.jog.cartas.append(var.mesa.descarte[i])
            var.mesa.descarte.pop(i)
        console.print("\nVOCÊ TEVE QUE COMPRAR", n, "CARTA(S)", style="bold orange1 u") ; sleep(1)
