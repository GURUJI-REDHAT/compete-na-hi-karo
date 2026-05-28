import subprocess as sp 
b = input("Enter Correct Service Name : ")
a = sp.getoutput(f"systemctl status {b}")

if 'running' in a :
    print(f"{b} service is already Active/Running")
elif 'dead' in a :
    sp.getoutput(f"systemctl restart {b}")
    print(f"Service {b} is restarted Successfully")
