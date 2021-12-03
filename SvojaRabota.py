from module1 import *
while True:
    a=input("Funktsioonid: \n udalenie-1\n dobavka-2\n sort-3\n minimalka-4\n maksimalka-5\n")
    if a=="1":
        udalenie()
    elif a=="2":
        dobavka()
    elif a=="3":
        sort()
    elif a=="4":
        minimalka()
    elif a=="5":
        maksimalka()
    else:
        print("Pishi цифры, которые указаные")
        break