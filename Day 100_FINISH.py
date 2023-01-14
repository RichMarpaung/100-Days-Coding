print('##  Program Python Menghitung Jumlah Huruf Vokal  ##')
print('====================================================')
print()
  
x = input('Input kata / kalimat: ').lower()
print()
 
# Hitung jumlah huruf vokal
vokal = 0
for i in x:
  if(i=='a' or i=='i' or i=='u' or i=='e' or i=='o'):
    vokal = vokal + 1
 
# Tampilkan total huruf vokal jika ditemukan
if vokal > 0 :
  print('Jumlah huruf vokal =', vokal)
else:
  print('Huruf vokal tidak ditemukan')