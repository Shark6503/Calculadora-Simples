prod1= input("Insira  o produto 1")
prod2= input("Insira  o produto 2")
prod3= input("Insira  o produto 3")
preco1=float(input("Insira o preco do produto 1"))
preco2=float(input("Insira o preco do produto 2"))
preco3=float(input("Insira o preco do produto 3"))
quant1=int(input("Insira o quantidade do produto 1"))
quant2=int(input("Insira o quantidade do produto 2"))
quant3=int(input("Insira o quantidade do produto 3"))
valorTotal1 = preco1*quant1
valorTotal2 = preco2*quant2
valorTotal3 = preco3*quant3
valorArmazem = valorTotal1+valorTotal2+valorTotal3
print("Valor Total",prod1,":",valorTotal1)
print("Valor Total",prod2,":",valorTotal2)
print("Valor Total",prod3,":",valorTotal3)