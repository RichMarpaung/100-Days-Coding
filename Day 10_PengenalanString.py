'''Pengenalan Tipe Data String'''

#Cara Membuat String
'''
    1. Dengan Menggunakan singel quote '.....'
    2. Dengan Menggunakan double quote "....."
'''

#String Dengan Singel Quote '...'


singel_quote = 'Ini Mengguanakan Singel Quote'
print(singel_quote)

#String Dengan Double Quote
double_quote = "Ini Mengguanakan Double Quote"
print(double_quote)

# mengguakan singel quote dan Double quote

gabungan_quote = '"Hallo Apa Kabar?"' 
print(gabungan_quote) #Maka Quote yang ada di dalam akan dibaca menjadi string
gabungan_quote = "'Hallo Apa Kabar?'" 
print(gabungan_quote) #Maka Quote yang ada di dalam akan dibaca menjadi string

# Menggunakan tanda \ 
# membuat tanda ' menjadi string
print('Besok Adalah Hari Jum\'at') #<- petik 1 akan di ubah menjadi string

# membuat tanda \ menjadi string
print ("C:\\User\\Rich\\Document") #<- double \ akan mengubah \ menjadi string

#tab
print("Penggunaan \t \\t akan menjauh")

#backspace
print("Hallo \bDunia") #<- Menghapus 1 karakter ke belakang

#newline
print("baris pertama\nbaris kedua")

#raw string 
print(r"C:\User\Rich\Document") #<Apapun yang di tulis akan di anggap string