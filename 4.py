import subprocess as sp
#f = input("Enter a Domain ")
a = sp.getoutput("host -t a {f} | awk '{print $4}'").split("\n")
for i in a:
    b = sp.getoutput(f"host -t ptr {i}").split("\n")

print(f"{a}")
print(b)
#for ip in a :
#    c=ip.split(".")
#    print(c[::-1])
