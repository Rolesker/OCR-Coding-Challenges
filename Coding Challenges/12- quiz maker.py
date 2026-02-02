import json
import random

q_file=open("12-quiz_questions.txt","rb")
question_bank=json.load(q_file)
max_questions=len(question_bank.keys())
q_file.close()

quiz_length=int(input("how many questions do you want in the quiz? "))
quiz_length=min(max_questions,quiz_length)
questions=[-1]*quiz_length
for i in range(quiz_length):
    r=-1
    while r in questions:
        r=random.randint(1,max_questions)
    questions[i]=str(r)

score=0
for i in questions:
    print(question_bank[i][0])
    answer=input("enter answer here ")
    if answer==question_bank[i][1]:
        score+=1
        print("correct!")
    else:
        print("incorrect")
    print()

print("final score: ",score,"/",quiz_length)
    
    
