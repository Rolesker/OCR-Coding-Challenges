import random
money=500

def gamble(bet,wager):
    print()
    value=random.randint(0,30)
    print("The value was "+str(value)+"!")
    if value!=bet:
        return wager*-1
    else:
        if value%2==0:
            wager*=2
        if value%10==0:
            wager*=3
        if value<5:
            wager*=2
        if value in [2,3,5,7,11,13,17,19,23,29]:
            wager*=5
    print("You gained",wager)
    return wager

while money>0:
    print("Current money:",money)
    print("Enter a choice:")
    print("1) Gamble")
    print("2) Quit")
    choice=0
    while choice not in [1,2]:
        choice=int(input("Enter decision: "))
    print()
    if choice==1:
        wager=-1
        while wager<=0:
            wager=int(input("How much money do you want to gamble? "))
        bet=-1
        while bet<=-1 or bet>=31:
            bet=int(input("Select a number between 0 and 30 to place a bet on: "))
        money+=gamble(bet,wager)
    else:
        break
    print()

print("Final money:",money)