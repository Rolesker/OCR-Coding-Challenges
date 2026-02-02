import random

envelope=[1]

def process():
    selection=envelope[random.randint(0,len(envelope)-1)]
    envelope.remove(selection)
    print("The foreman started with a size of A"+str(selection))
    while selection!=5:
        selection+=1
        envelope.append(selection)
    print("The contents of the envelope are now:", envelope)
    print()

simulations=16
for i in range(simulations):
    process()
    
