#import style
import sys
from colorama import Fore, Style

def baralho_com_cor(cartas):
    for i in range(len(cartas)):
        carta_atual = cartas[i].split()

        if carta_atual[1] == "vermelho":
            if i == len(cartas)-1:
                print(Fore.RED + cartas[i], end='')
            else:
                print(Fore.RED + cartas[i] + Fore.WHITE, end=' - ')

        elif carta_atual[1] == "amarelo":
            if i == len(cartas)-1:
                print(Fore.YELLOW + cartas[i], end='')
            else:
                print(Fore.YELLOW + cartas[i] + Fore.WHITE, end=' - ')

        elif carta_atual[1] == "azul":
            if i == len(cartas)-1:
                print(Fore.BLUE + cartas[i], end='')
            else:
                print(Fore.BLUE + cartas[i] + Fore.WHITE, end=' - ')

        elif carta_atual[1] == "verde":
            if i == len(cartas)-1:
                print(Fore.GREEN + cartas[i], end='')
            else:
                print(Fore.GREEN + cartas[i] + Fore.WHITE, end=' - ')
    print(Style.RESET_ALL)

b = ["1 amarelo", "2 vermelho", "3 azul", "4 verde"]

baralho_com_cor(b)
print("a", end='')
print("b")