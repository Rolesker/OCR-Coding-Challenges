# note to anyone reading, I could only be bothered to do the 1st extension
user_data={}

def enter_credentials():
    name=input("Enter the name you would like to use: ")
    dob=input("Enter your date of birth: ")
    plan=input("Enter the kind of membership plan you would like to subscribe to: ")
    number=input("Enter your phone number: ")
    reason=input("Give a short description on how you got into rock climbing: ")
    user_data[name]={"Date Of Birth":dob,"Membership Plan":plan,"Phone Contact":number,"Description":reason}
    print("Entry successful! Returning to menu")
    print()

def display_record():
    query=input("Enter the username of the record you would like to check: ")
    if user_data.get(query)==None:
        print("ERROR: User does not exist, returning to menu")
        print()
        return
    print("-------"+query+"-------")
    for i in user_data[query]:
        print(i," - ",user_data[query][i])
    print()

while True:
    print("------------WELCOME-USER-------------")
    print("What would you like to do? (select an option)")
    print("1) Enter a membership")
    print("2) Query a membership")
    print("3) Exit")
    choice=4
    while choice not in [1,2,3]:
        choice=int(input("Enter your choice here: "))
    print()
    if choice==1:
        enter_credentials()
    elif choice==2:
        display_record()
    else:
        break