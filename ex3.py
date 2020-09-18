meses = {1,2,3,4,5,6,7,8,9,10}
pergunta = int(input("Escolha um mês em numero de 1 a 11:"))
if(pergunta in meses):
    print("Numero do mês:: %s" %pergunta)
    if(pergunta==1):
        print("Mês escolhido: fevereiro")
    elif(pergunta==2):
        print("Mês escolhido: março")
    elif(pergunta==3):
        print("Mês escolhido: abril")
    elif(pergunta==4):
        print("Mês escolhido: maio")
    elif(pergunta==5):
        print("Mês escolhido: junho")
    elif(pergunta==6):
        print("Mês escolhido: julho")
    elif(pergunta==7):
        print("Mês escolhido: agosto")
    elif(pergunta==8):
        print("Mês escolhido: setembro")
    elif(pergunta==9):
        print("Mês escolhido: outubro")
    else:
        print("Mês escolhido: novembro")
else:
    print("O mês não está na lista")
