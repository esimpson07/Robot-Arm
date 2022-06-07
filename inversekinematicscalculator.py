import math
from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

#on servos 0 and 4, 0-180 is not 100% safe, since that is the maximum range of the servo
#on servo 15, full open -> closed is 30 -> 85
kit.servo[0].angle = 90
kit.servo[1].angle = 90
kit.servo[2].angle = 45
kit.servo[13].angle = 90
kit.servo[14].angle = 90
kit.servo[15].angle = 30

arm1 = 103
arm2 = 97
pdist = 140
dist = 100
clawLength = 150
baseHeight = 107
x = 200
y = 270
z = 150
tx = -200
ty = 280
tz = 107
steps = 100 #~40 steps will be executed a second, tells how many segments to divide movement into
A = 0
B = 0
C = 0
R = 0

def iloc(a,b,c): #inverse law of cosines (law of arccosines)
    try:
        return(round(math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b))),2))
    except ValueError:
        print("inverse law of cosines unable to calculate!!!")
        return(0)

def smooth(): #servo movement smoothening
    global x
    global y
    global z
    global tx
    global ty
    global tz
    global steps
    if(steps > 0):
        xd = x - tx
        yd = y - ty
        zd = z - tz
        x -= (xd / steps)
        y -= (yd / steps)
        z -= (zd / steps)
        steps -= 1 

def cv(): #check values
    global A
    global B
    global C
    global R
    if(A > 180):
        A = 180
        print("A capping!!!")
    elif(A < 0):
        A = 0
        print("A flooring!!!")
    if(B > 180):
        B = 180
        print("B capping!!!")
    elif(B < 0):
        B = 0
        print("B flooring!!!")
    if(C > 225):
        C = 225
        print("C capping!!!")
    elif(C < 45):
        C = 45
        print("C flooring!!!")
    if(R > 180):
        R = 180
        print("R capping!!!")
    elif(R < 0):
        R = 0
        print("R flooring!!!")

def cn(): #calculate numbers
    global R
    try:
        deg = round(math.degrees(math.atan(y/x)))
    except ZeroDivisionError:
        deg = 0
    if(deg > 0):
        R = deg
    elif(deg < 0):
        R = (180 + deg)
    else:
        R = 90
    global pdist
    pdist = round(math.sqrt(x**2 + y**2),6)
    global dist
    dist = round(math.sqrt((pdist - clawLength)**2 + (z - baseHeight)**2),6)
    global A
    A1 = math.degrees(math.atan(((z-baseHeight)/(pdist-clawLength))))
    A2 = iloc(dist,arm1,arm2)
    A = round((A1 + A2),2)
    global C
    C = iloc(arm1,arm2,dist)
    global B
    B = A + C - 90

while True:
    smooth()
    cn()
    cv()
    print("R =",R)
    print("A =",A)
    print("B =",B)
    print("C =",iloc(arm1,arm2,dist))
    print("pdist =",pdist)
    print("dist =",dist)
    kit.servo[0].angle = R
    kit.servo[1].angle = A
    kit.servo[2].angle = 180 - (C - 45)
    kit.servo[13].angle = B
    sleep(1/40) # 1/40th of a second
