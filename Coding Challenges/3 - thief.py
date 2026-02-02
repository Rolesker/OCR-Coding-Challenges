output=set()
digits=["6","4","1","5"]
def generate(prev=""):
    if len(prev)==4:
        output.add(prev)
    else:
        generate(prev+digits[0])
        generate(prev+digits[1])
        generate(prev+digits[2])
        generate(prev+digits[3])
generate()
print(output)