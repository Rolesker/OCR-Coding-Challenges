def check_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    return False

def day_of_week(d, m, y):
    month_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y -= 1
    year_code = (y % 100) + (y % 100) // 4
    year_code = (year_code + (y // 100) // 4 + 5 * (y // 100)) % 7
    return (d + month_code[m - 1] + year_code) % 7

def enter_date():
    day=int(input("Enter day digit: "))
    if day<=0 or day>=32:
        return
    month=int(input("Enter month digit: "))
    if month<=0 or month>=13:
        return
    year=int(input("Enter year digit: "))
    if year<=999 or year>=10000:
        return
    if month in [4,6,9,11] and day==31:
        return
    elif month==2:
        if check_leap_year(year)==True:
            if day>=30:
                return
        elif day>=29:
            return
    return ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"][day_of_week(day,month,year)]

got=enter_date()
if got!=None:
    print("The date is valid and the day is a",got)
else:
    print("Invalid date")