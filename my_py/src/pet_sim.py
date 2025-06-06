"""
Plan:
1: Ask for the pet name
2: Assign into variable
3: Ask for the pet status
4: Assign that mood into a variable
5: If mood then print certain phrase
"""
import time
pet_name = input("What is your pet's name?\n")
pet_status = input("Is your pet happy, sad, or hungry?\n")
print(f"pet_status value: {pet_status}")
if pet_status == "happy":
    print(f"{pet_name}'s so happy, 'cause today he sold the world")
elif pet_status == "sad":
    print(f"{pet_name} has PTSD")
else:
    print(f"{pet_name} needs to be taken to the nearest Five Guys place")




