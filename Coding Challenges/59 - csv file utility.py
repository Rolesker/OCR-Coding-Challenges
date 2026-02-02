import csv

#file=input("Enter name of file (don't forget the .csv!) ")
file="59 - sample file.csv"
records=[]

with open(file,newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    print("Your CSV file:")
    for row in reader:
        print(row)
        records.append(row)
    print()

def sortby(feild):
    return sorted(records,key=lambda x:x[feild])

print("Three feild names have been identified:")
for i in records[0].keys():
    print(i)
chosen_feild="slakdjsalkdjsaldjaslkdjlajdlkajdlajdalsjdsalj"
while chosen_feild not in records[0].keys():
    chosen_feild=input("Choose a feild to sort by ")

records=sortby(chosen_feild)

with open(file,"w",newline="") as csvfile:
    fieldnames=records[0].keys()
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in records:
        writer.writerow(i)
print("File has been updated")
