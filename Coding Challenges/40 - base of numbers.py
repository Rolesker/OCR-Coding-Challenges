def convert(n,base):
    if base>20 or base<2:
        return "Base is too large or small"
    output=""
    conversion=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J"]
    while n>0:
        output=conversion[n%base]+output
        n=n//base
    return output

print(convert(15,16))
print(convert(15,2))
print(convert(25,20))