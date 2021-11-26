from module1 import*
palk=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def palgad(p,i):
    valik=input("srednjaja zarplata - 1,\nminimalka zp - 2,\nMaksimalka zarplata - 3,\nDelete 4eloveka - 4,\nADD 4eloveka - 5")
    if valik=="1":
        kesk_palk=round(keskmine(palk),2)
        print("srednjaja ",kesk_palk)
        print()
        print()
    elif valik=="2":
        m_palgad,nimi=minimum(palk,inimesed)
        for n in nimi:
            print(m_palgad[0], " budet ",n)
            print()
            print()
    elif valik=="3":
        max_palk,kto=maksimum(palk,inimesed)
        print("maksimalnja zp ", max_palk, " budet  ",kto)
        print()
        print()
    elif valik=="4":                                       
        p,i=delete(palk,inimesed)
        print(palk,inimesed)
        if len(inimesed)==0:
            print("Tühi list")
        else:
            for i in range(len(inimesed)):
                print(inimesed[i]," saab kätte ", palk[i])
    elif valik=="5":                                        
        i=adding(palk,inimesed)
        print("Obnovlenie spiski: ")
        print(inimesed)
        print(palk)
        print("Dobavlen element", inimesed[-1])
        print("S zp", str(palk[-1])+'€')
    elif valik=="7":
        x,y=kalk()
while True:

    palgad(palk,inimesed)