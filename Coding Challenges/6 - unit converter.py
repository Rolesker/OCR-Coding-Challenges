kind=""
while kind not in ["temperature","length"]:
    kind=input("enter the type of unit ")
data=float(input("enter the value of the unit "))
if kind=="temperature":
    selected=""
    while selected not in ["celsius","fahrenheit","kelvin"]:
        selected=input("choose the unit of your data out of: celsius, fahrenheit and kelvin ")
    output={"celsius":0,
            "kelvin":0,
            "fahrenheit":0}
    output[selected]=data
    if selected=="kelvin":
        output["celsius"]=data-273.15
        output["fahrenheit"]=(output["celsius"]*(9/5))+32
    elif selected=="celsius":
        output["kelvin"]=data+273.15
        output["fahrenheit"]=(output["celsius"]*(9/5))+32
    else:
        output["celsius"]=(5/9)*(data-32)
        output["kelvin"]=output["celsius"]+273.15
    print(output)
elif kind=="length":
    data=abs(data)
    options={
        "picometers":10**12,
        "nanometers":10**9,
        "micrometers":10**6,
        "millimeters":10**3,
        "centimeters":10**2,
        "meters":1,
        "kilometers":10**-3,
        "megameters":10**-6,
        "gigameters":10**-9,
        "terameters":10**-12}
    selected=""
    while selected not in options.keys():
        selected=input("choose the unit of your data out of: "+str([i for i in options.keys()])+" ")
    divisor=options[selected]
    for i in options.keys():
        options[i]/=divisor
        options[i]*=data
    print(options)
                       
