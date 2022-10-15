print("="*10,"Casting Type Data","="*10)
print("Casting Tipe data adalah mengubah jenis tipe data\n")

print("="*10,"Integer","="*10)#Casting Dari Int ke String, Float, dan Boolean
data_awal = 23
print(f"Data awal : {data_awal}, Tipe data : {type(data_awal)}")
data1 = str(data_awal)
data2 = float(data_awal)
data3 = bool(data_awal) #tipe bool akan False jika data nya bernilai 0
print(f"Data 1: {data1}\t, Tipe data : {type(data1)}")
print(f"Data 2: {data2}\t, Tipe data : {type(data2)}")
print(f"Data 3: {data3}\t, Tipe data : {type(data3)}")

print("="*10,"Float","="*10) #Casting Dari Float ke String, Integer, dan Boolean
data_awal = 23.7
print(f"Data awal : {data_awal}, Tipe data : {type(data_awal)}")
data1 = str(data_awal)
data2 = int(data_awal) #Disini Bilangan Float akan di sederhanakan kebawah
data3 = bool(data_awal)
print(f"Data 1: {data1}\t, Tipe data : {type(data1)}")
print(f"Data 2: {data2}\t, Tipe data : {type(data2)}")
print(f"Data 3: {data3}\t, Tipe data : {type(data3)}")

print("="*10,"String","="*10) #Casting Dari String ke Integer, Float, dan Boolean
data_awal = "105"
print(f"Data awal : {data_awal}, Tipe data : {type(data_awal)}")
#Program akan Error apa bila Data awal merupakan huruf saat casting str > int,float
data1 = int(data_awal)
data2 = float(data_awal)
data3 = bool(data_awal) #Data akan False apabila String nya kosong 
print(f"Data 1: {data1}\t, Tipe data : {type(data1)}")
print(f"Data 2: {data2}\t, Tipe data : {type(data2)}")
print(f"Data 3: {data3}\t, Tipe data : {type(data3)}")

print("="*10,"Boolean","="*10) #Casting Dari Boolean ke String, Float, dan Integer
data_awal = True
print(f"Data awal : {data_awal}, Tipe data : {type(data_awal)}")
data1 = int(data_awal)
data2 = float(data_awal) 
data3 = str(data_awal)
print(f"Data 1: {data1}\t, Tipe data : {type(data1)}")
print(f"Data 2: {data2}\t, Tipe data : {type(data2)}")
print(f"Data 3: {data3}\t, Tipe data : {type(data3)}")