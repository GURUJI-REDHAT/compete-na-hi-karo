import subprocess as sp 

#a = sp.getoutput("cat /var/log/auth.log | grep -i 'failed password'")

b = sp.getoutput("cat /var/log/auth.log | grep -i 'failed password' | awk '{print $11}'").split("\n")

d = {}

for ip in b :
    if ip in d :
        d[ip] += 1
    else :
        d[ip] = 1

for i,j in d.items():
    if j >= 5:
        print(f"Suspicious IP : {i} ({j} time login Attempts)")
