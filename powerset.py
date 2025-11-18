import math;
def powerSet(set,setsize):
    powerSetsize =(int) (math.pow(2,setsize))
    outer=0
    inner=0
    for outer in range(0,powerSetsize):
        for inner in range(0,setsize):
            if((outer & (1 << inner)) > 0):
                print(set[inner],end=" ")
        print("")
size=int(input("Enter size of set: "))
set=[]
for i in range(0,size):
    n=int(input("Enter element: "))
    set.append(n)
powerSet(set,len(set))    