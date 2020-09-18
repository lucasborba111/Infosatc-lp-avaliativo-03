masculino = 0
mediaM = 0
feminino = 0
mediaF = 0
idadegeralM  = 0
idadegeralF = 0
pessoas = int(input("Escreva o total de pessoas"))
while(feminino+masculino<pessoas):
    sexo = input("M para masculino e F")
    if(sexo=="M"):
      masculino = masculino + 1
      idadeM = float(input("Escreva sua idade:"))
      idadegeralM = idadegeralM + idadeM
      mediaM = idadegeralM/masculino
    elif(sexo=="F"):
        feminino = feminino + 1
        idadeF = float(input("Escreva sua idade:"))
        idadegeralF = idadegeralF + idadeF
        mediaF = idadegeralF/feminino
    else:
         pass
print("Idade media dos homens:",mediaM)
print("Idade media das mulheres:",mediaF)

