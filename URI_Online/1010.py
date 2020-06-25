a,b,c = input().split()
a = int(a)
b = int(b)
c = float(c)

code1, unit1, product1 = a
code2, unit2, product2 = b

total = (int(unit1) * float(product1)) + (int(unit2) * float(product2))

print("VALOR A PAGAR: R$ %0.2f" %total)

