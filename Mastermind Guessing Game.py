# short variables
rule1 = print("- This is a number guessing game.")
rule2 = print("- There are two difficulties. 'Easy' and 'Hard' mode.")
rule3 = print("- Easy Mode gives you a 3 digit number to guess. Hard mode gives you a 4 digit number to guess")
rule4 = print("- You will have to keep on inputting guesses until atleast one of your digits are correct. At that point, the console will tell you which digit is correct.")
rule5 = print("- Note, the first digit has position 0, second digit position 1, etc.")
minitextfiller = "------"
textfiller = "--------------------------------------"

# subroutines
def easymode():
    import random
    
    RandomNumber = random.randint(100, 999)
    RandomNumberTotal = str(RandomNumber)
    print(minitextfiller)
    print("You have to guess a three-digit number.")
    y = 0
    while y == 0:
        ask = input("Enter guess: ")
        found = 0
        x = 0
        for i in RandomNumberTotal:
            if ask[x] == i:
                print("The number found in position", x, "is correct")    
                found = found + 1
                if found == 3:
                    y = 1
            x = x + 1

#######################

def hardmode():
    import random
    
    RandomNumber = random.randint(10000, 99999)
    RandomNumberTotal = str(RandomNumber)

    print(minitextfiller)
    print("You have to guess a four-digit number.")
    y = 0
    while y == 0:
        ask = input("Enter guess: ")
        found = 0
        x = 0
        for i in RandomNumberTotal:
            if ask[x] == i:
                print("The number found in position", x, "is correct")
                found = found + 1
            x = x + 1
        
        if found == 4:
            y = 1

# main program
print(textfiller)
(rule1)
(rule2)
(rule3)
(rule4)
(rule5)
p = 0
while p == 0:
    difficulty = input("'Easy' difficulty or 'Hard' difficulty: ")
    if difficulty == "Easy" or difficulty == "easy":
        easymode()
        p = 1
    elif difficulty == "Hard" or difficulty == "hard":
        hardmode()
        p = 2
    else:
        (textfiller)
        print("Please enter either 'Easy' or 'Hard' mode.")
        (textfiller)
