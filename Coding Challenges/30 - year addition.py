import random
def add_digits(num):
    output=0
    for i in num:
        output+=int(i)
    return output



year=-1
while year<=-1 or year>=10000:
    year=int(input("Enter a year: "))
print(add_digits(str(year)))

year_to_guess=random.randint(0,9999)
print("Try to guess a year where the sum of the digits are",add_digits(str(year_to_guess)))
attempts=0
while int(input("Enter guess: "))!=year_to_guess and attempts!=2:
    attempts+=1
if attempts!=2:
    print("Congratulations you guessed",year_to_guess,"correctly!")
else:
    print("You failed, answer was",year_to_guess)
