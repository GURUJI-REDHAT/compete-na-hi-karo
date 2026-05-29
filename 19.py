import subprocess as sp

a = sp.getoutput("ss -tuln | awk '{print $5}' | cut -d ':' -f 2 | egrep -0 '[0-9]{1,}'").split("\n")
print(a)

for i in a :
    if i.isdigit():
       # b =sp.getoutput(f"sudo lsof -i:{i}")
        pid = sp.getoutput(f"sudo lsof -i:{i} | awk '{{print $2}}' | tail -1 ")
        name = sp.getoutput(f"sudo lsof -i:{i} | awk '{{print $9}}' | tail -1")
        print(f"Name : {name} - Pid : {pid} - Port : {i}")




