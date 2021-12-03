def adding(palk,inimesed):
    """"
    Programm lisab nimekirjad nimi ja palk
    esimene arv nimi: str
    teine arv - palk: int 
    rtype var: str
    """
    add=input("vvedite imja: ")
    inimesed.append(add)
    add_zp=int(input("vvedite zp: "))
    palk.append(add_zp)
    return palk,inimesed
def udalenie():
    keskmin = udalenie(palk)
    print(keskmin)
    for i in palk:
        if i < kesk:
            index = palk.index(i)
            palk.pop(index)
            inimesed.pop(index)
def maksimalka(palk,inimesed):
    """
    Programm kontrollib nimekirjad ja kuvab inimese maksimaalne palk
     var type: int
    """
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
def minimalka(palk,inimesed):
    """Programm kontrollib nimekirjad ja kuvab väikseima palgaga inimese.
    sisestage var: int
    """
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
def srednija(palk):
    """
  Programm kontrollib nimekirjad ja kuvab keskmise palga.
        sisestage var: int
    """
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    k=summa/n
    return k