# Get the operation from the user
ctrl = str(input("What is the program of calculator you do?\n"
             "01. + (addition)\n"
             "02. - (subtraction)\n"
             "03. × (multiplication)\n"
             "04. ÷ (division)\n"
             "05. % (remainder)\n"
             "Please enter the option number: "))

# Get the two numbers from the user
num1 = float(input("What is the first number? "))
num2 = float(input("What is the second number? "))

# Perform the operation based on user input
if ctrl == "01":
    print("Result:", num1 + num2) 
elif ctrl == "02":
    print("Result:", num1 - num2)
elif ctrl == "03":
    print("Result:", num1 * num2)
elif ctrl == "04":
    if num2 != 0:  # Check for division by zero
        print("Result:", num1 / num2)
    else: 
        print("Error! Division by zero.")
elif ctrl    == "05":
    print("Result:", num1 % num2)
else:
    print("Error! Invalid option selected")