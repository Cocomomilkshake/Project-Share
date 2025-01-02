# Reminding the user about the program's sensitivity to capitalization
print("-------------------------THIS PROGRAM IS CASE SENSITIVE-------------------------")

# List to store previous values
stored_vals = []

# While loop for the code to run forever
while True:

    # Option to choose an arithmetic operator
    mode = input("Type of operation (Add, Sub, Multiply, Divide, Exponent, Root): ")

    # Option to assign values to ONLY two variables
    x = input("Let x: ")
    y = input("Let y: ")

    # The calculator:
    # Variable to store values in
    R = 0

    # Addition
    if mode == "Add":
        print(x + " + " + y + " =")
        R = float(x) + float(y)
        print(R)

    # Subtraction
    elif mode == "Sub":
        print(x + " - " + y + " =")
        R = float(x) - float(y)
        print(R)

    # Multiplication
    elif mode == "Multiply":
        print(x + " * " + y + " =")
        R = float(x) * float(y)
        print(R)

    # Division
    elif mode == "Divide":
        print(x + " / " + y + " =")
        R = float(x) / float(y)
        print(R)

    # Exponentiation
    elif mode == "Exponent":
        print(x + " ^ " + y + " =")
        R = float(x) ** float(y)
        print(R)

    # Rooting
    elif mode == "Root":
        print(x + " ^ (1 / " + y + ") =")
        R = float(x) ** (1 / float(y))
        print(R)

    # Triggered upon an invalid string registered
    else:
        print("Invalid operator OR mistake in the capitalization")

    # Add the result into a list and print it out
    stored_vals.append(R)

    # If statement to remove the 10th value stored in the list
    if len(stored_vals) > 9:
        stored_vals.pop(0)

    print(stored_vals)