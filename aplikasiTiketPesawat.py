from os import system


def print_menu():
	system("cls")
	menu_tampilan = """
	----------------------
	APLIKASI TIKET PESAWAT
	----------------------
	[A]. Tambah Profile / Check In
	[B]. Penambahan Tiket Pesawat
	[C]. Cari Profile 
	[D]. Cari Tiket Pesawat
	[E]. Keluar Aplikasi
	"""
	print(menu_tampilan)

def searching(profile):
	if profile in data_profile:
		print(f"""
		-DATA DITEMUKAN-
	Nama:{profile}
	Umur:{data_profile[profile]["umur"]}
	Telp:{data_profile[profile]["telp"]}
	KTP: {data_profile[profile]["ktp"]}
	Asal Negara: {data_profile[profile]["asal_negara"]}
			""")
	input("Tekan ENTER untuk kembali ke MENU")


def tambah_profile():
	system("cls")
	print("Menambahkan Profile\nInformasi Profile")
	nama = input("Nama\t:")
	umur = input("Umur\t:")
	telp = input("Telp\t:")
	ktp = input("KTP\t:")
	negara = input("Asal Negara\t:")
	respon = input(f"Yakin ingin menyimpan {nama} ? (Y/N) ")
	if respon.upper() == "Y":
		data_profile[nama] = {
			"umur" : umur,
			"telp" : telp,
			"ktp" : ktp,
			"asal_negara" : negara
		}
		print("Data Profile Tersimpan.")
	else:
		print("Batal menyimpan.")
	input("Tekan ENTER untuk kembali ke MENU")

def penambahan_tiket_pesawat():
	system("cls")
	print("Menambahkan Tiket Pesawat\nInformasi Tiket Pesawat")
	tanggal_keberangkatan = input("Tanggal Keberangkatan\t:")
	print("[1]. Garuda Indonesia , [2]. Citilink , [3]. Lion Air")
	respon = input("Pesawat yang akan di naik :")
	if respon == "1":
		print("Selamat Menikmati Penerbangan bersama Garuda Indonesia")
	elif respon == "2":
		print("Selamat Menikmati Penerbangan bersama Citilink")
	elif respon == "3":
		print("Selamat Menikmati Penerbangan bersama Lion Air")
	input("Tekan ENTER untuk kembali ke MENU utama")

def cari_profile():
	system("cls")
	nama = input("Nama yang akan dicari : ")
	result = searching(nama)

def cari_tiket_pesawat():
	pass

def check_input(char):
	char = char.upper()
	if char == "E":
		return True 
	elif char == "A":
		tambah_profile()
	elif char == "B":
		penambahan_tiket_pesawat()
	elif char == "C":
		cari_profile()
	elif char == "D":
		cari_tiket_pesawat()



data_profile = {
	'Nez' : {
		'umur' : '15',
		'telp' : '0812',
		'ktp' : '00',
		'asal_negara' : 'Jepang'
	},
	'Dita' : {
		'umur' : '21',
		'telp' : '0812',
		'ktp' : '00',
		'asal_negara' : 'Indonesia'
	}
}
stop = False


while not stop:
 print_menu()
 user_input = input("Pilihan : ")
 stop = check_input(user_input)