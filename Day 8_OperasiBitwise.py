'''Operasi Bitwise'''
a = 9
b = 5
#Bitwise AND
print("\n=======AND=======")        #menggunakan tanda &
c = a & b
print('Nilai : ',a,',binary : ',format(a,'08b'))
print('Nilai : ',b,',binary : ',format(b,'08b'))
print('-----------------------------------(&)')
print('Nilai : ',c,',binary : ',format(c,'08b'))

#Bitwises OR
print("\n=======OR=======")        #menggunakan tanda |
c = a | b
print('Nilai : ',a,',binary : ',format(a,'08b'))
print('Nilai : ',b,',binary : ',format(b,'08b'))
print('-----------------------------------(|)')
print('Nilai : ',c,',binary : ',format(c,'08b'))

#Bitwise XOR
print("\n=======XOR=======")        #menggunakan tanda ^
c = a ^ b
print('Nilai : ',a,',binary : ',format(a,'08b'))
print('Nilai : ',b,',binary : ',format(b,'08b'))
print('-----------------------------------(^)')
print('Nilai : ',c,',binary : ',format(c,'08b'))

