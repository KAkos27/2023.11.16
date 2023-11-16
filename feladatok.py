def elso(a):
    osszeg:int = 0
    for i in range(0, len(a), 1):
        if a[i] == " ":
            osszeg+=1

    return osszeg

def masodik(a):
    szoveg:str=""
    for i in range(0, len(a), 1):
        if a[i] != " ":
            szoveg+=a[i]

    return szoveg

def harmadik(a):
    a = a.lower()
    szoveg:str=""

    for i in range(0, len(a), 1):
        if a[i] == "á":
            szoveg += "a"
        elif a[i] == "é": 
            szoveg += "e"
        elif a[i] == "í": 
            szoveg += "i"
        elif a[i] == "ú" or a[i] == "ű" or a[i] == "ü": 
            szoveg += "u"
        elif a[i] == "ó" or a[i] == "ő" or a[i] == "ö": 
            szoveg += "o"
        else:
            szoveg += a[i]
        
    hossz:int = len(szoveg)
    ujszoveg:str = ""

    for i in range(0, hossz, 1):
        ujszoveg+=szoveg[hossz-1-i]
        
    return ujszoveg

