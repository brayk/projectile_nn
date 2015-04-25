# Kameron Bray
# Sunny Ali
#
# CSC 180 - Average and Median

from array import *
import random
import statistics

# BOUNDARY CASES
# 0,0,0;
# 50,50,50;
# 100,100,100;
# 0,50,100;
# 100, 50, 0
# 5 cases

#SETTINGS
TRAINING_AMOUNT = 50
TESTING_AMOUNT  = 50
BOUNDARIES = 5

# INPUTS
FirstNumber = []
SecondNumber = []
ThirdNumber = []

#// OUTPUTS
med = []
avg = []

#files
training = open('statsA.dat', 'wb')
testing = open('statsB.dat', 'wb')
count = 0;

# GENERATE
    # BOUNDARY CASES
#FirstNumber.append(0);
#FirstNumber.append(50);
#FirstNumber.append(100);
#FirstNumber.append(0);
#FirstNumber.append(100);


#SecondNumber.append(0);
#SecondNumber.append(50);
#SecondNumber.append(100);
#SecondNumber.append(50);
#SecondNumber.append(50);

#ThirdNumber.append(0);
#ThirdNumber.append(50);
#ThirdNumber.append(100);
#ThirdNumber.append(100);
#ThirdNumber.append(0);

for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    num1 = random.uniform(1.0, 100.0)
    FirstNumber.append(num1)

for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    num2 = random.uniform(1.0, 100.0)
    SecondNumber.append(num2)

for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
    num3 = random.uniform(1.0, 100.0)
    ThirdNumber.append(num3)

	# FIND MEDIAN

for i in range(0, TRAINING_AMOUNT + TESTING_AMOUNT):
    num1 = FirstNumber[i]
    num2 = SecondNumber[i]
    num3 = ThirdNumber[i]

    items = [num1, num2, num3]

    med = statistics.median(items)
#   if(num1 < num2 and num1 > num3):
#        med = num1
#    elif(num2 < num3  and num2 > num1):
#        med = num2
#    elif(num1 < num3 and num1 > num2):
#        med = num1
#    elif(num2 > num3 and num2 < num1):
#        med = num2
#    elif(num3 > num2 and num3 < num1):
#        med = num3
#    elif(num3 < num2 and num3 > num1):
#        med = num3
#    elif(num2 < num1 and num2 > num3):
#        med = num2

    avg = (num1+num2+num3)/3
##	print( ("%f  %f  %f     %f  %f\n" % (num1, num2, num3, med, avg)).rjust(20) )
    if(i < TRAINING_AMOUNT):
        training.write( ("%f  %f  %f     %f  %f\n" % (num1, num2, num3, med, avg)) )
    else:
        testing.write( ("%f  %f  %f     %f  %f\n" % (num1, num2, num3, med, avg)) )
        count = count+ 1
print(count)


#

