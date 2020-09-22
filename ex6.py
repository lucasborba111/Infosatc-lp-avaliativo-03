
for i in range(0, 5):
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

    cadastro = input("Deseja efetuar castro?")
    if(cadastro=="sim"):
       i=i+1
       nome = input("Escreva seu nome completo")
       cpf = input("Escreva seu cpf:")
       senha = input("Defina uma senha:")
       sangue = input("Apresenta-se apto(a) para doar sangue?")
       if(i==1):
           cliente1 = (nome,cpf,senha,sangue)
       elif(i==2):
           cliente2 = (nome,cpf,senha,sangue)
       elif(i==3): 
           cliente3=(nome,cpf,senha,sangue)   
       elif(i==4):
           cliente4 = (nome,cpf,senha,sangue)
       else:
           cliente5 = (nome,cpf,senha,sangue)   
    elif(cadastro=="não"):
        pass
    else:
        print("Opção indisponível")
print("primeiro cliente",cliente1)
print("segundo cliente",cliente2)
print("terceiro cliente",cliente3)
print("quarto cliente",cliente4)
print("quinto cliente",cliente5)




    