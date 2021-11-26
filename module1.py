def adding(palk,inimesed):
    add=input("vvedite imja: ")
    inimesed.append(add)
    add_zp=int(input("vvedite zp: "))
    palk.append(add_zp)
    return palk,inimesed
def adding(palk,inimesed):
    add=input("Imja 4eloveka:  ")
    inimesed.append(add)
    add_palk=int(input("ZP 4eloveka:  " ))
    palk.append(add_palk)
    return palk,inimesed
    print()
    print()
def delete(palk, inimesed):
    x=input("Imja Polzovatelja napisano bukvami - 1 ILI 2iframi - 2? ")
    if x=="2":
        i=int(input("VVedi nomer: "))
        palk.pop(i-1)
        inimesed.pop(i-1)
    elif x=="1":
        i=0
        keda=input("VVedi Imja: ")
        n=len(inimesed)
        while i<n:
            if keda==inimesed[i]:
                inimesed.pop(i)
                palk.pop(i)
                n=len(inimesed)
            else:
                i+=1
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
    inimesed_copy=inimesed.copy()
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
