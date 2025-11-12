kwh=float(input("Indique os kwh que consome: "))
tipo=input("Qual o tipo de instalação(R-Residência,I-indústria,C-Comércio: ")
if tipo=="R":
    if kwh<500:
        pagamento=kwh*0.4
    else:
        pagamento=kwh*0.65
elif tipo=="C":
    if kwh<1000:
        pagamento=kwh*0.55
    else:
        pagamento=kwh*0.6
elif tipo=="I":
    if kwh<5000:
        pagamento=kwh*0.55
    else:
        pagamento=kwh*0.6
else:
    pagamento=0
print("Tem de pagar:",pagamento)



