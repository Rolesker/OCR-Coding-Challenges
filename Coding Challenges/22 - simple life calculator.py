
def times_table(n):
    for i in range(12):
        print(i+1,(i+1)*n)

def vat(amount,s):
    if s=="Standard":
        return amount*0.8
    elif s=="Reduced":
        return amount*0.95
    else:
        return amount

def tax(amount):
    if amount<12570:
        return amount
    elif amount>=12570 and amount<50270:
        return amount*0.8
    elif amount>=50270 and amount<125140:
        return amount*0.6
    else:
        return amount*0.55
    
while True:
    print("------SIMPLE-LIFE-CALCULATOR-------")
    print("Enter a choice")
    print("1) Times tables")
    print("2) VAT")
    print("3) Tax")
    print("4) Exit")
    choice=0
    while choice not in [1,2,3,4]:
        choice=int(input("Enter choice: "))
    print()
    if choice==1:
        times_table(int(input("Enter the times table you wish to view: ")))
    elif choice==2:
        print(vat(int(input("Enter amount being paid: ")),input("Enter rate (Standard, Reduced or None): ")))
    elif choice==3:
        print(tax(int(input("Enter annual pay: "))))
    else:
        break
    print()