kwh=float(input("Indique os kwh que consome: "))
tipo=input("Qual o tipo de instalação(R-Residência,I-indústria,C-Comércio: ")
match tipo:
    case "R":
        if kwh<500:
            pagamento=kwh*0.4
        else:
            pagamento=kwh*0.65
    case "C":
        if kwh<1000:
            pagamento=kwh*0.55
        else:
            pagamento=kwh*0.6
    case "I":
        if kwh<5000:
            pagamento=kwh*0.55
        else:
            pagamento=kwh*0.6
    case _:
            pagamento=0
print("Tem de pagar:",pagamento)
