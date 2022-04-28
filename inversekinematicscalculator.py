import math

#definitions
arm1 = 100
arm2 = 80
clawLength = 30
baseHeight = 30

#variables
dist = 100
A1 = 0
A2 = 0
A = 0
B1 = 0
B2 = 0
B = 0
C = 0
x = 0
y = 0
z = 0

x = 30
y = 70
z = 40

#Angle R = rotation servo angle
#Angle A = first lift servo angle
#Angle C = second lift servo angle
#Angle B = third lift servo angle
#Angle D = fourth servo, claw rotation angle
#Angle E = final servo, claw open/close angle

''' Array will be cartesian coordinates '''
''' # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
  ^ # # # # # # # # # # # # # # # # # #
  | # # # # # # # # # # # # # # # # # #
  Y # # # # # # # # # # # # # # # # # #
  | # # # # # # # # # # # # # # # # # #
  v # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # #
    # # # # # # # # Claw# # # # # # # #
                < - - X - - >
'''

def iloc(a,b,c): #inverse law of cosines
    return(round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))),6))

def cbt():
    return(math.sqrt((dist - clawLength)**2 + (z - baseHeight)**2))

def fA():
    A1 = math.degrees(math.tan((z-baseHeight)/(dist-clawLength)))
    A2 = iloc(cbt(),arm1,arm2)
    if(baseHeight > z):
        A = A2 - A1
    elif(baseHeight < z):
        A = A2 + A1
    else:
        A = A2
    return(A)

def calc(x,y,z):
    dist = round(math.sqrt(x**2 + y**2),6)
    print(dist)
    C = iloc(arm1,arm2,cbt())
    A = fA()
    B = C + A
    print(C,A,B)

calc(30,70,30)

'''print("Distance =",dist)
print("c =",cbt())
print("Angle A =",fA())
print("Angle C =",iloc(arm1,arm2,cbt()))'''
