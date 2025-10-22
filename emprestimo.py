dinheiro=int(input("Quanto dinheiro queremos imprestar"))
divida=int(input("Tem dividas? (1=sim 2=nao)"))

if   divida == 1:
    print("Tem divida,nao posso emprestar")
elif divida == 2:
    print("Posso emprestar",dinheiro,"€")
else:
    print("Nao utilizaste a duvida correta")

