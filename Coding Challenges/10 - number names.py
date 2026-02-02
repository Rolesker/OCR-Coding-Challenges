import math

def onedig(d):
    return ["","one","two","three","four","five","six","seven","eight","nine"][d]

def twodig(d):
    return ["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"][d]

def teendig(d):
    return ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"][d]

def order_of_ten(d):
    return ["","thousand","million","billion"][d]

def threedigittoword(bit):
    numstr=""
    for i in bit:
        numstr+=str(i)
    num=int(numstr)
    output=""
    if num==0:
        return ""
    if num>100:
        output+=onedig(int(numstr[0]))+" hundred"
    numstr=numstr[1]+numstr[2]
    num=int(numstr)
    if num!=0:
        output+=" and "
    if num>10:
        if num>19:
            output+=twodig(int(numstr[0]))
        else:
            return output+teendig(int(numstr[1]))
    return output+" "+onedig(int(numstr[1]))
        
        
output=""
number=float(input("Enter a number "))
strflip=str(math.trunc(number))
times=len(strflip)//3
for i in range(times):
    if i==times:
        bit=strflip[i*3:]
    else:
        bit=strflip[i*3:i*3+3]
    if bit!=[0,0,0]:
        output+=(threedigittoword(bit)+" "+order_of_ten(times-i-1))+", "
print(output)
