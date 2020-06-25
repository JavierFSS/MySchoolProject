abcd = input().split(" ")

A, B, C, D = abcd

if B > C and D > A and (C+D) > (A+B) :
	print("Valores aceitos")
else :
	print("Valores nao aceitos")
