text_speak_dictionary={
    "lol":"laugh out loud",
    "hru":"how are you",
    "wbu":"what about you",
    "brb":"be right back",
    "fr":"for real",
    "omg":"oh my god",
    "lmao":"laughing my ass off",
    "rofl":"rolling on the floor laughing",
    "tldr":"too long didn't read",
    "afk":"away from keyboard",
    "btw":"by the way",
    "ftw":"for the win",
    "fyi":"for your information",
    "atm":"at the moment",
    "rn":"right now",
    "gtg":"got to go",
    "ily":"I love you",
    "irl":"in real life",
    "tbh":"to be honest",
    "icl":"I can't lie",
    "lmk":"let me know",
    "ngl":"not gonna lie",
    "omw":"on my way",
    "wyd":"what are you doing",
    "smh":"shaking my head"
}

def translate(sentence):
    reformed=""
    for i in sentence.split(" "):
        if text_speak_dictionary.get(i):
            reformed+=text_speak_dictionary[i]+" "
        else:
            reformed+=i+" "
    return reformed

txt=input("Enter a sentence to convert from text-speak to proper english: ")
print(translate(txt))