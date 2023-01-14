import math
 
print('##  Program Python Mencari Akar Persamaan Kuadrat  ##')
print('=====================================================')
print()
print('Format persamaan: ax^2 + bx + c = 0')
 
a = int(input('Input nilai a: '))
b = int(input('Input nilai b: '))
c = int(input('Input nilai c: '))
print()
 
D = (b*b)-(4*a*c)
print('Diskriminan =',D,end='')
 
if (D > 0):
  print(' (akar real dan berbeda)');
  x1 = (-b + math.sqrt(D)) / (2*a)
  x2 = (-b - math.sqrt(D)) / (2*a)
      
  print('x1 =',round(x1,2))
  print('x2 =',round(x2,2))
elif (D == 0):
  print(' (akar real dan sama)');
  x1 = (-b + math.sqrt(D)) / (2*a)
  x2 = x1
  
  print('x1 = ',round(x1,2))
  print('x2 = ',round(x2,2))
else:
  print(' (akar tidak real / imajiner)');