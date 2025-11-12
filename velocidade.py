velocidade=float(input("A que volocidade passou no radar"))
if velocidade>80:
   acima=velocidade-80
   multa=acima*2
   print(f'Está acima de velocidade permitida,a multa é{multa}€')
else:
    print("Dentro do limite,boa viagem!")