sequence=[0,1]

def fibbonaci_to(n):
    total=0
    for i in range(n):
        if i>=2:
            sequence.append(sequence[i-1]+sequence[i-2])
        total+=sequence[i]
    print(sequence)
    print(total)

def backwards():
    b=[]
    while sequence:
        b.append(sequence.pop())
    print(b)

fibbonaci_to(20)
backwards()