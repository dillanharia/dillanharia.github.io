# --------variables--------
x = 0
uppercase=0
lowercase=0
specialcharactersindex = 0
specialcharacters = ['[','@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','}','{','~',':',']']
numbers = ['1','2','3','4','5','6','7','8','9']
number = 0

# --------main program--------

print("Welcome to your password reset! ")
print("- Please ensure your password is greater than 8 characters")
print("- Please include atleast one uppercase and lowercase letter")
print("- Please include atleast one special character")
while x == 0:
	print("------------------------------")
	password = input("Enter your new password: ")
	(password)

	if len(password) < 8:
		print("!! Your password is too short. Please enter one longer than 8 characters. ")
	else: 	
		for letter in password:
			if letter.isupper():
				uppercase = 1
			elif letter.islower():
				lowercase = 1
			elif letter in numbers:
				number = 1
			elif letter in specialcharacters:
				specialcharactersindex = 1
				
	if uppercase == 0:
		print("!! Please include an uppercase letter in your password")
	elif lowercase == 0:
		print("!! Please include a lowercase letter in your password")
	elif numbers == 0:
		print("!! Please include a number")
	elif specialcharactersindex == 0:
		print("!! Please include a special character")
	else:
		print("Accepted")
		print("---")
		
		doublecheck = input("Please re-enter your password: ")
		if doublecheck == password:
			x = 1
			print("Your password has been changed.")
		else:
			print("Passwords do not match. Please try again.")
	
	

		