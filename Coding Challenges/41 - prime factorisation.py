def factorise(n):
    if n==1:
        return []
    for i in range(2,n+1):
        if n%i==0:
            return [i]+factorise(n//i)
        
print(factorise(50))