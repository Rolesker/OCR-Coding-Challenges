def check_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def fizz_buzz(a,b,do_primes):
    for i in range(1,31):
        output=""
        if i%a==0:
            output+="Fizz"
        if i%b==0:
            output+="Buzz"

        if do_primes:
            if check_prime(i):
                output="OOPS!"

        if output=="":
            output=i
        print(output)
    print()

fizz_buzz(3,5,False)
fizz_buzz(3,5,True)
fizz_buzz(2,3,False)
