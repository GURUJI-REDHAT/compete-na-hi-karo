import subprocess as sp

a = sp.getoutput("cat /var/log/apache2/access.log ").split("\n")
print("The total Number of requests :" ,len(a))

b = sp.getoutput("cat /var/log/apache2/access.log | grep -i '404'").split("\n")
print("The total Number of 404 Errors : ",len(b))


c = sp.getoutput("cat /var/log/apache2/access.log | egrep -io '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'").split("\n")
d = {}

for ip in c:
    if ip in d:
        d[ip] += 1
    else :
        d[ip] = 1
for key,value in d.items():
    print(f"The Ip is {key} and the NUmber of Occurance  {value}")



