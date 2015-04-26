# p = 1/2 * k * x^2
# all turns into kinetic -> p = 1/2mv^2
# solve for V
# component v into x and y velocities
# see how long





from array import *
import random
import math

#SETTINGS
TRAINING_AMOUNT = 50
TESTING_AMOUNT  = 10

# 4 Inputs - Constant, Angle from ground (firing angle will be this angle 90-theta), distance pulled


GRAVITY = 9.81;

def findDistance(constant, angle, distance, mass):
    energy = .5 * constant * (pow(distance,2))
    velocityXY = math.sqrt((2*energy)/mass)

    velocityY = velocityXY * math.sin(math.radians(angle))
    velocityX = velocityXY * math.cos(math.radians(angle))

#    print("VelocityXY: %f" % velocityXY)
##    print("VelocityY: %f" % velocityY)
#    print("VelocityX: %f" % velocityX)

    time = velocityY / (.5* GRAVITY)
#    print(time)
    traveled = velocityX * time
    return traveled
    # 0 = velocityY * t - .5*-9.81 * t^2
    #  t = velocityY / (.5*9.81)



# INPUTS

CONSTANT = []
ANGLE = []
DISTANCE = []
MASS = []

#// OUTPUTS
traveled = [ ]



#files
training = open('statsA.dat', 'wb')
testing = open('statsB.dat', 'wb')
count = 0;


for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    constant = random.uniform(100, 400)
    CONSTANT.append(constant)

for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    angle = random.uniform(25, 70)
    ANGLE.append(angle)

for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    distance = random.uniform(2, 5) # in meters
    DISTANCE.append(distance)

for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    mass = random.uniform(1, 5) # in kg
    MASS.append(mass)



	# FIND MEDIAN

for i in range(0, TRAINING_AMOUNT + TESTING_AMOUNT):
    constant = CONSTANT[i]
    angle = ANGLE[i]
    distance = DISTANCE[i]
    mass = MASS[i]

    traveled = findDistance(constant, angle, distance, mass)
#	print( ("%f  %f  %f     %f  %f\n" % (num1, num2, num3, med, avg)).rjust(20) )
    if(i < TRAINING_AMOUNT):
                        #constant angle distance mass    traveled distance
        training.write( ("%f  %f  %f  %f    %f\n" % (constant, angle, distance, mass, traveled)) )
    else:
        testing.write(  ("%f  %f  %f  %f    %f\n" % (constant, angle, distance, mass, traveled)) )
        count = count+ 1
print(count)




