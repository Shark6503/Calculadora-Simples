numero_inicial=int(input("Diga o numero inicial"))
numero_final=int(input("Diga o numero final"))

decisao=input("Par(P)Impar (I)")
if decisao == "P":
    if numero_inicial%2==0:
        for i in range(numero_inicial,numero_final+1,2):
            print (i)
    else:
        for i in range(numero_inicial,numero_final+1,2):
            print(i)
elif decisao == "I":
    if numero_inicial%2 !=0:
        for i in range(numero_inicial+1,numero_final+1,2):
            print(i)
    else:
        for i in range(numero_inicial+1,numero_final+1,2):
            print (i)