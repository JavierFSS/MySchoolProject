from tkinter import Tk, ttk

#membuat sebuah instance / object nyata
my_apps = Tk()

def change_color():
	pass
	"""
	action_button = action.configure(text="Color Has Been Changed!")
	label1.configure(foreground="red")
	label1.configure(text="Hello in Red")
	"""

#title = method dalam object Tk()
my_apps.title("My First Python Apps")
my_apps.resizable(True, True)

#menambahkan label / tulisan
label1 = ttk.Label(my_apps, text="Nama Lengkap \t:").grid(column=0, row=0)
label2 = ttk.Label(my_apps, text="Tempat, Tanggal Lahir \t:").grid(column=0, row=1)
label3 = ttk.Label(my_apps, text="Alamat \t:").grid(column=0, row=2)
label4 = ttk.Label(my_apps, text="Agama \t:").grid(column=0, row=3)
label5 = ttk.Label(my_apps, text="No.Telp \t:").grid(column=0, row=4)

#membuat tombol / button
button1 = ttk.Button(my_apps, text="Change Color", command=change_color).grid(column=0, row=5)

#method untuk memulai GUI Apps
if __name__ == "__main__":
	my_apps.mainloop()