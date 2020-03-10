list_1=[4,-3,5,-2,-1,2,6,-2]
n=len(list_1)
maxSum=0
for i in range(n):
    for j in range(i,n): #baslangıc konumu i,gittiği yer de n.
        t=0
        for k in range(i,j):
            t=t+list_1[k]
        if(t>maxSum):
            maxSum=t
print(maxSum)