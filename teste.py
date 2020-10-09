def carta_possivel(carta_mesa, cartas, cartas_jog):
    carta_mesa = carta_mesa.split()

    #ordem de prioridade das escolhas = ordem dos for de cima pra baixo
    for i in range(len(cartas)):
        carta_atual = cartas[i].split()

        if carta_atual[0] == "bloquear" or carta_atual[0] == "retornar" and carta_atual[1] == carta_mesa[1]: #se for carta de bloqueio ou retorno da cor da mesa
            return cartas[i] #joga essa carta primeiro

    if len(cartas_jog) <= 3:
        for i in range(len(cartas)): #vê se tem +4 em todas as cartas da mão
            carta_atual = cartas[i].split()

            if carta_atual[0] == "+4": #se for um +4
                return cartas[i] #joga o +4
        
        for i in range(len(cartas)):#vê se tem +2 em todas as cartas da mão
            carta_atual = cartas[i].split()

            if carta_atual[0] == "+2" and carta_atual[1] == carta_mesa[1]: #se for +2 da cor da mesa
                return cartas[i] #joga o +2

        for i in range(len(cartas)):
            carta_atual = cartas[i].split()

            if (carta_atual[0] == carta_mesa[0] or carta_atual[1] == carta_mesa[1]): #se tiver carta normal
                return cartas[i] #jogar
        
        for i in range(len(cartas)):
            carta_atual = cartas[i].split()

            if(carta_atual[0] == "escolhe"): #se tiver coringa (escolhe cor)
                return cartas[i] #joga a coringa

        return "comprar"
        #comprar_carta(descarte, carta_mesa)

    else:
        for i in range(len(cartas)):#vê se tem +2 em todas as cartas da mão
            carta_atual = cartas[i].split()

            if carta_atual[0] == "+2" and carta_atual[1] == carta_mesa[1]: #se for +2 da cor da mesa
                return cartas[i] #joga o +2

        for i in range(len(cartas)):
            carta_atual = cartas[i].split()

            if (carta_atual[0] == carta_mesa[0] or carta_atual[1] == carta_mesa[1]): #se tiver carta normal
                return cartas[i] #jogar

        for i in range(len(cartas)):
            carta_atual = cartas[i].split()

            if(carta_atual[0] == "escolhe"): #se tiver coringa (escolhe cor)
                return cartas[i] #joga a coringa

        for i in range(len(cartas)): #vê se tem +4 em todas as cartas da mão
            carta_atual = cartas[i].split()

            if carta_atual[0] == "+4": #se for um +4
                return cartas[i] #joga o +4

        return "comprar"
        #comprar_carta(descarte, carta_mesa)
        

mesa = "4 amarelo"
cartas_b = ["2 azul", "9 azul", "e5 vermelho", "2 verde"]
cartas_j = ["4 verde", "9 azul", "5 vermelho", "9 amarelo"]

print(carta_possivel(mesa, cartas_b, cartas_j))