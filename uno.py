#BIBLIOTECAS
#------------
import random
from rich.console import Console
from rich.table import Table
from rich import box
from time import sleep

#ARQUIVOS
#----------
import variaveis as var
from classes import baralho_colorido

#VARIAVEIS INICIAIS
#------------------- 
BARALHO = ["1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", "+2 vermelho", 
"1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo", "+2 amarelo",
"1 azul", "2 azul", "3 azul", "4 azul", "5 azul", "6 azul", "7 azul", "8 azul", "9 azul", "+2 azul",
"1 verde", "2 verde", "3 verde", "4 verde", "5 verde", "6 verde", "7 verde", "8 verde", "9 verde", "+2 verde",

"bloquear vermelho", "bloquear amarelo", "bloquear azul", "bloquear verde",
"retornar vermelho", "retornar amarelo", "retornar azul", "retornar verde",

"escolhe cor", "escolhe cor", "escolhe cor", "escolhe cor", "+4 coringa", "+4 coringa", "+4 coringa", "+4 coringa"]

BARALHO.extend(BARALHO) #pra dobrar o baralho sem digitar muito


'''#FUNÇÕES
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
'''
#MAIN
#-----------
#try:
console = Console()
reiniciar = "sim"

print("\n")

#---TABELA DE APRESENTAÇÃO---
titulo = Table(box=box.HEAVY_HEAD, style="bold indian_red")

titulo.add_column(">>>> UNO EM PYTHON PLAYER VS CPU <<<<", style="i bold medium_purple4", justify="center")
titulo.add_row(">> ESSE PROJETO FOI FEITO POR GITHUB.COM/TARTAPONEI <<")
titulo.add_row(">> DIVIRTA-SE :)) <<", style="i bold pink3")

console.print(titulo) ; sleep(4)

print("\n=============================================================\n")

