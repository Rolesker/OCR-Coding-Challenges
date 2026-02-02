class ComplexNumber:
    def __init__(self,re,im):
        self.a=re
        self.b=im

    def Re(self):
        return self.a

    def Im(self):
        return self.b
    
    def output(self):
        if self.a==0:
            print(str(self.b)+"i")
        else:
            if self.b==0:
                print(self.a)
            elif self.b>0:
                print(str(self.a)+"+"+str(self.b)+"i")
            else:
                print(str(self.a)+str(self.b)+"i")
    
def add(x,y):
    return ComplexNumber(x.Re()+y.Re(),x.Im()+y.Im())

def subtract(x,y): # x-y
    return ComplexNumber(x.Re()-y.Re(),x.Im()-y.Re())

def negate(x):
    return ComplexNumber(x.Re()*-1,x.Im()*-1)

def multiply(x,y):
    return ComplexNumber((x.Re()*y.Re())-(x.Im()*y.Im()),(x.Re()*y.Im())+(x.Im()*y.Im()))

def divide(x,y): # x/y
    denominator=y.Re()**2+y.Im()**2
    return ComplexNumber(((x.Re()*y.Re())+(x.Im()*y.Im()))/denominator,((y.Re()*x.Im())-(x.Re()*y.Im()))/denominator)

def inversion(x):
    return divide(ComplexNumber(1,0),x)

z1=ComplexNumber(3,4)
z2=ComplexNumber(2,-2)
z1.output()
z2.output()
print()
add(z1,z2).output()
subtract(z1,z2).output()
negate(z1).output()
multiply(z1,z2).output()
divide(z1,z2).output()
inversion(z1).output()