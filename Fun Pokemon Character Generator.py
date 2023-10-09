# --------------random function--------------

import random

PokemonClass = ["Electric","Fire","Water","Earth","Shadow","Ice","Poison","Steel","Dragon","Wind","Ghost"]
gender = ["Male","Female"]
strength_value = ["10","15","20","25","30","35","40","45","50","55","60","65","70","75","80","85","90"]
magic_value = ["10","15","20","25","30","35","40","45","50","55","60","65","70","75","80","85","90"]
dexterity_value = ["10","15","20","25","30","35","40","45","50","55","60","65","70","75","80","85","90"]
ExtraAbilities = ["Flight","Rage","Brace","Prediction","Invisibility","Super Speed","Teleportation"]

number1 = random.randint(0,len(PokemonClass)-1)
number2 = random.randint(0,len(gender)-1)
number3 = random.randint(0,len(strength_value)-1)
number4 = random.randint(0,len(magic_value)-1)
number5 = random.randint(0,len(dexterity_value)-1)
number6 = random.randint(0,len(ExtraAbilities)-1)

# --------------variables--------------
filler = "------------------------------"

# --------------information--------------
# classes
electricity = "Your pokemon wields the power of electricity, electrocuting your opponents on turn."
fire = "Your pokemeon wields the power of fire, burning your opponents on turn"
water = "Your pokemeon wields the power of water, one with the aquamarine."
earth = "Your pokemeon wields the power of earth, dealing extra 5% damage. "
shadow = "Your pokemeon wields the power of shadow, blinding your opponents."
ice = "Your pokemeon wields the power of ice, freezing your opponents on turn."
poison = "Your pokemeon wields the power of poison, dealing damage over time rather than all at once. "
steel = "Your pokemeon wields the power of steel, ultimate protection. "
dragon = "Your pokemeon wields the power of dragons,"
magma = "Your pokemeon wields the power of magma,"
wind = "Your pokemeon wields the power of the wind,"
ghost = "Your pokemeon wields the power of a ghost-like form."

# Gender
male = "Your pokemon is male."
female = "Your pokemon is female."

#statpoints
strength = "A measure of how physically strong your pokemon is. Strength controls how powerful or how much damage your pokemon has."
magic = "Magic or is a measure indicates your pokemon's power to use special magical abilities. "
dexterity = "A measure of how agile a character is. Dexterity controls attack and movement speed and accuracy, as well as evading an opponent's attack."

# Skillpoints (strength, magic, dexterity)
ten_to_thirty = "Eh.. your pokemon is quite weak for."
thirty_to_fifty = "Your pokemon's average for."
fifty_to_seventy = "Not bad, your pokemon is average for."
seventy_to_90 = "Wow, your pokemon is quite strong for."

# Extra abilities
flight = "Take the power of flight, leaping down onto your opponents and dealing extra damage."
rage = "Enrage yourself with the power of the gods, dealing 10% more damage."
brace = "Receieve 10% protection when bracing yourself."
prediction = "Predict the opponents move and you reflect it back at them with 50% power."
invisibility = "Go invisible, earning your pokemon an extra turn."
superspeed = "Unleash your super speed, receiving an extra turn on use."
teleportation = "Teleport behind your opponent for a 20% damage increase."


# --------------main program--------------
print(filler)
print("YOUR POKEMON HAS BEEN CREATED")
print(filler)
print("Class =",PokemonClass[number1])
print("Gender =",gender[number2])
print("Strength =",strength_value[number3])
print("Magic =",magic_value[number4])
print("Dexterity =",magic_value[number5])
print("Extra ability =",ExtraAbilities[number6])
print(filler)

x = 0
while x == 0:
	print(filler)
	moreinformation = input("Do you want to know any more information about your stats? Specify with 'Yes' or 'No': ")
	if moreinformation == "Yes":
			questions = input("Enter the exact stat to see more information about it: ")
			# classes
			if questions == "Electricity":
				print(electricity)
			elif questions == "Fire":
				print(fire)
			elif questions == "Water":
				print(water)
			elif questions == "Earth":
				print(earth)
			elif questions == "Shadow":
				print(shadow)
			elif questions == "Ice":
				print(ice)
			elif questions == "Poison":
				print(poison)
			elif questions == "Steel":
				print(steel)
			elif questions == "Dragon":
				print(dragon)
			elif questions == "Ghost":
				print(ghost)
			# gender
			elif questions == "Male":
				print(male)
			elif questions == "Female":
				print(female)
			# statpoints
			elif questions == "Strength":
				print(strength)
			elif questions == "Magic":
				print(magic)
			elif questions == "Dexterity":
				print(dexterity)
			# extra abilities
			elif questions == "Flight":
				print(flight)
			elif questions == "Rage":
				print(rage)
			elif questions == "Brace":
				print(brace)
			elif questions == "Prediction":
				print(prediction)
			elif questions == "Invisibility":
				print(invisibility)
			elif questions == "Super speed":
				print(superspeed)
			elif questions == "Teleportation":
				print(teleportation)
			
	elif moreinformation == "No":
		print("Okay!")
		x = 1
