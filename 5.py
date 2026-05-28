import subprocess as sp
import hashlib as h

l = ['@','$','!']
a = input("Enter the Password : ")
up=any(i.isupper() for i in a )
dn=any(i.islower() for i in a )
dg=any(i.isdigit() for i in a )
sc = False
for i in a:
    if i in l :
        sc = True
if up and dn and dg and sc and len(a) >= 8:
    print("Strong Password")
else :
    print("Weak Password")
    
b = a.encode('UTF-8')
c = h.sha256(b).hexdigest()

print(c)

e = input("Enter to check if Corrcet : ")
f = h.sha256(e.encode('UTF-8')).hexdigest()

if c == f:
    print("Password Match Successfully ")
else :
    print("Password is not Matched ")
