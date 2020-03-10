#Keyfi bir seri yazalim ardisik toplamlari en büyük degeri veren alt diziyi bulsun.

liste_1=[4,-3,5,-2,-1,2,6,-2]
max=0
for i in range(8):   #0 dan baslayıp devam ettigini unutma.
    for j in range(i,8):
        #print(i,j) kodu kontrol etmene yarar,alt dizileri bastırır.
        t=0
        for k in range(i,j):
            t=t+liste_1[k]
        if max<t:
            max=t
            i_1,i_2=i,j
print(max,i_1,i_2)