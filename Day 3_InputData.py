#Input Data Dari User

#inputan data ini menghasilkan tipe data string
print("\n",5*"=","Input String",5*"=")
data = input("Masukkan Data : ")
print("Data :",data,type(data))

#untuk mendapatkan inputan data bertipe int, float, bool
#maka di lakukan casting

#input bertipe data integer
print("\n",5*"=","Input Integer",5*"=")
data_int = int(input("Masukkan Angka : "))  
print("Data :",data_int,type(data_int))

#input bertipe data float
print("\n",5*"=","Input Float",5*"=")
data_float = float(input("Masukkan Angka Desimal : "))
print("Data :",data_float,type(data_float))

#input bertipe data bool
print("\n",5*"=","Input Boolean",5*"=")  
data_bool = bool(int(input("Masukkan boolean 0 or 1 : "))) #disini untuk harus di casting ke integer terlebih dahulu 
print("Data :",data_bool,type(data_bool)) 

