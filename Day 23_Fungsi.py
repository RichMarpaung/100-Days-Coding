#Praktikum 
def hello(nama) :                           #deskripsi fungsi
    print(f"Hai {nama}!, Apa kabar?")       #isi fungsi

hello("rich")                               #Pemanggilan Fungsi


def kenal (nama,asal,kuliah):
    print(f"\nHai, nama saya {nama}, asli dari {asal}, sekarang kuliah di {kuliah}")

kenal('rich','medan','Unsulbar')

def suhu (daerah,suhu,satuan = "Celcius"):
    print(f"Cuaca di {daerah} saat ini {suhu} {satuan}")

suhu ("majane",30)
suhu("majane", 53,"Fahrenheit")

#Tugas Praktikum

print('\n============Tugas Praktikum==============')
'''Menampilkan hasil modulo dengan menggunakan Fungsi'''
def modulo (angka1,angka2):
    hasil = angka1%angka2
    return hasil

angka1 = 17
angka2 = 3
print(f"{angka1} % {angka2} = {modulo(angka1,angka2)}")

'''Perkalian dari nilai Fungsi di atas dengan parmeter tertentu '''
def perkalian (fungsi1,nilai):
    hasil_kali = fungsi1*nilai
    return hasil_kali
fungsi1 = modulo(angka1,angka2)     #Pendeklarasian fungsi modulo ke dalam variabel fungsi1
nilai = 8

print(f"\n{fungsi1} * {nilai} = {perkalian(fungsi1,nilai)}")

'''Fungsi  untuk mengambil 2 bil integer sehingga membentuk persegi'''
print('\n')
def persegi(p,l):
    for i in range(p):
        print("*"*l)

p = int(input("Masukkan Panjang : "))
l = int(input("Masukkan Lebar :"))

persegi(p,l)