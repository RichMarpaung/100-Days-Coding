def angka_hari (hari):
    if hari == 'senin':
        return 1
    elif hari == "selasa":
        return 2
    elif hari == "rabu":
        return 3
    elif hari == "kamis":
        return 4
    elif hari == "jumat":
        return 5
    elif hari == "sabtu" :
        return 6
    elif hari == "minggu":
        return 7
def hari_angka (angka):
    if angka == 1:
        return "senin"
    elif angka == 2:
        return "selasa"
    elif angka == 3:
        return "rabu"
    elif angka == 4 :
        return "kamis"
    elif angka == 5:
        return "jumat"
    elif angka == 6:
        return "sabtu"
    elif angka == 7 :
        return "minggu"

hari = input("masukkan nama hari : ").lower()
jarak = int(input("masukkan jarak hari : "))
hari_lanjut = jarak%7

hasil = angka_hari(hari)+hari_lanjut
if hasil > 7 :
    hasil -= 7

print(f"{jarak} hari dari hari {hari} adalah hari {hari_angka(hasil)}")