'''Operasi Logika'''
#not, or, and,xor0
a = True
b = False
print("==========NOT===========")
print (f"a = {a}")
print(f"b = {b}")
print(f"not a = {not a}")
print(f"not b = {not b}")

print ("\n=========OR==========")
print(f"{a} or {b} = {a or b}")
print(f"{b} or {a} = {b or a}")
print(f"{a} or {a} = {a or a}")
print(f"{b} or {b} = {b or b}")

print ("\n=========AND==========")
print(f"{a} and {b} = {a and b}")
print(f"{b} and {a} = {b and a}")
print(f"{a} and {a} = {a and a}")
print(f"{b} and {b} = {b and b}")

print ("\n=========xor==========")         #Akan true apabila satu bernilai True
print(f"{a} xor {b} = {a ^ b}")            #apabila ada 2 true akan menjadi false
print(f"{b} xor {a} = {b ^ a}")
print(f"{a} xor {a} = {a ^ a}")
print(f"{b} xor {b} = {b ^ b}")
