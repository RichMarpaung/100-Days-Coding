'''FORMAT STRING'''

#Contoh Penggunaan Format String
#String
nama = "Rich"
format_str = f"Nama = {nama}" #<- Nilai Variabel nama akan di masukkan ke dalam string
print (format_str)

#angka
angka = 2002.23
format_str = f"angka = {angka}"
print(format_str)

#boolean
boolean = True
format_str = f"Boolean = {boolean}"
print(format_str)

#Bilangan Bulat
angka = 23
format_str = f"Bilangan Bulat : {angka:d}"#<- d disini menandakan bilangan bulat
print(format_str)

#Bilangan ribuan dan jutaan
ribuan = 2000
format_str = f"Bilangan Ribuan : {ribuan:,}"#<- ',' koma ini menandakan ribuan
print(format_str)
jutaan = 23000000
format_str = f"Bilangan jutaan : {jutaan:,}"#<- ',' koma ini menandakan ribuan
print(format_str)

#Bilangan Desimal / tipe data float
desimal = 23.52547822323
format_str = f"Bilangan Desimal : {desimal:.3f}"#<'.3f' maksudnya 3 angka di belakang titik float
print(format_str)

#Leading zero
desimal = 23.52547822323
format_str = f"Bilangan Desimal : {desimal:09.3f}"#<- total jumlah huruf 9 apabila kurang dari 9 maka akan di tambah 0 di depan
print(format_str)

#Menampilkan Plus Minus
angak_Minus = -23
angka_plus = +23.65722

format_minus = f"minus = {angak_Minus:+}"#<- '+' disini untuk menampilkan nilai positif atau negattif
format_plus = f"plus = {angka_plus:+.2f}" #<- Perpaduan bilangan desimal dengan plus minus
print(format_minus)
print(format_plus)
#Persentase
persen = 0.032
format_persen = f"persen : {persen:.2%}"#<- angka 2 disini menunjukkan angka di belakang desimal
print(format_persen)

