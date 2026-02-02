while True:
    result=False
    operation=input("Enter operation: ")
    num1=bool(int(input("Enter first input: ")))
    if operation!="NOT":
        num2=bool(int(input("Enter second input: ")))
    else:
        result=not(num1)



    if operation=="OR":
        result=(num1 or num2)
    elif operation=="AND":
        result=(num2 and num2)
    elif operation=="NOR":
        result=(not(num1 and num2))
    elif operation=="NAND":
        result=(not(num1 and num2))
    elif operation=="XOR":
        result=(num1^num2)
    elif operation!="NOT":
        result=("Invalid operation")
    print("Result:",int(result))
    print()