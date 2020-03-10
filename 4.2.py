#4.1 de girdiğin v kadar tekrar eden bir sayı olup olmadığını kontrol eden fonksiyon.
def lookup(d,v):
    for k in d:
        if d[k]==v:
            return k
    return -1 #fonk kullanılcaksa koy
