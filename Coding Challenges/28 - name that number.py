import random
def replace_with_digits(number):
    replacements={}
    for i in number:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm" and not replacements.get(i):
            rand=random.randint(0,9)
            while rand in replacements.values():
                rand=random.randint(0,9)
            replacements[i]=rand
    number=list(number)
    for i in range(len(number)):
        if number[i] in replacements:
            number[i]=replacements[number[i]]
    return "".join(str(i) for i in number)

print(replace_with_digits("0141-CAT-DOOR"))

#actual horrible extension i don't want to do that