#Manipulasi dan Operator String

#1. Menyambung 2 buah string
string1 = "Rich"
string2 = "Rona"
string3 = "Marpaung"
print ("string1 : ",string1)
print ("string2 : ",string2)
print ("string3 : ",string3)

string_lengkap = string1 + " " + string2 +" "+string3
print("String Gabungan = ", string_lengkap)

# 2. Menampilkan Panjang String

nama = "Rich Rona S Marpaung" #<- Spasi Dihitung sebagai string
panjang_string = len(nama)

print(nama,"\nMemiliki Panjang :",panjang_string)

# 3. Mengecek kata dalam string
nama = "Rich Rona S Marpaung"
cek1 = "Rich" 
cek2 = "Sinaga" 
status1 = cek1 in nama  #<- Dalam Pengecekan Huruf kapital sangat berpengaruh
status2 = cek2 in nama
print ("kata",cek1,"Ada di : ",nama,"=",str(status1))
print ("kata",cek2,"Ada di : ",nama,"=",str(status2))

# 4. Mengulang String
print("ha"*5)
print(5*"wk")

# 5. Index String
nama = "Rich Rona S Marpaung"
print(nama)
print ("Index String ke 0 :", nama[0])
print ("Index String ke 7 :", nama[7])
print ("Index String ke : -1", nama[-1]) #<- Mengambil String Dari Belakang
print ("Index String 0 sampai 4",nama[0:4]) #<- Yang di ambil 0 sampai sebelum 4
print ("Index String ke [0,2,4,6,8,10] :", nama[0:10:2])#<- 2 disini maksudnya di lompatin 2

# 6. Mengecek Jumlah Huruf
nama = "Rich Rona S Marpaung"
jumlah_huruf = nama.count('R')
print("Jumlah 'R' dalam :",nama," = ",jumlah_huruf) #<-Huruf Kapital berpengearuh dalah pengecekan
