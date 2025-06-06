""" 
1: Ask  user for the numbers
2: Assign variables to the two numbers, such as number_1 and number_2
3: Ask the user for the operation
4: Assign the variable.
5: convert variables for the numbers back into integers, not strings.
6: Ask for operation 
7: if to do the operation based on the 
 After the code understands which operation to do, actually do the operation
8: Print the finished result.

"""
import time
print("Now running tiny calculator v.1")
time.sleep(1)
number_1 = int(input("Please give the first number.\n"))
time.sleep(1)
operation = input("Kindly give the operation in computer form\n")
time.sleep(1)
number_2 = int(input("Please give the second number\n"))
if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
else:
    result = number_1 / number_2
print(result)        
    
    
        