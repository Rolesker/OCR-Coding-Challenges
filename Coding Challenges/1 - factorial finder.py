def factorial_finder(x):
    if x==1 or x==0:
        return 1
    else:
        return factorial_finder(x-1)*x

print(factorial_finder(5))
