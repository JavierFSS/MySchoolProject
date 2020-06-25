notas = int(float(input())*100)
print("NOTAS:")
a = notas//10000
notas -= 10000*a
print("%i nota(s) de R$ 100.00" % (a))
a = notas//5000
notas -= 5000*a
print("%i nota(s) de R$ 50.00" % (a))
a = notas//2000
notas -= 2000*a
print("%i nota(s) de R$ 20.00" % (a))
a = notas//1000
notas -= 1000*a
print("%i nota(s) de R$ 10.00" % (a))
a = notas//500
notas -= 500*a
print("%i nota(s) de R$ 5.00" % (a))
a = notas//200
notas -= 200*a
print("%i nota(s) de R$ 2.00" % (a))
print("MOEDAS:")
a = notas//100
notas -= 100*a
print("%i moeda(s) de R$ 1.00" % (a))
a = notas//50
notas -= 50*a
print("%i moeda(s) de R$ 0.50" % (a))
a = notas//25
notas -= 25*a
print("%i moeda(s) de R$ 0.25" % (a))
a = notas//10
notas -= 10*a
print("%i moeda(s) de R$ 0.10" % (a))
a = notas//5
notas -= 5*a
print("%i moeda(s) de R$ 0.05" % (a))
a = notas//1
notas -= 1*a
print("%i moeda(s) de R$ 0.01" % (a))