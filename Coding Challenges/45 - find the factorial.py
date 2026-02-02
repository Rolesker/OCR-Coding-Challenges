# note: this is the same as the very first challenge

def factorial_by_recursion(n):
    if n==1 or n==0:
        return 1
    return factorial_by_recursion(n-1)*n

def factorial_by_iteration(n):
    answer=1
    while n>=2:
        answer*=n
        n-=1
    return answer

print(factorial_by_iteration(5))
print(factorial_by_recursion(5))