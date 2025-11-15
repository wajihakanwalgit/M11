def setorNot(number , n):
    if(number &  (1 << (n-1))):
        print("\n Set")
    else:
        print("\n notSet")
number= int(input("Enter number"))
n= int(input("Enter bit number"))
setorNot(number , n)
