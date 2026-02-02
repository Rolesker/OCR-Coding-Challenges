def seperate(arr):
    arr=sorted(arr)
    for i in range(1,len(arr)):
        l=i
        while l>0 and arr[l]%2!=arr[l-1]%2:
            arr[l],arr[l-1]=arr[l-1],arr[l]
            l-=1
    return arr

arr=[]
add=0
while add!=-1:
    add=int(input("Enter a number to add to the array (-1 to stop): "))
    if add!=-1:
        arr.append(add)

print(seperate(arr))