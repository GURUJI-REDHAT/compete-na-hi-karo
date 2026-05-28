import subprocess as sp

#a = sp.getoutput("df / | awk '{print $5}' | tail -1 | egrep -io '[0-9]{1,3}'")
a =86
print(a)
sp.getoutput("touch /var/log/disk_alert.log")
if int(a) > 79 :
    with open ('/var/log/disk_alert.log' , 'a') as f :
        f.writelines("Alert storage is about to full \n")
else :
    print("Storage is usable")


