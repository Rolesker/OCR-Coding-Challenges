def check_happy(num):
    original=num
    seen=[num]
    while num!=1:
        num=sum([int(i)**2 for i in str(num)])
        if num in seen:
            return str(original)+" is not happy"
        seen.append(num)
    return str(original)+" is happy"

for i in range(100):
    print(check_happy(i))
