print('##  Program Python Cari Nilai Terbesar  ##')
print('==========================================')
print()
  
n = int(input('Input jumlah element list: '))
print()
 
print('Input',n,'angka (dipisah dengan enter): ')
 
# simpan setiap angka yang diinput ke dalam list
x = []
for i in range(n):
  print('Angka ke-',i+1,': ',sep='',end='')
  x.append(int(input()))
 
print()
 
# proses mencari nilai terbesar
max_num = x[0]
for i in range(1,n):
  if(x[i] > max_num):
    max_num = x[i]
   
print('Angka terbesar adalah:', max_num)