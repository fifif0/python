#4.3.1.9
def is_prime(num):
    divisor=2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor+=1
    return True


for i in range(1, 30):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
#Odległość pomiędzy punktami

def threeD(Pa,Pb,Pc,Qa,Qb,Qc):
    wynik=((Qa-Pa)**2+(Qb-Pb)**2+(Qc-Pc)**2)**0.5
    if wynik<10:
        return None    
    return wynik


def cheack(var):
    while True:
        var=float(input("Type the coordinates of the three-dimensional space:"))
        if var>=0:
            print(var)
            break
        else:
            print("The given number is less then zero")
    return var


    
Px=cheack(1)
Py=cheack(2)
Pz=cheack(3)
Qx=cheack(1)
Qy=cheack(2)
Qz=cheack(3)


print("Distance between points in the coordinates of three-dimensional space = ",threeD(Px,Py,Pz,Qx,Qy,Qz))



