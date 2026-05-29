import subprocess as sp

a = sp.getoutput("cat /var/log/auth.log | grep -i 'failed password' | tail -10")

print(a)
