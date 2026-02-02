"""
this problem is pretty vague and poorly described so this is how i interpreted it
there are x members of a travel club, each owning m money
there is a list of expenses they all must contribute towards (collectively at least 1% towards this payment, the club will handle the rest)
return the amount of money will have to be exchanged between the members until they can all make a payment of the same amount
"""

def find_minmax(arr):
    minimum=float("inf")
    maximum=0
    min_i=0
    max_i=0
    for i in range(len(arr)):
        if arr[i]>maximum:
            maximum=arr[i]
            max_i=i
        if arr[i]<minimum:
            minimum=arr[i]
            min_i=i
    return min_i,max_i

def pay_fees(members, expenses):
    total=sum(expenses)
    exchanged=0
    if sum(members)<total*0.01:
        return -1

    while min(members)<(total*0.01):
        #print(members)
        min_i,max_i=find_minmax(members)
        needed=(total*0.01)-members[min_i]
        exchanged+=needed
        members[min_i]+=needed
        members[max_i]-=needed
    return exchanged

print(pay_fees([300,300,300],[400,600]))
print(pay_fees([1,1,1,1,800],[400,600]))
