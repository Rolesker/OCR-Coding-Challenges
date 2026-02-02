import math

phi=(1+math.sqrt(5))/2 #golden ratio
i=1
while math.floor(i*math.log(phi, 10)+math.log(1/math.sqrt(5),10))+1<1000:
    i+=1
print(i)
    
