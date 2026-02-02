import random

target=str(random.randint(1000,9999))
guesses=0
current_guess="0000"

while True:
    current_guess=""
    while len(current_guess)!=4:
        current_guess=input("Enter a 4 digit number: ")
    if current_guess==target:
        break
    mice=0
    men=0
    valid_for_men=["","","",""]
    for i in range(4):
        if current_guess[i]==target[i]:
            mice+=1
        else:
            valid_for_men[i]=target[i]
    for i in current_guess:
        j=0
        flag=False
        while not flag and j<4:
            if i==valid_for_men[j]:
                valid_for_men[j]=""
                men+=1
            j+=1
    print("mice:",mice)
    print("men:",men)
    print()

print()
print("You won!")

