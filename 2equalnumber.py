def checkifsame(number1,number2):
    if((number1 ^ number2 ) != 0):
        print("number are not equal")
    else:
        print("number are equal")
number1= int(input("enter number1"))
number2=int(input("Enter number 2"))

checkifsame(number1 , number2)
