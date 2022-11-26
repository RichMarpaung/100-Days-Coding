def luas_kubus (sisi):
    luas = 6*sisi*sisi
    if luas % 2 ==1 or luas % 2 ==0:
        return int(luas)
    return luas
sisi = float(input("Masukkan Panjang Sisi (cm): "))
if sisi % 2 ==1 or sisi % 2 ==0:
    sisi = int(sisi)

print(40*"=")
print(f"Panjang sisi \t: {sisi} cm")
print(f"Rumus Luas Kubus adalah : 6 * Sisi * Sisi")
print(f"Luas Kubus adalah 6 * {sisi} cm * {sisi} cm = {luas_kubus(sisi)} cm²")
print(40*"=")