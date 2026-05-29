import subprocess as sp

a = sp.getoutput("openssl aes-256-cbc -in 13.py -out 13.enc -pass pass:1234")
print("Data is Encrypted Successfully")

b = sp.getoutput("openssl aes-256-cbc -d -in 13.enc -out 13.txt -pass pass:1234")
print("Data is Decrypted Successfully")
