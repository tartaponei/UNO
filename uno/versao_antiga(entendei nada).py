import random

def escolhaBot(cartas, jog, mesa, baralho, n):
    opcoes = []
    cor = "" #variável da cor escolhida pelo bot
    escolha = []

    #definição das cartas prioridade
    #for i in range(len(cartas)):
    #print(i)
    
    for i in range(len(cartas)):
        #mesa = mesa.split()
        print(opcoes)
        print(jog)
        atual = cartas[i].split()

        if(jog > 3):
            if((atual[0] != "+4" and atual[0] != "+2" and atual[0] != "escolhe")):
                print(atual[0])
                print(atual[1])
                print(mesa[0])
                print(mesa[1])
                if(atual[0] == mesa[0] or atual[1] == mesa[1]):
                    opcoes.append(cartas[i])

                elif((mesa[0] != "+2" and atual[0] == "+2") or atual[0] == "+4"):
                    opcoes.append(cartas[i])
            else:
                if(atual[0] == "+2" and atual[1] == mesa[1]):
                    opcoes = [atual]
                else:
                    if(atual[0] == "escolhe cor"):
                        opcoes = [atual]

                    if(atual[0] == mesa[0] and atual[1] == mesa[1]):
                        opcoes.append(cartas[i])

                    if((mesa[0] != "+2" and atual[0] == "+2") or atual[0] == "+4"):
                        opcoes.append(cartas[i])

        else:
            if(atual[0] == "+4"):
                opcoes = [atual]
            else:
                if(atual[0] == "+2" and atual[1] == mesa[1]):
                    opcoes = [atual]
                else:
                    if(atual[0] == "escolhe cor"):
                        opcoes = [atual]

                    if(atual[0] == mesa[0] and atual[1] == mesa[1]):
                        opcoes.append(cartas[i])

                    if((mesa[0] != "+2" and atual[0] == "+2") or atual[0] == "+4"):
                        opcoes.append(cartas[i])

    #if(len(opcoes) < 1):
         #opcoes.append(random.choice(baralho))

    
    p = random.choice(opcoes)

    #escolha da cor caso a carta escolhida seja a de escolher cor
    if(p[0] == "escolhe cor"):
        if(len(cartas) > 1):
            v = 0
            a = 0
            for i in opcoes:
                atual = opcoes[i]

                if(atual[1] == "vermelho"):
                    v = v + 1
                if(atual[1] == "amarelo"):
                    a = a + 1

            if(v > a):
                cor = "vermelho"
            if(a > v):
                cor = "amarelo"
            if(v == a):
                cores = ["vermelho", "amarelo"]
                cor = random.choice(cores)
    escolha = p + cor
    return escolha


baralho = ["1 vermelho", "2 vermelho", "3 vermelho", "4 vermelho", "5 vermelho", "6 vermelho", "7 vermelho", "8 vermelho", "9 vermelho", "+2 vermelho",
"1 amarelo", "2 amarelo", "3 amarelo", "4 amarelo", "5 amarelo", "6 amarelo", "7 amarelo", "8 amarelo", "9 amarelo", "+2 amarelo",
"+4", "escolhe cor"]

n = int(input("número de cartas pra cada jogador: "))

cartas_jog = []

"""
igual = 0
while(igual == 0 or igual == 1):
    #c = random.randrange(0, 22)
    cartas_jog = random.sample(baralho, n)
    if (len(cartas_jog) > 1):
    	for i in range(len(cartas_jog)):
            for s in range(len(cartas_jog)):
    		if(cartas_jog[i] == cartas_jog[s]):
		    igual = igual + 1
		    break
    break
	
print(cartas_jog)

cartas_bot = []

igual = 0
while(igual == 0 or igual == 1):
    cartas_bot = random.sample(baralho, n)
    if (len(cartas_bot) > 1):
	for i in range(len(cartas_bot)):
	    for s in range(len(cartas_bot)):
		if(cartas_bot[i] == cartas_bot[s]):
		    igual = igual + 1
		    break
    break
	
print(cartas_bot)
"""
#emabaralha as cartas
random.shuffle(baralho)

#distribui as cartas e conta quantas tem em cada mão
cartas_jog = baralho[0:n]
num_jog = len(cartas_jog)
cartas_bot = baralho[n:n*2]
num_bot = len(cartas_bot)
descarte = baralho[n*2:-1]
	
print("\nSUAS CARTAS: ", cartas_jog)
print("\nBOT: ", cartas_bot)
#print("\nBARALHO: ", descarte)

#escolhe e coloca a carta inicial da mesa (exclui as especiais das opcções)
s = 0
while(s == 0):
    mesa = random.choice(descarte)
    tipo = mesa.split()
	
    if(tipo[0] == "+2" or tipo[0] == "+4" or tipo[0] == "escolhe "):
        s = 0
    else:
        s = 1
	
print("\nCARTA ATUAL DA MESA: ", mesa)

#vez = random.randrange(0, 2)
vez = 1

while(num_jog > 0 or num_bot > 0):
    if(vez == 0):
        j = int(input("É A SUA VEZ, ESCOLHA UMA CARTA DO SEU BARALHO DE ACORDO COM O ÍNDICE (LEMBRE QUE COMEÇA NO 0): ", cartas_jog))
        mesa = cartas_jog[j]
        del(cartas_jog[j])
        num_jog = len(cartas_jog)
        vez = 1
    else:
        mesa = escolhaBot(cartas_bot, num_jog, mesa, descarte, n)
        for i in range(len(cartas_bot)):
            atual = cartas_bot[i]
            if(cartas_bot[i] == mesa or mesa[0] == "escolhe" and atual[0] == "escolhe"):
                del(cartas_bot[j])
        num_bot = len(cartas_bot)
        vez = 0
    print("\nCARTA ATUAL DA MESA: ", mesa)
