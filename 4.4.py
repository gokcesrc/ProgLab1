from sympy import FiniteSet
s=FiniteSet(1,1.5,Fraction(1,5))
for member in s:
    print(member)
t=FiniteSet(Fraction(1,5),1.5,1,1)
if s==t:
    print("True")
s.intersect(t)
s.uninon(t)

p=s**2
p1=s**3
