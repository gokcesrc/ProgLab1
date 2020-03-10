#Insertion sort adı üstünde araya girme sıralı kısım yavaş yavaş büyüyecek.
#büyükten küçüğe
def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1 #karşılaştırdıkların her biri bir adım sağa kayıyor.
        arr[j+1]=key
