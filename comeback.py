while True:
    name = input("Enter your name: ")
    if not name.isalpha():
        print("Error: Name must contain only alphabetic characters. Please try again.")
    else:
        print("Valid name entered.")
        break

while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Error: Age must be a valid integer. Please try again.")
    else:
        print("Your name is " + name + " and your age is " + age)
        break  
