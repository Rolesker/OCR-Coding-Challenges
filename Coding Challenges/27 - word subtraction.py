def subtract_asciis(s1,s2):
    ascii1=0
    ascii2=0
    for i in s1:
        ascii1+=ord(i)
    for i in s2:
        ascii2+=ord(i)
    return abs(ascii1-ascii2)

def remove_letters(s1,s2):
    banned_letters=set(s1)
    new_word=""
    for i in s2:
        if i not in banned_letters:
            new_word+=i
    return new_word

print(subtract_asciis("hello","howdy"))
print(remove_letters("hello","howdy"))