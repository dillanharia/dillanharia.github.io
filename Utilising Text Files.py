
# boy names

myFile = open("boynames","w")
print("Please enter 3 boy names. ")

for i in range(3):
	boy = input("Enter name: ")
	myFile.write(boy+"\n")
myFile.close()

print("-----") # organisation

# girl names
myFile = open("girlnames","w")
print("Please enter 3 girl names. ")

for i in range(3):
	girl = input("Enter name: ")
	myFile.write(girl+"\n")
myFile.close()

print("----------------------")
question = input("Do you want to display the boy names or the girl names? ")
print("----------------------")

if question == ("boy names"):
	myFile = open("boynames","r")
	lines1 = myFile.readlines()
	lines1.sort()
	for linestorage1 in lines1:
		print(linestorage1)
	
elif question == ("girl names"):
	myFile = open("girlnames","r")
	lines2 = myFile.readlines()
	lines2.sort()
	for linestorage2 in lines2:
		print(linestorage2)
else:
	question != ("boy names") or ("girl names")
	print("Please specify whether you want to display the 'boy names' or 'girl names'")