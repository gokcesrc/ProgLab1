#!/usr/bin/env python
# coding: utf-8

# In[61]:


#Lesson-1
def min_heapify(array,i): #İki parametre alıyor. Düzenlenecek dizi ve bulundugumuz mevcut düğüm
    left=2*i+1 #sol düğüm
    right=2*i+2 #sağ düğüm
    length=len(array)-1 #index
    smallest=i
    if left <= length and array[i]>array[left]: #eğer sol düğüm varsa ve mevcut düğümden küçükse;
        smallest=left #küçük sol düğümdür.
    if right <= length and array[smallest]>array[right]:#eğer sağ düğüm varsa ve mevcut düğümden küçükse;
        smallest=right #küçük sağ düğümdür.
    if smallest !=i:#eğer mevcut değer başta olan değer değilse;
        array[i],array[smallest]=array[smallest],array[i] #swap işlemi
        min_heapify(array,smallest)#recursive çağırdık.

def build_min_heapify(array): #Bir parametre alıyor.Düzenlenecek olan dizi.
    for i in reversed(range(len(array)//2)): #// = Tam sayı bölmesi.
        #Tersten gidiyoruz.
        min_heapify(array,i)#Sıralattık.
        

#Lesson-2


# In[62]:


def heapsort(array):
    array =array.copy()#Dizi değişince eskisi elimde kalsın diye kopyaladım.
    build_min_heapify(array)#heap oluşturdum
    sorted_array=[]#Aldığım sayıları atacağım yapı
    #Dizi boş ise append fonk. kullanamıyoruz en azından bir elemanı olmalı.
    for _ in range(len(array)):#arrayin boyutu kadar diziyi dolaşacak.. _ önemsiz bir değişken.
        array[0],array[-1]=array[-1],array[0]#arrayin başı ile sonundaki elemanı yer değiştirdik.
        sorted_array.append(array.pop())#En küçük elemanı pop ile çıkardık boş olan diziye ekledik.
        min_heapify(array,0)
    return sorted_array#Sıralanmış diziyi döndürdük.


# In[63]:


def insert(array,item):
    array.append(item)
    i = len(array)-1
    if i<=0:
        return    
    parent = (i-1)//2
    while parent>=0 and array[parent] > array[i]:
        array[parent],array[i] = array[i],array[parent]            
        i = parent
        parent = (i-1)//2
    
def remove(array):
    i = len(array)
    if i<=0:
        print("Heap boş")
        return
    array.pop()


# In[67]:


array = [7,14,6,5,11,9,8,3,4]
build_min_heapify(array)
print(array)
insert(array,2)
insert(array,1)
remove(array)
remove(array)
print(array )
print(heapsort(array))
print(array)


# In[ ]:





# In[ ]:




