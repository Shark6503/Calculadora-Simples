num_inicial =int(input("Diga o numero inicial"))

num_final =int(input("Diga o numero final"))
incremento=2

if num_inicial%2 == 0:
      for i in range(num_inicial,num_final+1,incremento):
            print(i)

else:
      for i in range(num_inicial+1,num_final+1,incremento):
            print(i)