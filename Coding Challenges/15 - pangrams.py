def check_pangram(s):
    for i in "qwertyuiopasdfghjklzxcvbnm":
        if i not in s: return False
    return True




while True:
    s=input("Enter a string: ")
    if check_pangram(s):
        print("This is a pangram")
    else:
        print("This is not a pangram")
    print()
