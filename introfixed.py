while True:
    name= input( "whats your name")
    if name.isalpha():
        break
    else:
        print("input letteres only nga")


while True:
    age = input("How old are you? ")
    if age.isdigit():  # Check if the input is a positive integer
        age = int(age)  # Convert to integer
        break
    else:
        print("Error: Age must be a valid integer. Please try again.")
    
while True:
    favourite_food = input( "whats ur favourite food?")
    if favourite_food.isalpha():
        break
    else:
        print("please avoid enterning numbers")
            
print(f"\nyour name is {name} ,your age is {age} and your favourite food is {favourite_food}") 

input()
