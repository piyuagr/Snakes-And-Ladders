import hashlib

s = input("Enter the string: ")
i = 1
s1 = s + str(i)
s1 = hashlib.sha256(s1.encode())

while (s1.hexdigest()) >=  "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff":
    i += 1
    s1 = s+str(i)       
    s1=hashlib.sha256(s1.encode())
    
print(i)
