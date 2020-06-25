A, B, C = input().split()
 
#kemudian karena default tipe datanya string, harus diubah ke float
A, B, C = float(A), float(B), float(C)
#karena problem kita itu bhaskara formula
#nama lainnya adalah rumus ABC, karena menampilkan akar2nya
# R1 dan R2, kalau imajiner tampil "Impossivel calcular"
#maka nilai dari inputan harus diolah terlebih dahulu
 
bhaskara = B**2-4*A*C #alias untuk diskriminan
if bhaskara < 0 or A == 0: #jika Diskriminan < 0 atau nilai A = 0 (TM)
    print("Impossivel calcular")
else: #kalau nilai bhaskara alias diskriminan < 0
    #R1 dan R2 dicetak 5 angka dibelakang point
    print("R1 = %.5f" % ((-B+bhaskara**0.5)/(2*A))) #akar pertama
    print("R2 = %.5f" % ((-B-bhaskara**0.5)/(2*A))) #akar kedua