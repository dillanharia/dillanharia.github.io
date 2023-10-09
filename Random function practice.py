import random

hair = ["brown hair","black hair","blonde hair","ginger hair","red hair","blue hair"]
height = ["dwarf","short","average","tall","very tall"]
age = ["a fetus","a baby","a toddler","a teenager","an adult","old"]

number1 = random.randint(0,len(hair)-1)
number2 = random.randint(0,len(height)-1)
number3 = random.randint(0,len(age)-1)

print("Guss has",hair[number1])
print("Guss's height is",height[number2])
print("Guss is",age[number3])