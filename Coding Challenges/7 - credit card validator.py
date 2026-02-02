card=""
while len(card)!=16:
    card=input("Enter a 16 digit credit card number")
parsed=[int(card[i])*(((i+1)%2)+1) for i in range(len(card))]
print(parsed)
for i in range(len(parsed)):
    if parsed[i]>9:
        parsed[i]=sum([int(j) for j in str(parsed[i])])
print(parsed)
if sum(parsed)%10==0:
    print("card valid")
else:
    print("card invalid")
                      
                       
