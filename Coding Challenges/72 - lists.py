import random

def generate_list(l,r):
    out=[]
    for i in range(l,r+1):
        out.append(i)
    return out

def insert(arr,data,pos):
    return arr[:pos]+[data]+arr[pos:]

def create_sublists(arr,lists,n): #n is how many elements to use
    out=[]
    for i in range(lists):
        out.append([])
    random.shuffle(arr)
    for i in range(n):
        out[random.randint(0,lists-1)].append(arr[i])
    return out

def sort_based_on_length(arrs):
    combined=list(zip([len(i) for i in arrs],arrs))
    combined=sorted(combined)
    return [combined[i][1] for i in range(len(arrs))]

test=generate_list(3,20)
print(test)
test2=insert(test,11,2)
print(test2)
test3=create_sublists(test2,3,10)
print(test3)
print(sort_based_on_length(test3))
