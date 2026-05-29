import subprocess as sp

a = sp.getoutput("ip -br a | awk '{print $1}'").split("\n")

b = sp.getoutput("ip -br a | awk '{print $2}'").split("\n")



c = sp.getoutput("ip -br a | awk '{print $3}' | egrep -io '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'").split("\n")


d = sp.getoutput("ip a | grep 'link/ether' | awk '{print $2}'")
print("Mac Address of Device : " ,d, "\n \n")

for i in range(0,len(a)):
    print(f"Interface : {a[i]} -- Status : {b[i]} -- IP : {c[i]}")
