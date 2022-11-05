def prima(x):
    for i in range (2,x):
        if x%i ==0:
            return False
    return True

def bilprima(awal,akhir):
    listku = []
    for x in range (awal,akhir):
        if prima(x):
            listku.append(x)
    return listku


a = int(input('Masukkan Awal : '))
b= int(input('Masukkan Akhir : '))
print(bilprima(a,b))