d = int (input("Escreveste um numero "))
e = int (input("Escreve outro numero : "))
sinal= input("Insere + - * ou / : ")

if sinal == "+" :
    f = d + e
elif sinal == "-":
    f = d - e
elif sinal == "*":
    f = d * e
elif sinal == "/":
    f = d / e
print (f)
