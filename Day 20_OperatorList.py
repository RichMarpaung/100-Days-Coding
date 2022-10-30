'''Operator List'''
#Menampilkan Index Data
data = ['rich','rona','selamat','marpaung']
lokasi = data.index('selamat') # Menampilkan data 'selamat' berada index keberapa
print(f'Data "selamat" berada pada index : {lokasi}\n')

#Menambah Data
data = ['rich','rona','marpaung']
print(f"Data awal : {data}")
data.append('selamat') #menambah data 'selamat' pada urutan akhir list
print(f"Data di tambah : {data}\n")

#Menghapus Data
data = ['rich','rona','selamat','marpaung']
print(f"Data Awal : {data}")
data.remove('marpaung')
print(f"Data Setelah di hapus : {data}\n")

#MEnyisipkan Data
data = ['rich','rona','marpaung']
print(f"Data awal : {data}")
data.insert(2,'Selamat') #menyisipkan 'Selamat' ke index 2
print(f"Data setelah insert :{data}\n")

#Mengurutkan Data Terkecil ke terBesar
data = [13,5,2,1,4,3,6,8,7,9,10]
data.sort()
print(f"Data terkecil ke terbesar {data}")

#Mengurutkan Data terbesar ke terkecil
data = [13,5,2,1,4,3,6,8,7,9,10]
data.sort(reverse=True)
print(f"Data terbesar ke terkecil {data}\n")

#Membalikkan Urutan List dari belakang ke depan
data =[1,2,3,43,5,6,7]
print(f"data awal {data}")
data.reverse()
print(f"Data revers {data}\n")

#Menghitung berapa kali data muncul
data = [2,3,4,3,4,5,3,4,3,7,6,1,8]
muncul = data.count(3) #Menghitung nilai 3 muncul berapa kali
print(data)
print(f"Angka 3 muncul : {muncul} kali")

#