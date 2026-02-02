import math
def triangulate(s1,s2,s3):
    if s1<=0 or s2<=0 or s3<=0:
        return "Invalid"
    sides=set([s1,s2,s3])
    if len(sides)==1:
        return "Equilateral"
    if len(sides)==2:
        return "Isosceles"
    else:
        return "Scalene"

def cosine_rule_for_side(b,c,A): #this is the only one the extension actually needs
    return math.sqrt((b**2)+(c**2)-(2*b*c*math.cos(A)))

def sine_rule_for_side(A,b,B):
    return (math.sin(A)*b/math.sin(B))

def cosine_rule_for_angle(a,b,c):
    return math.acos(((b**2)+(c**2)-(a**2))/(2*b*c))

def sine_rule_for_angle(a,b,B):
    return math.asin(a*math.sin(B)/b)


print(triangulate(6,6,6))
