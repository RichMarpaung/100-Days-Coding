for i in range(2):
    print('i')  #ini akan mengcetak nilai i sebanyak 2 kali

print('\n')
for i in range (1,10): #mencetak 1 sampai 10
    print(i)
print('\n')
for i in range (1,20,3): #akan mecetak 1 dengan di tambah 3 terus sampai 20
    print (i)
print('\n')
for i in range (15,1,-2): #akan mecetak nilai dari i mulai dari 15 dan di kurang 2 hingga 1
    print (i)



'''Mencari Angka Ganjil & Angka Genap'''


#Mencari bilangan Genap
data = int(input("Masukkan Panjang Data : "))
ganjil =[]
genap = []
for i in range(data):
    if i % 2 == 0:
        genap.append(i)

    if i %2==1 :
        ganjil.append(i)

print(f"Angka Genap : {ganjil}")
print(f"Angka Genap : {genap}")

#Membuat Segitiga dengan panjang di tentukan user

panjang = int(input("Masukkan panjang segitiga : "))

for i in range (panjang+1):
    print('*'*i)
    i+=1