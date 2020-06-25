totalWaktu = int(input())

Jumlah = [3600, 60, 1]
hasil = []

for item in Jumlah :
	jumlah2 = (totalWaktu / item)
	hasil.append(str(jumlah2))
	totalWaktu -= item * jumlah2

print(":".join(hasil))