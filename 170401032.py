
def get_words():
    wordList=[]
    for i in range(1,10):
        with open("{}.txt".format(i),"r",encoding="utf-8") as f:
            contents=f.read()
            words=contents.split()
            for word in words:
                wordList.append(word)
    return wordList


def get_hist(wordList):
    wordHist={}
    for w in wordList:
        if w in wordHist.keys():
            wordHist[w]=wordHist[w]+1
        else:
            wordHist[w]=1
    return wordHist

list=get_words()
a=get_hist(list)
print(a)
print(list)

def sonrakiKelimelerCoklu(wordList,text):
    words=text.split()
    lenwords=len(words)
    lenWordList = len(wordList)
    nextword1=[]

    if lenwords>6:
        print("Hatalı giriş")

    else:
        for i in range(lenWordList-lenwords):
            for j in range(lenwords):
                if wordList[i]==words[j]:
                    i+=1
                    if(j==lenwords-1):
                        nextword1.append(wordList[i])
    return nextword1


x=sonrakiKelimelerCoklu(get_words(),"tartışılacak bir")
print(x)


b=get_hist(x)
print(b)

all_values=b.values()
max_value=max(all_values)


print(max_value)

keymax=max(b,key=b.get)
print(keymax)




























