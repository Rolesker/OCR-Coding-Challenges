binaries=[]
def generate_binaries(sequence,n):
    if len(sequence)==n:
        binaries.append(sequence)
        return
    generate_binaries(sequence+"0",n)
    generate_binaries(sequence+"1",n)
columns=int(input("Enter the number of input variables: "))
if columns>=11:
    print("That is way too many inputs, simply your expression pls")
else:
    generate_binaries("",columns)
    print("ABCDEFGHIJ"[0:columns])
    for i in range(2**columns):
        print(binaries[i])