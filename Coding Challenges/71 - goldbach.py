def get_all_primes_leading_up_to(n):
    ans=[]
    is_prime=[True]*(n-1)
    for i in range(2,n-1):
        if is_prime[i]:
            ans.append(i)
        j=i
        while j<n-1:
            is_prime[j]=False
            j+=i
    return ans

def two_sum(target,nums):
    l=0
    r=len(nums)-1
    while l<r:
        if nums[l]+nums[r]>target:
            r-=1
        elif nums[l]+nums[r]<target:
            l+=1
        else:
            return (nums[l],nums[r])

def goldbach(n):
    if n<=2 or n%2==1:
        print("invalid number")
        return
    (num1,num2)=two_sum(n,get_all_primes_leading_up_to(n))
    print(str(n)+" = "+str(num1)+" + "+str(num2))

goldbach(40)