while reiniciar == "sim":
    random.shuffle(BARALHO) #embaralha as cartas

    #---TABELA DE PLACAR---
    placar = Table(box=box.MINIMAL, title="Placar Atual", style="bold orange3")

    placar.add_column("BOT", justify="center", style="magenta")
    placar.add_column("VOCÊ", justify="center", style="magenta")
    placar.add_row(str(var.v_bot), (str(var.v_jog)))

    console.print(placar) ; sleep(1)

    n = 0

    while n <= 3:
        n = int(input("\nDIGITE O NÚMERO DE CARTAS PRA CADA JOGADOR (A PARTIR DE 4): "))

    #print("\033[H\033[J") #limpa a tela

    #---DISTRIBUIÇÂO DAS CARTAS---
    var.jog.cartas = BARALHO[0:n] #primeiras n cartas separadas pro jog
    var.bot.cartas = BARALHO[n:n*2] #as próximas n cartas pro bot

    descarte = BARALHO[n*2:-1] #restante das cartas pro descarte

    console.print("\n\n[bold u reverse]>>> O JOGO COMEÇOU!<<<[/bold u reverse]\n") ; sleep(0.2)

    console.print("[bold]\nSEU BARALHO INICIAL:[/bold]", end=' ')
    baralho_colorido(var.jog.cartas) ; sleep(3) #colocar carta colorida
    #print("\nBOT:", bot.cartas)

    console.print("\nBOT TEM[bold] {} [/bold]CARTAS" .format(len(var.bot.cartas)), style="bold pink3") ; sleep(1)
    console.print("VOCÊ TEM[bold] {} [/bold]CARTAS" .format(len(var.jog.cartas)), style="bold pink3") ; sleep(1)

    #---ESCOLHE A CARTA DA MESA---
    var.mesa.descarte = descarte
    var.mesa.carta = var.mesa.escolhe_carta_mesa() #escolhe a carta da mesa

    console.print("\n[bold u]CARTA DA MESA:[/bold u]", end=' ')
    baralho_colorido(var.mesa.carta) ; sleep(1)

    #---EXCLUI A CARTA DA MESA DO DESCARTE---
    for i in range(len(var.mesa.descarte)): #enquanto o inicializador for0
        if var.mesa.descarte[i] == var.mesa.carta: #se a carta atual for a mesma da mesa
            var.mesa.descarte.pop(i) #carta atual é excluída
            break

    #---PRIMEIRA RODADA---
    quem_joga = random.randint(0, 1)

    #---CONTINUAÇÃO DO JOGO---
    while (len(var.jog.cartas) > 0 and len(var.bot.cartas) > 0): #enquanto nenhum dos dois bater
        if quem_joga == 0: #se quem jogou antes foi o jogador
            #---VEZ DO BOT---
            var.mesa.carta = var.bot.vez(var.mesa.carta, var.mesa.descarte)

            #print("\nBARALHO ATUALIZADO DO BOT:", bot.cartas)

            console.print("\nBOT TEM[bold] {} [/bold]CARTAS" .format(len(var.bot.cartas)), style="bold pink3") ; sleep(1)
            console.print("VOCÊ TEM[bold] {} [/bold]CARTAS" .format(len(var.jog.cartas)), style="bold pink3") ; sleep(1)

            console.print("[bold u]\nNOVA CARTA DA MESA:[/bold u]", end=' ')
            baralho_colorido(var.mesa.carta) ; sleep(1) #colocar carta colorida

            var.mesa.descarte.append(var.mesa.carta) #a carta da mesa já entra no final do descarte pra não acabar as cartas do descarte

            if len(var.bot.cartas) == 1: #caso tenha uma carta
                console.print("[bold orange1 u]\nBOT DISSE UNO!![/bold orange1 u]") ; sleep(1)

            tipo_carta =var. mesa.carta.split()

            quem_joga = 1 #próximo a jogar é o jogador

        else:
            #---VEZ DO JOGADOR---
            var.mesa.carta = var.jog.vez(var.mesa.carta, var.mesa.descarte) #carta da mesa vira a que foi escolhida pelo jog

            console.print("[bold]\nSEU BARALHO ATUALIZADO:[/bold]", end=' ')
            baralho_colorido(var.jog.cartas) #colocar carta colorida

            console.print("\nBOT TEM[bold] {} [/bold]CARTAS" .format(len(var.bot.cartas)), style="bold pink3") ; sleep(1)
            console.print("VOCÊ TEM[bold] {} [/bold]CARTAS" .format(len(var.jog.cartas)), style="bold pink3") ; sleep(1)

            console.print("[bold u]\nNOVA CARTA DA MESA:[/bold u]", end=' ')
            baralho_colorido(var.mesa.carta) ; sleep(1) #colocar carta colorida

            var.mesa.descarte.append(var.mesa.carta) #a carta da mesa já entra no final do descarte pra não acabar as cartas do descarte

            if len(var.jog.cartas) == 1: #caso tenha uma carta
                console.print("[bold orange1 u]\nVOCÊ DISSE UNO!![/bold orange1 u]") ; sleep(1)

            tipo_carta = var.mesa.carta.split()

            quem_joga = 0 #próximo a jogar é o bot

    if len(var.jog.cartas) == 0:
        vencedor = "VOCÊ"
        var.v_jog += 1
    else:
        vencedor = "BOT"
        var.v_bot += 1

    console.print("\n====================================================\n\n[u bold red]>>>> {} VENCEU, PARABÉNS!! <<<<[/u bold red]" .format(vencedor))
    console.print("[u bold violet]\n-----> FIM DO JOGO!! :) <-----[/u bold violet]")

    console.print("\n\n> DESEJA JOGAR DE NOVO? DIGITE 'sim' OU 'não':", end=' ', style="bold pink3")
    reiniciar = input("")
#except:
    #console.print("\n>>> Algum erro ocorreu. Reinicie e vê se vai da próxima :)", style="bold red")