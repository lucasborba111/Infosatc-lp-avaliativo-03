idade = int(input("Idade:"))
peso = float(input("Peso:"))
sono = input("Dormiu 6 horas nas últimas 24 horas?")
if(sono=="sim"or sono=="não"):
    if(sono=="não"):
        print("Não apresenta-se totalmente disposto")
else:
    pass
if(idade<16 or idade>69):
    print("Não possui idade ideal")
else:
    pass
if(peso<50):
    print("Não possui peso ideal")
else:
    pass