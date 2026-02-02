import random

suggested=""
for i in range(8):
    suggested+=chr(random.randint(33,122))
print("Enter a password, or enter the word Suggested (case sensitive) to use the suggested password")
print("Suggested password:",suggested)
choice=""
while choice=="":
    choice=input("Enter here: ")
if choice=="Suggested":
    password=suggested
else:
    password=choice
choice=""
while choice!=password:
    choice=input("Verify password: ")

choice=""
while choice!=password:
    choice=input("Enter password to access file: ")
f=open("24-target.txt","r")
print(f.readline())
f.close()