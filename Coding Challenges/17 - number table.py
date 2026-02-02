def number_table(operation,n):
    n+=1
    header=operation+" |"
    for i in range(n):
        header+=" "+str(i)
    print(header)
    print("-"*(n+2)*2)
    for i in range(n):
        line=""
        for j in range(n+2):
            if j==0:
                line+=str(i)+" "
            elif j==1:
                line+="| "
            else:
                if operation=="+":
                    line+=str(i+j-2)
                elif operation=="-":
                    line+=str(i-j+2)
                elif operation=="*":
                    line+=str((i-2)*j)
                elif j!=0:
                    line+=str((i-2)/j)
                else:
                    line+="N/A"
                line+=" "
        print(line)

number_table("+",4)
