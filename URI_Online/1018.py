n = int(input())
print(n)
a = n//100
n -= 100*a
print("%i nota(s) de R$ 100,00" % (a))
a = n//50
n -= 50*a
print("%i nota(s) de R$ 50,00" % (a))
a = n//20
n -= 20*a
print("%i nota(s) de R$ 20,00" % (a))
a = n//10
n -= 10*a
print("%i nota(s) de R$ 10,00" % (a))
a = n//5
n -= 5*a
print("%i nota(s) de R$ 5,00" % (a))
a = n//2
n -= 2*a
print("%i nota(s) de R$ 2,00" % (a))
a = n//1
n -= 1*a
print("%i nota(s) de R$ 1,00" % (a))