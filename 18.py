import subprocess as sp

a = input("Enter the Subnet to Ping : ").split(".")
print(a)
b = ""
for i in range(0,3) :
    b +=a[i]
    b +='.'
print(b)

for i in range(1,255):
    c=sp.getoutput(f"ping -c 1 -W 1 {b}{i}")
    if '0 received' in c :
        continue
    else :
        print(f"Live : {b}{i}")


