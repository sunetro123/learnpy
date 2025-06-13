# Old version 1.0.0
# 1: Get pet name
# 2:Get pet status
# 3:print stuff if certain status is achieved.

# New version: 2.0.0
# 1:establish while True
# 2:get pet Name
# 3:get pet status
# 4: if pet status is like HaPpy, use .lower to convert into lowercase
# 5:if result is one stated, print the correct reaction
# 6:if result is not given, print confused phrase
# 7:print request for exit, and break the while loop of necessary
# 8: use time.sleep and request certain exits during every part of the code
import time
import sys
while True:
    print("Now running pet simulator v.2.0.0")
    time.sleep(1)
    pet_name = input("What is your pet's name?\n" )
    pet_status = input("Is your pet happy, sad, or hungry?\n")
    pet_status = pet_status.lower()
    if pet_status == "happy":
        print(f"{pet_name} is doing a victory dance.\n")
    elif pet_status == "sad":
        print(f"{pet_name} needs a hug")
    elif pet_status == "hungry":
        print(f"{pet_name} needs food to survive. You must feed your pet.")
    else:
        print(f"{pet_name} is confused. Try giving a listed emotion such as happy, sad, or hungry.\n")
    end_rquest = input("Would you like to exit this simulator?\n Please answer either y or n, case insensitive.\n")
    end_rquest = end_rquest.lower()
    if end_rquest == "y":
        time.sleep(1)
        print("Goodbye.")
        break            




