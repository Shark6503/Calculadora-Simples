num_inicial =int(input("Diga o numero inicial"))

num_final =int(input("Diga o numero final"))

incremento =int(input("Incremento"))

print(f"Os números entre o {num_inicial} e {num_final} com incremento {incremento}")
for i in range(num_inicial,num_final+1,incremento):
    print(i)