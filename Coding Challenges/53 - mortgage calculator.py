def apply_interest(initial, rate, time, salary, interval="Months"):
    if interval=="Months":
        months=time
    elif interval=="Weeks":
        months=time//4.5
    elif interval=="Days":
        months=time//30.5
    else:
        return
    monthly_pay=0
    for i in range(int(months)):
        initial*=(1+rate)
        monthly_pay+=initial
    print("Average monthly payment over this period: ",monthly_pay/months)
    print("Months needed to repay this at your salary: ",monthly_pay/(salary/12))

apply_interest(3000,0.05,100,42000,"Days")


