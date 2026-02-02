def validate_card(n):
    checksum=0
    n,check_digit=n[0:len(n)-1],n[-1]
    n=n[::-1]
    for i in range(len(n)):
        if i%2==0:
            temp=int(n[i])*2
            if temp>=10:
                temp-=9
        else:
            temp=int(n[i])
        checksum+=temp
    return True if int(check_digit)==(10-(checksum%10))%10 else False

print(validate_card("17893729974"))
print(validate_card("17893729973"))
