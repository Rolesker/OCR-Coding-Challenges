import re

def directed_sort(arr,order):
    arr=sorted(arr)
    if order=="a":
        return arr
    else:
        return arr[::-1]


data=[]
for i in range(10):
    data.append(int(input("Enter a piece of data: ")))
choice=input("Do you want to sort this data in ascending or descending order? (a for ascending, d for descending) ")
print(directed_sort(data,choice))

#extenstion 2

def sentence_sort(s):
    punctuation={}
    for i in range(len(s)):
        if s[i] in "!,.?()-:; ":
            punctuation[i]=s[i]
    words=re.split("[!,.?()-:; ]",s)
    sentence=""
    for i in range(len(words)):
        sentence+="".join(j for j in sorted(list(words[i])))
    for i in range(len(s)):
        if i in punctuation:
            sentence=sentence[0:i]+punctuation[i]+sentence[i:]
    print(sentence)

sentence_sort("Hi! I can enter a sentence, sort it; but punctuation like this ? will be fine, even when in the mid!!dle o.f wor-ds")
