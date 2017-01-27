def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n
class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,other):
        newnum=self.num*other.den+self.den*other.num
        newden=self.den*other.den
        common=gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __eq__(self,other):
        firstnum=self.num*other.den
        secondnum=other.num*self.den
        return firstnum==secondnum
    def __mul__(self,other):
        newnum=self.num*other.num
        newden=self.den*other.den
        common=gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    __rmul__=__mul__
    def __lt__(self,other):
        firstnum=self.num*other.den
        secondnum=other.num*self.den
        return(firstnum<secondnum)

myFrac1=Fraction(10,63)
myFrac2=Fraction(8,63)
myFrac3=Fraction(5,42)
print(myFrac1+myFrac2+myFrac3)
