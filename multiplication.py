import time 
print("Quick! Think of two numbers that multiply together")
print("----------")
time.sleep(3)

# variables
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

# the real answer
total = number1 * number2

# main code
answer = int(input("Enter the multiple of number 1 and 2: "))

if answer == total:
    print("------")
    print("Correct!")
    print("------")
else:
    print("------")
    print("Sorry that is incorrect. The correct answer is",total)
    print("------")