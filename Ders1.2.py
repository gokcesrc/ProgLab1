#Ust kısmın cıft olup olmadıgı durumunu kontrol eder.
def power(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    else:
        if b%2==0:
            return power(a*a,b//2)
        else:
            return power(a*a,b//2)*a

print(power(5,3))
