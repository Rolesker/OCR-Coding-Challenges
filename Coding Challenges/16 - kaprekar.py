def check_kaprekar(num):
    digits=len(str(num))
    squarestr=str(num**2)
    righthalf=""
    for i in range(digits):
        righthalf=squarestr[len(squarestr)-i-1]+righthalf
    return int(squarestr.rstrip(righthalf))+int(righthalf)==num
    
print(check_kaprekar(9))
print(check_kaprekar(297))
print(check_kaprekar(55))
print(check_kaprekar(100))
