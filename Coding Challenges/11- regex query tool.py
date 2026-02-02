import re

txt=input("Enter text you will be querying: ")
txt2=input("Enter string being searched for: ")
choice=0
while choice not in [1,2,3]:
    print("Select what you want the result of the query to be")
    print("1) List of all matches")
    print("2) Removing all matches and splitting remaining text into a list")
    print("3) Replacing all matches with another piece of text")
    choice=int(input("Enter here: "))
if choice==1:
    print(re.findall(txt2,txt))
elif choice==2:
    print(re.split(txt2,txt))
else:
    extra_txt=input("Enter text to replace with: ")
    print(re.sub(txt2,extra_txt,txt))
