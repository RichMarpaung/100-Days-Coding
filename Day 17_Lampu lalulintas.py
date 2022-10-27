import os
import time 

os.system('cls')

waktu = 60

while  True:
    if waktu >=30 and waktu <=60:
        print('Merah')
        print(waktu)
        time.sleep(1)
        waktu -=1
        os.system('cls')
    elif waktu <30 and waktu >=0:
        print('Kuning')
        print(waktu)
        time.sleep(1)
        waktu -=1
        os.system('cls')
    elif waktu <0 and waktu >= -60:
        print('Hijau')
        print(waktu+60)
        waktu -=1
        time.sleep(1)
        os.system('cls')
    else:
        waktu += 120