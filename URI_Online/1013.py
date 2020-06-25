abc = input().split(" ")

a, b, c = abc

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
hasil = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%i eh o maior" %hasil)