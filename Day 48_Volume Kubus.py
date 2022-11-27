def volume (sisi):
    vol = sisi**3
    if vol % 2 ==1 and vol % 2 ==0:
        return int(vol)
    else:
        return round(vol,1)
sisi = float(input("Masukkan Panjang Sisi (cm): "))
if sisi % 2 ==1 or sisi % 2 ==0:
    sisi = int(sisi)

print(40*"=")
print(f"Panjang sisi \t: {sisi} cm")
print(f"Rumus Volume Kubus adalah : Sisi * Sisi * Sisi")
print(f"Volume Kubus adalah {sisi} cm * {sisi} cm * {sisi} cm = {volume(sisi)} cm³")
print(40*"=")