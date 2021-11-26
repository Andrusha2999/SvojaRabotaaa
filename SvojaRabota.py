palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("srednjaja - 1,\nMinimalnaja Zarplata - 2,\nMaksimalka zarplata - 3,\nfind po imeni - 4,\nSortirovka - 5, \nADD 4eloveka - 6\n3 samix bogatix и 3 samix bednix - 7, \n")
    if valik=="1":
        kesk_palk=round(keskmine(palk),2)
        print("Keskmine palk on ",kesk_palk)
        print()
        print()
    elif valik=="2":
        m_palgad,nimi=minimum(palk,inimesed)
        for n in nimi:
            print(m_palgad[0], " tebe dadut ",n)
            print()
            print()
    elif valik=="3":
        max_palk,kto=maksimum(palk,inimesed)
        print("maks zarplata ", max_palk, " tebe dadut ",kto)
        print()
        print()
    elif valik=="4":
        ots_nimi,ots_palk=nimi(palk,inimesed)
        for i in range(len(ots_nimi)):
            print(ots_nimi[i]," tebe dadut", ots_palk[i])
            print()
            print()
    elif valik=="5":
        p,i=sorteerimine(palk,inimesed)
        for i in range(len(inimesed)):
            print(inimesed[i]," tebe dadut ", palk[i])
            print()
            print()
    elif valik=="6":
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Пустой лист")
            print()
            print()
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," tebe dadut ", palk[i])
                print()
                print()

    elif valik == '7':
        bog, bog_p, bed, bed_p = top3(palk,inimesed,n)
        print("3 самых богатых")
        for i in range(3):
            print(b1[i],'получает',str(b2[i])+'€')
        print()
        print("3 самых бедных")
        for i in range(3):
            print(b4[i],'получает',str(b3[i])+'€')
def topbogat(palk,inimesed):
    top,inimes=sorteerimine(palk,inimesed)
    k= int(input("Выберите значение топ: " ))
    palk.reverse()
    inimesed.reverse()
    for i in range(0,k,1):
        print(palk[i])
        print(inimesed[i])
    return palk, inimesed
    print()
    print()

def adding(palk,inimesed):
    add=input("kogo dobovit? ")
    inimesed.append(add)
    add_palk=int(input("kakaya zarplata? " ))
    palk.append(add_palk)
    return palk,inimesed
    print()
    print()
def delete(palk, inimesed):
    x=input("name or number ")
    if x=="number":
        i=int(input("Chose number "))
        palk.pop(i-1)
        inimesed.pop(i-1)
        print()
        print()
    elif x=="name":
        i=0
        keda=input("Write the name => ")
        n=len(inimesed)
        while i<n:
            if keda==inimesed[i]:
                inimesed.pop(i)
                palk.pop(i)
                n=len(inimesed)
                print()
                print()
            else:
                i+=1
            print()
            print()
    return palk, inimesed
    print()
    print()
def kustutamine():
    keskmin = keskmine(palk)
    print(keskmin)
    for i in palk:
        if i < kesk:
            index = palk.index(i)
            palk.pop(index)
            inimesed.pop(index)
            print()
            print()
def sorteerimine(palk,inimesed):
    abi_p=0
    abi_i=""
    n=len(inimesed)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if palk[i]>palk[j]:
                abi_p=palk[i]
                palk[i]=palk[j]
                palk[j]=abi_p
                abi_i=inimesed[i]
                inimesed[i]=inimesed[j]
                inimesed[j]=abi_i
    return palk,inimesed
    print()
    print()
def nimi(palk,inimesed):
    ots_nimi=[]
    ots_palk=[]
    palk_keda=0
    keda=input("Sisesta nimi... ")
    n=len(inimesed)
    for j in range(n):
        if inimesed[j]==keda:
            palk_keda=palk[j]
            ots_nimi.append(inimesed[j])
            ots_palk.append(palk_keda)
            print()
            print()
        else:pass
    return ots_nimi,ots_palk
    print()
    print()
def maksimum(palk,inimesed):
    m_palgad=[]
    nimed=[]
    max_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p>max_palk:
            max_palk=p
            i=palk.index(max_palk)
            kellel=inimesed[i]
            print()
            print()
    n=palk.count(max_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesed.copy()
    for i in range(n):
        j=palk_copy.index(max_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed
    print()
    print()
def minimum(palk,inimesed):
    m_palgad=[]
    nimed=[]
    min_palk=palk[0]
    kellel=inimesed[0]
    for p in palk:
        if p<min_palk:
            min_palk=p
            i=palk.index(min_palk)
            kellel=inimesed[i]
    n=palk.count(min_palk)
    palk_copy=palk.copy()
    inimesed_copy=inimesedcappendRCy()
    for i in range(n):
        j=palk_copy.index(min_palk)
        m_palgad.append(palk_copy.pop(j))
        nimed.append(inimesed_copy.pop(j))
    return m_palgad, nimed
    print()
    print()
def keskmine(palk):
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    k=summa/n
    return k
    print()
    print()
while True:
    palgad(palk,inimesed)