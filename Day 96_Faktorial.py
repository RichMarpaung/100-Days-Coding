print('##  Program Python Menghitung Faktorial  ##')
print('===========================================')
print()
  
angka = int(input('Input angka: '))
 
hasil = 1
for i in range(1,angka+1):
  hasil = hasil * i
 
print(angka,'! = ', hasil)
