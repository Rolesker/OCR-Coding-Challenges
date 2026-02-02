def check_happy(n):
    seen=[n]
    while n!=1:
        temp=[i for i in str(n)]
        n=0
        for i in temp:
            n+=int(i)**2
        if n in seen:
            return False
        seen.append(n)
    return True

for i in range(1,100):
    print(check_happy(i))