'''Cara Cara Membuat Array atau List'''
#LIST
#List Numerik
from traceback import print_tb


data_angka = [1,2,3,4,5]
print(f"List angka : {data_angka}")

#list String
data_string = ['rich','rona','marpaung']
print(f"List string:{data_string}")

#list boolean
data_boolean = [True,False,False,False,True]
print(f"List Boolean : {data_boolean}")

#List Campuran
data_campuran = [1,'rich',2,'rona',3,'marpaung',True]
print(f"List Campuran : {data_campuran}\n")

'''Cara lain membuat list menggunakan Range dan For'''
#menggunakan Range
data_range = range(0,10) #Bagian ini tidak akan menghasilkan List
print(data_range)
data_list_range = list(data_range)  #<- ini digunakan untuk menghasilkan list 
print(f"List Menggunakan range: {data_list_range}")

#mengguanak FOR
data_for = [i for i in range(0,10)]
print(f"List Menggunakan For : {data_for}\n")

#mengguanakan FOR IF
#Membuat list bilangan ganjil dan genap
data_ganjil = [i for i in range(0,10) if i%2!=0]#ini akan menghasilan angka ganjil
print(f"List angka ganjil : {data_ganjil}")
data_genap = [i for i in range (0,10) if i%2==0]#ini akan menghasilkan angka genap
print(f"List Angka Genap : {data_genap}")
