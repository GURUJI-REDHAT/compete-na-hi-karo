import subprocess as sp
a = sp.getoutput("crontab -l")
print(a)

b = input("Name a Job to Check If Exist :")
if b in a :
    print("Current Job is scheduled for This User")
else :
    print("This Job is not Scheduled ")
