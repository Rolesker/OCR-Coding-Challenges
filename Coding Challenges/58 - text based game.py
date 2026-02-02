import time
import sys

print("----------- GLYMBO'S GOLD -----------")
while input("Type start to start: ")!="start":
    pass

def text_reader(txt):
    for i in txt:
        print(i)
        time.sleep(len(i)//20)

def present_options(options):
    print()
    print("You have the following choices:")
    for i in range(len(options)):
        print(str(i+1)+") "+options[i])
    choice=-1
    while choice<0 or choice>len(options):
        choice=int(input("Enter a number to make a choice: "))
    return choice

def glymbo_dialouge():
    if inventory["gold"]:
        text_reader(["You: Mr goblin, I have some gold for you!",
                     "Glymbo: Wowee!! For me? This is my favourite gift, I am so honoured.",
                     "Glymbo: Human, I forgive your crimes. I absolve you. You may leave.",
                     "",
                     "Congratulations, you have won and escaped the dungeon!"])
        sys.exit()
    else:
        text_reader(["You: Erm excuse me, why have you placed me here sir?",
                     "Glymbo: Human, come no closer! You have been imprisoned for your crimes against goblin kind.",
                     "You: Crimes against goblin kind?? I have done no such thing sir, you must be mistaken.",
                     "Glymbo: Yesterday during your walk through the forest, you stepped on one of our good allies.",
                     "Glymbo: You stepped on a gnome.",
                     "You: Please mr guard sir, it was an accident I swear's it! Please let me go!",
                     "Glymbo: No chance. Unless maybe... you have some gold for me? We goblins love gold, you see...",
                     "You: I don't think I do have any gold the last time I checked... but I can try and get some."])

def goat_dialouge():
    if inventory["key"]:
        text_reader(["Goat: I already gave you the key.",
                     "Goat: Just leave me alone already!"])
    elif inventory["lettuce"]:
        text_reader(["Goat: Human, is that lettuce I smell?",
                     "Goat: It smells amazing!! Give it to me... and I will excrete the key held in the inner depths of my body...",
                     "You give the lettuce to the goat, and it produces a key.",
                     "A key has been added to your inventory!"])
        inventory["key"]=True
    else:
        text_reader(["You: Excuse me goat, have you seen any gold around?",
                     "Goat: No, I haven't. I am just a goat, I know nothing about any gold.",
                     "Goat: I'll tell you what I do know, this grass is so lousy, I wish I could eat something tastier.",
                     "Goat: I got so desperate, I even ate a key! It's dark days for me...",
                     "You: I am sorry to hear that."])

def farmer_dialouge():
    if inventory["lettuce"]:
        text_reader(["You: I am sorry mr farmer, I can't really help your situation.",
                     "Farmer: I have been here for many years... Do not feel bad, for my hope has already vanished.",
                     "You: Sorry mr farmer. Thanks for the lettuce."])
    else:
        text_reader(["You: Hello? Are you alright?",
                     "Farmer: No, I am not. I got imprisoned for supposedly stealing vegetables from a goblin.",
                     "Farmer: But I wasn't, they were mine! No one believes me!",
                     "Farmer: They chained me up for complaining too much. Glymbo the goblin really doesn't like chatback.",
                     "You: Noted.",
                     "Farmer: All I have to my name is this lettuce in my pocket. You could have it if you like.",
                     "Farmer: My chances of escaping have already passed, take the lettuce and use it wisely.",
                     "You picked up the lettuce."])
        inventory["lettuce"]=True

def robber_dialouge():
    if inventory["gold"]:
        text_reader(["You cannot talk to the robber, because he ran away somewhere!",
                     "Wherever he ran, he isn't getting out of the dungeon, not without his gold he left...",
                     "You laugh to yourself cunningly."])
    elif inventory["key"]:
        text_reader(["Robber: Is that a key? Please, quick, use it to open my cell and set me free!!",
                     "You use the key to open his cell",
                     "Robber: Oh good golly! I'm finally free! I am giddy with glee!!",
                     "The robber was so excited about his freedom, he ran away leaving his gold behind",
                     "You took it, gold was added to your inventory!"])
        inventory["gold"]=True
    else:
        text_reader(["Robber: Psst, oi, you there! Can you help me out?",
                     "Robber: They locked me up for no reason!",
                     "You: Then what is that bag of gold?",
                     "Robber: Ok maybe I stole from them a little... but that doesn't justify this terrible treatment!",
                     "Robber: There must be a key around here somewhere that can free me. Please find it...",
                     "You: I will think about it."])

inventory={
    "gold":False,
    "lettuce":False,
    "key":False,}

def room1(): #glymbo
    text_reader(["You stand in the main room of the dungeon.",
                 "A goblin is guarding a large door."])
    while True:
        choice=present_options(["Go east","Go west","Go south",
                                "Talk to the goblin","Look around"])
        print()
        match choice:
            case 1:
                room2()
            case 2:
                room3()
            case 3:
                room4()
            case 4:
                glymbo_dialouge()
            case 5:
                text_reader(["The walls of the dungeon are very gray and ominous. They scare you.",
                             "It almost feels like they were designed that way...",
                             "Who would do such a terrible thing?!"])
    
def room2(): #goat
    text_reader(["You went east and found a room with a single goat standing in the centre.",
                 "The goat is munching on grass."])
    while True:
        choice=present_options(["Go west","Talk to the goat","Look around"])
        print()

        match choice:
            case 1:
                text_reader(["You went west, and found yourself back in the main room."])
                return
            case 2:
                goat_dialouge()
            case 3:
                text_reader(["You wonder to yourself how grass is growing inside the dungeon.",
                             "It really doesn't make much sense."])
    

def room3(): #farmer
    text_reader(["You went west and found a room where a farmer sits, shackled to the wall.",
                 "He does not look very pleased..."])
    while True:
        choice=present_options(["Go east","Talk to the farmer","Look around"])
        print()

        match choice:
            case 1:
                text_reader(["You went east, and found yourself back in the main room."])
                return
            case 2:
                farmer_dialouge()
            case 3:
                text_reader(["You look at the shackles keeping the farmer to the wall.",
                             "They are pretty intimidating, it seems like he can't be helped.",
                             "You feel bad, but glad you are not in his position."])

def room4(): #robber
    text_reader(["You went south and found a room with a robber behind bars.",
                 "He has a big bag of gold next to him."])
    while True:
        choice=present_options(["Go north","Talk to the robber","Look around"])
        print()

        match choice:
            case 1:
                text_reader(["You went north, and found yourself back in the main room."])
                return
            case 2:
                robber_dialouge()
            case 3:
                text_reader(["It seems like his cell can be opened using some sort of key...",
                             "It also doesn't seem like he knows that bag of gold is his key to get out of here.",
                             "You must get it from him at all costs!"])

def room5(): #freedom
    pass


print()
text_reader(["Once upon a time, you were minding your own business...",
             "And then you were suddenly kidnapped by a goblin!",
             "The next thing you know, you are trapped in a dungeon..."])
room1()
