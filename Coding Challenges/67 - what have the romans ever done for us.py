def get_components(n):
    t=len(str(n))
    out=[]
    for i in range(t):
        out.append(n%(10**(i+1))//(10**i))
    return out

def get_digit(dig,low,mid,large):
    out=""
    if dig==0:
        return ""
    elif dig<4:
        out+=low*dig
    elif dig==4:
        out=low+mid
    elif dig==5:
        out=mid
    elif dig<9:
        out=mid+(low*(dig-5))
    else:
        out=low+large
    return out

def int_to_roman(num):
    components=get_components(num)
    ans=""
    for i in range(len(components))[::-1]:
        if i==3:
            ans+=get_digit(components[i],"M","M","M")
        elif i==2:
            ans+=get_digit(components[i],"C","D","M")
        elif i==1:
            ans+=get_digit(components[i],"X","L","C")
        elif i==0:
            ans+=get_digit(components[i],"I","V","X")
    return ans

print(int_to_roman(67))


