import random

money=1
def select_option():
    return ["cherry","bell","lemon","orange","star","skull"][random.randint(0,5)]

while money>0:
    if input("do you want to roll? ")!="y":
        break
    freqs={
        "cherry":0,
        "bell":0,
        "lemon":0,
        "orange":0,
        "star":0,
        "skull":0
        }
    for i in range(3):
        freqs[select_option()]+=1
    print(freqs)
    if freqs["bell"]==3:
        money+=5
    elif freqs["skull"]==3:
        money=0
    elif freqs["skull"]==2:
        money-=0.5
    elif 3 in freqs.values():
        money+=1
    elif 2 in freqs.values():
        money+=0.5
    money-=0.2
    money=round(money,2)
    print("current money = ",money)
        
