def merger(n):
    sets=[]
    freqs={}
    big_fat_set=set()
    for i in range(n):
        k=int(input("How long do you want shopping list "+str(i+1)+" to be? "))
        temp=set()
        for j in range(k):
            item=input("Enter item "+str(j+1)+" :")
            temp.add(item)
            if item in freqs:
                freqs[item]+=1
            else:
                freqs[item]=1
        sets.append(temp)
        big_fat_set.update(temp)
        print("Shopping list",i+1,":",temp)
        print()
    for i in range(n):
        print("Unique items to shopping list",i+1)
        for j in sets[i]:
            if freqs[j]==1:
                print(j)
        print()
    print("Total shopping list: ",big_fat_set)
    sorted_by_values = dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))
    print()
    print("Top 3 most popular items:")
    count=0
    for i in sorted_by_values:
        print(i, sorted_by_values[i])
        count+=1
        if count==3:
            break
n=int(input("How many shopping lists do you wish to create? "))
print()
merger(n)