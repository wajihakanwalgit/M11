def power2(number):
    if(number==0):
        return 0
    if((number)&(~(number-1))==number):
        return 1
    number = int(input("Enter the number"))

    if(power2(number)):
        print("\n the number is power of 2")
    else:
        print("\n the number is not power of 2")
    
    


