import random
results=[]

def generate_things():
    operator=["+","-","*","/"][random.randint(0,3)]
    num1=-1
    num2=100000
    if operator=="+":
        num1=random.randint(0,99)
        num2=random.randint(0,99)
    elif operator=="-":
        num1=random.randint(0,99)
        if num1==99:
            num2=99
        else:
            while num2>num1:
                num2=random.randint(0,99)
    elif operator=="*":
        num1=random.randint(0,12)
        num2=random.randint(0,12)
    else:
        num2=random.randint(1,12)
        num1=num2*random.randint(1,12)
    return num1, operator, num2

def generate_question(num1,operator,num2):
    print("What is " +str(num1)+" "+operator+" " +str(num2)+"?")
    given=float(input("Enter answer "))
    if operator=="+":
        answer=num1+num2
    elif operator=="-":
        answer=num1-num2
    elif operator=="*":
        answer=num1*num2
    else:
        answer=num1/num2
    print()
    return int(round(answer,2)==round(given,2))
    
for i in range(10):
    a,b,c=generate_things()
    print("Question "+str(i+1))
    results.append(generate_question(a,b,c))
print("Your scores for each question:")
print(results)
print("You got "+str(sum(results))+"/10")
    
    
