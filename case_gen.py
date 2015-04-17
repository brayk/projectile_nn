from array import *
import random

#SETTINGS


TRAINING_AMOUNT = 25
TESTING_AMOUNT  = 10


# INPUTS
FirstNumber = []
SecondNumber = []
ThirdNumber = []

#// OUTPUTS
med = []
avg = []





for i in range(1,(TRAINING_AMOUNT + TESTING_AMOUNT + 1)):
	if(i == 1):
		print("==============Training===============")
	elif (i == TRAINING_AMOUNT + 1):
		print("===============Testing===============")
	num1 = random.uniform(1.0, 100.0)
	num2 = random.uniform(1.0, 100.0)
	num3 = random.uniform(1.0, 100.0)
	
	FirstNumber.append(num1)
	SecondNumber.append(num2)
	ThirdNumber.append(num3)

	# FIND MEDIAN
	
	if(num1 < num2 and num1 > num3):
		med = num1
	elif(num2 < num3  and num2 > num1):
		med = num2
	else:
		med = num3


	med = med 
	avg = (num1+num2+num3)/3
	space = "  "
	tab   = "     "
	print( ("%f  %f  %f     %f  %f" % (num1, num2, num3, med, avg)).rjust(20) )



