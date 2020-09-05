from json import load, dump
from os import system
from time import sleep

import feature

statusLoading = feature.loadData() #True

system('cls')

if statusLoading :
	#print('Pass')
	passLogin = feature.login() #True
	if passLogin:
		print('Selamat Datang!')
		sleep(2)
		menu_choice = ''

		while menu_choice != 'q':
			system('cls')
			feature.cetak_menu()
			menu_choice = input('Ketik Pilihan Dalam Angka : ').lower()

			if menu_choice == '1':
				feature.cetak_barang()
				input('ENTER Untuk Keluar')

			elif menu_choice == '2':
				feature.tambah_barang()
				input('ENTER Untuk Keluar')

			elif menu_choice == '3':
				feature.hapus_barang()
				input('ENTER Untuk Keluar')

			elif menu_choice == '4':
				feature.ubah_harga()
				input('ENTER Untuk Keluar')

			elif menu_choice == '5':
				feature.lihat_harga()
				input('ENTER Untuk Keluar')

			elif menu_choice == 'q':
				print('Terima Kasih Telah Menggunakan Aplikasi Ini!')
				break

			else: 
				print('Ketikkan Pilihan Yang Benar!')
				input('ENTER Untuk Keluar')

	else:
		print('Gagal Untuk Login.')
else:
	print('Aplikasi Tidak Bekerja.')