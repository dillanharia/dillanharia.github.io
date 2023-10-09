#subprograms

def job():

	print("Are you employed?")
	employment = input("Y/N: ")
	if employment == "Y" or "y":
		print("Good to hear!")
	elif employment == "N" or "n":
		print("Unfortunate, jobs are really important")
	else:
		print("Please enter either Y or N")
##

def fingers():
	print("How many fingers do you have? ")
	fingernumber = int(input("Enter number: "))
	if fingernumber == 10:
		print("Amazing!")
	elif fingernumber < 10:
		print("Most people have 10. Sorry.")
	elif fingernumber > 10:
		print("Wow! Extra fingers must be cool!")
	else:
		print("Please enter a reasonable numeral. ")
	
##

def feet():
	print("What size are your feet? ")
	feetsize = int(input("Enter number: "))
	if feetsize < 5:
		print("You have very small feet.")
	elif feetsize < 8:
		print("You have average-sized feet.")
	else:
		print("You have big feet.")

##
def workout():
	print("How many days a week do you workout? ")
	days = int(input("Enter number: "))
	if days < 1:
		print("Are you injured or something?")
	elif days <= 2:
		print("Good effort, keep on going!")
	elif days <= 5:
		print("You are dedicated!")
	elif days <= 7:
		print("You are a machine!")
	else:
		days > 7;
		print("There are only 7 days in a week")
##

def age():
	print("How old are you?")
	ageinyears = int(input("Enter number: "))
	if ageinyears >= 18:
		print("You are considered an adult!")
	elif ageinyears > 12:
		print("You are a teenager!")
	elif ageinyears < 4:
		print("You are a toddler!")
	elif ageinyears < 1:
		print("You are a baby!")
	else:
		print("You are not an adult")


#main programs================

job()
print("---------------")
fingers()
print("---------------")
feet()
print("---------------")
workout()
print("---------------")
age()