# 1: make a while loop
# 2: get the first number(put as variable)
# 3:get the operation(put as variable based on string input)
# 4: get the second number (put as variable)
# 5: get result as variable
# 6: repeat.
# 7:make if statement that makes sure that if the person types "exit", the while loop breaks.
import time
while True:
    print("Now running rpt_calc v.2.0.0")
    time.sleep(1)
    first_num_or_exit = input("Please give the first number or type exit to stop.\n")
    if first_num_or_exit == "exit":
        print("Goodbye.\n")
        break
    first_num = int(first_num_or_exit)

    time.sleep(1)
    operation = input("please give one of either +,-,*,and /. Complex operations coming soon.\n")
    time.sleep(1)
    second_num = int(input("Please give the second number\n"))
    if operation == "+":
        result = first_num + second_num
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
    elif operation == "/":
        result = first_num / second_num    
    else:
        print("Command not understood. Please only give either +,-,/,or * to represent the simple operations.")    
    print(f"Your result is {result}. \n") 
    end_request =input("Would you like to exit?\nSay y or n\n")
    if end_request == "y":
        print("Goodbye.\n")
        break

    # time.sleep(10)

