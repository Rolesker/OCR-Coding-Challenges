output=4
for i in range(1,100000):
    if i%2==1:
        output-=4/((2*i)+1)
    else:
        output+=4/((2*i)+1)
    print(output)