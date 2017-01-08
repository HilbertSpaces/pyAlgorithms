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
    def __multiply__(self,other):
        newnum=self.num*other.num
        newden=self.den*other.den
        return Fraction(newnum,newden)
    def __lt__(self,other):
        firstnum=self.num*other.den
        secondnum=other.num*self.den
        return(firstnum<secondnum)

myFrac=Fraction(3,5)
myFrac1=Fraction(5,4)+Fraction(3,4)
Frac2=Fraction(3,5)
Frac3=Fraction(7,10)
print(Frac2<Frac3)
