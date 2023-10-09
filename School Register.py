#-----------------server-----------------
import time
import datetime

x = datetime.datetime.now()

guide = ("Please enter 'Y' for Present or 'N' if Absent")
space = ("")


#-----------------lists-----------------
students = ["Dillan", "Dylan", "Tio", "Ray", "Will", "Shade", "Saanvi", "Yelena"] 
present = []
absent = []

#-----------------main-----------------
print("-----------------")
print(space)
print("Welcome to the register for:")
print(x.strftime("%x"))
print(guide)
print(space)

for i in students:
	print("-----------------")
	print(i)
	attendance = input("Is this student present? Y/N: ")
	if attendance == "Y":
		present.append(i)
		print(i,"was added to the present list ")

	elif attendance == "N":
		absent.append(i)
		print(i,"was added to the absent list")
		
	else:
		print("Please enter either Y or N")

print("-----------------")
print("Register complete")
print("-----------------")

import time
time.sleep(0.5)

print("Present list:")
print(present)
print("Absent list:")
print(absent)





