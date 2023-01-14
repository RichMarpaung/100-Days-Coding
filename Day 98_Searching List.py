print('##  Program Python Pencarian List / Array  ##')
print('=============================================')
print()
  
n = int(input('Input jumlah element list: '))
print()
 
print('Input',n,'angka (dipisah dengan enter): ');
 
# simpan setiap angka yang diinput ke dalam list
x = []
for i in range(n):
  print('Angka ke-',i+1,': ',sep='',end='')
  x.append(int(input()))
 
print()
 
num = int(input('Input angka yang akan dicari: '))
  
# proses pencarian element list
for i in range(n):
  if(x[i]==num):
    print('Angka ditemukan pada urutan ke',i+1)
    break
 
if(i+1 == n):
  print('Angka tidak ditemukan')