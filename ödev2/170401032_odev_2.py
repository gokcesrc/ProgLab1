import csv
import sys
import math


file=open("input_hw_2[523].csv","r+",encoding="utf-8")
list=file.read()
#print(list)

x=list.split(";")
#print(x)
dates=[]
for i in range(3,len(x),3):
    dates.append(x[i].split("-"))

quitDates=[]
for i in range(len(dates)):
    quitDates.append(dates[i][1])
    
#print(quitDates)

def getHist(quitDates):
    ayHist={}
    for m in quitDates:
        if m in ayHist.keys():
            ayHist[m]=ayHist[m]+1
        else:
            ayHist[m]=1
    return ayHist

a=getHist(quitDates)
#print(a)
all_values=a.values()
#print(all_values)
 
def ortalama(a):
    toplam=sum(a.values())
    ay=len(a)
    ort=toplam/ay
    return ort

y=ortalama(a)
print("Ortalama: ",y)


monthlist=sorted(all_values)
#print(monthlist)

def getMedian(monthlist):
    if len(monthlist)%2==0:
        middle=len(monthlist)/2
        median=monthlist[middle]
    else:
        middle=math.ceil(len(monthlist)/2)
        x=middle
        median=monthlist[x]
    
    return median

medyan=getMedian(monthlist)
print("Medyan: ",medyan)

with open("170401032_hw_output.txt","w",encoding="(utf-8") as dosya:
    dosya.write("Medyan"+str(medyan)+"\n")
    dosya.write("Ortalama"+str(y))





    
    

    