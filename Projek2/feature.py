from json import load, dump
from os import system
from getpass import getpass
from time import sleep

fileUser = 'user.json'
fileProduk = 'produk.json'

user = {}
produk = {}

def loadData():
	global user, produk

	with open(fileUser) as f:
		user = load(f)

	with open(fileProduk) as f:
		produk = load(f)

	return True

def saveData():
	global user, produk

	with open(fileUser, 'w') as f:
		dump(user, f)

	with open(fileProduk, 'w') as f:
		dump(produk, f)

	return True

def login():
	counter = 1
	Username = input('Masukkan Username : ')
	Password = input('Masukkan Password : ')
	dataCheck = False
	passLogin = False
	if Username in user:
		dataCheck = True
		passLogin = (user[Username] == Password)

	while (not dataCheck) or (not passLogin):
		counter += 1
		if counter > 3:
			return False
		print('Nama atau Password Salah. Silahkan Coba Lagi!')
		Username = input('Masukkan Username : ')
		Password = input('Masukkan Password : ')
		if Username in user:
			dataCheck = True
			passLogin = (user[Username] == Password)
	else:
		print('Berhasil Login!')
		return True

def cetak_menu():
	print('Selamat Datang di Aplikasi Pengecek Barang')
	print('1. Cetak Barang')
	print('2. Tambah Barang')
	print('3. Menghapus Barang')
	print('4. Mengubah Harga Barang')
	print('5. Melihat Harga Barang')
	print('Q. Keluar')

def cetak_barang():
	if len(produk) > 0:
		for info in produk:
			print(f'Nama Barang \t: {info}\t Harga \t: {produk[info]}')
	else:
		print('Tidak Ada Barang Tersedia Sekarang.')

def tambah_barang():
	print('Menambah Barang\n')

	barang = input('Nama Barang \t: ')
	harga = input('Harga Barang(per dus) \t: ')

	produk[barang] = harga
	saveData()
	print('Menyimpan Barang...')
	sleep(1.5)
	print('Data Tersimpan!')

def hapus_barang():
	print('Menghapus Barang\n')

	barang = input('Nama Barang \t:')

	if barang in produk:
		del produk[barang]
		saveData()
		print('Menghapus Barang...')
		sleep(1.5)
		print('Data Tersimpan.')
	else:
		print(f'{barang} Tidak Tersedia di Aplikasi Ini!')

def ubah_harga():
	print('Mengubah Harga Produk\n')

	barang = input('Masukkan Nama Barang \t: ')

	if barang in produk:
		print(f'Harga Lama : {produk[barang]}')
		harga = input('Harga baru : ')

		produk[barang] = harga

		saveData()
		print('Mengganti Harga...')
		sleep(1.5)
		print('Data Tersimpan.')
	else:
		print(f'{barang} Tidak Tersedia Di Aplikasi Ini!')


def lihat_harga():
	print('Melihat Harga\n')

	barang = input('Barang \t: ')

	if barang in produk:
		print(f'Barang \t: {barang}\t Harga \t:{produk[barang]}')
	else:
		print(f'{barang} Tidak Tersedia di Aplikasi Ini!')	


	