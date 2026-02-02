def reverser(s):
    print(s,"backwards is",s[::-1])
    if s==s[::-1]:
        print(s,"is a palindrome!")

reverser("hello")
print()
reverser("racecar")