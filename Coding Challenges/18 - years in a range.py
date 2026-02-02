def find_repeats(start,end):
    count=0
    for i in range(start,end+1):
        if len(str(i))==len(list(set(str(i)))):
            print(i," contains no repeats")
        else:
            count+=1
            print(i," contains repeats")
    return count


year1=int(input("Enter a year: "))
year2=int(input("Enter a second year: "))
print(find_repeats(min(year1,year2),max(year1,year2)))
