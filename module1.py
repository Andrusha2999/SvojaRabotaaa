def adding(palk,inimesed):
    add=input("vvedite imja: ")
    inimesed.append(add)
    add_zp=int(input("vvedite zp: "))
    palk.append(add_zp)
    return palk,inimesed
    #добовляет людей и их зарплаты
def udalenie():
    keskmin = udalenie(palk)
    print(keskmin)
    for i in palk:
        if i < kesk:
            index = palk.index(i)
            palk.pop(index)
            inimesed.pop(index)
            #удаляет людей и зп (ну как минимум должен был) 
def maksimalka(palk,inimesed):
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
#показывает максимальную зп
def minimalka(palk,inimesed):
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
#показывает минимальную зп 
def srednija(palk):
    summa=0
    n=len(palk)
    for p in palk:
        summa+=p
    k=summa/n
    return k
#Показывает среднюю зп человека