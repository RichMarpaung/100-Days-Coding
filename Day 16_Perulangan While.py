i =     1
while i <= 5:   #program akan berhenti apabila nilai i <= 5 
    print (i)   #mencetak nilai i
    i += 1      #nilai i akan di tambah 1 setiap perulangan dilakukan
print('Loping 1 Selesai\n')

#Membuat Segitiga

panjang = int(input("Masukkan Luas Segitiga : "))
i = 1  
while i <= panjang:
    print('*'*i)
    i+=1

print('Looping 2 Selesai\n')

#segitiga Terbalik
i = 0
while i <= panjang :
    sisi = panjang - i
    print('*'*sisi)
    i+=1

print('Looping 3 selesai\n')


#mencari angka ganjil
print('Angka Ganjil 1-10 :')
i = 1
while i  < 10:
    if i % 2 == 1:
        print(i)
    i+= 1

print('Looping 4 selesai\n')

#mencari angka genap
print('Angka Genap 1-10 : ')
i = 1
while i <10:
    if i % 2 == 0:
        print(i)
    i+=1
print('Looping 5 Selesai')