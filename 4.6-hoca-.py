
def my_h(list_1):
    my_d={}
    for item in list_1:
        if item not in my_d:
            my_d[item]=1
        else:
            my_d[item]=item+1
    return my_d
print(my_h([2,3,4,6,2,5,6,6,6,6,6,2]))

def lookup(d,v):
    print(d,v)
    for key in d:
        if d[key]==v:
            return key
        else:
            return -1


