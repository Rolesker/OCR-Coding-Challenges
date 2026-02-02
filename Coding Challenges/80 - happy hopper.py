def happy_hopper(numbers):
    diff=[]
    for i in range(len(numbers)-1):
        diff.append(abs(numbers[i]-numbers[i+1]))
    return set(diff).symmetric_difference(set([i+1 for i in range(len(diff))]))==set()

print(happy_hopper([1,4,2,3]))
print(happy_hopper([1,2,3,4]))
    
