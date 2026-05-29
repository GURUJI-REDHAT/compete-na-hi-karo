import re 

a = "fardin@gamil.com,192.168.74.32, https://www.fardin.com ,http://fab.com"

ipr= r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
emr= r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-z]{2,}'
urr= r'https?://[\S]+'
b =re.findall(ipr,a)
c =re.findall(emr,a)
d =re.findall(urr,a)
print("IP : ",b, "Email : ",c, "Url : ",d)
