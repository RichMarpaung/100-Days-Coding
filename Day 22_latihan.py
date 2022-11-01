#1
print('No1')
x = 1
y = 2
z = 3
print(f"data{x,y,z}")
print(f"pertukaran : {y,z,x}")

#2
print('\nNo2')
nama_depan = input("Masukkan Nama Depan : ")
nama_belakang = input("Masukkan Nama Belakang : ")
almt = input('masukkan alamat : ')
no_tlp = input('masukkan no hp')
berat = float(input('berat badan (kg) : '))
umur = input('masukkan umur : ')
print('\nBiodata')
print(f"nama depan = {nama_depan}\nnama belakang : {nama_belakang}\nAlamat : {almt}\nNomor hp : {no_tlp}\nberat badan : {berat} Kg\nUmur : {umur} tahun")
#print(f"Alamat : {almt}")
#print(f"no hp : {no_tlp}")
#print(f"berat badan : {berat} Kg")
#print(f"Umur : {umur} tahun")

#3
print('\nNo3')
tinggi = int(input("masukkan tinggi badan (cm) : "))
tahap1 = tinggi - 100
ideal =tahap1 - (0.1*tahap1)
print(f"berat yang ideal dengan tinggi {tinggi} adalah {ideal} Kg")

#4
print('\nNo4')
for i in range (1,100+1):
    if i % 2 == 0:
        print(i,end = ' ')
print()

#5
print('\nNo5')
data = [1,2,3,4,5]
print (data)

#6
print('\nNo6')
x = int(input("masukkan bilangan : "))
hasil = (2*(x**3))+2*x+(15/x)
print(f'menghitung fungsi \n f(x) = 2x^3+2x+15/x')
print(f"f({x})=2*{x}^3+2*{x}+15/{x} = {hasil}")
#7
import time
import os
print('\nNo7')
detik = 60
while detik <= 60:
    if detik <=60 and detik >30:
        print('merah')
        print(detik)
        time.sleep(0.5)
        os.system('cls')
        detik-=1
    elif detik <=30 and detik >= 0:
        print('kuning')
        print(detik)
        time.sleep(1)
        os.system('cls')
        detik-=1
    elif detik < 0  and detik >= -60:
        print('Hijau')
        print(detik+60)
        time.sleep(1)
        os.system('cls')
        detik-=1
    else :
        detik+=121
#8
print('\nNo8')
hewan = ['ayam','ular','kucing','anjing','kelinci','harimau','panda','kangguru','jerapah','singa']
print(hewan)
indeks = hewan.index('ayam')
print(indeks)
print(f'indek ke-3 : {hewan[3]}')
print(f'indek ke-5 : {hewan[5]}')
hewan.pop(6)
print(f'Setalah dihapus : {hewan}')
#9
nama = "Rich Rona Selamat Marpaung"
print(nama)
print(nama.lower())
print(nama.upper())

#10
tinggi = int(input("Masukkan Tinggi N : "))
tinggi = (tinggi//2)+1

print(f'Nilai N : {tinggi}')
titik = 0
for i in range(1,tinggi+1):
    for spasi in range(1,(tinggi-i)+1):
        print(end='  ')
    while titik != ((2*i)-1):
        print('*',end = ' ')
        titik +=1
    titik = 0
    print()
for i in range(tinggi-1,0,-1):
    for spasi in range(1,(tinggi-i)+1):
        print(end='  ')
    while titik != ((2*i)-1):
        print('*',end = ' ')
        titik +=1
    titik = 0
    print()    
