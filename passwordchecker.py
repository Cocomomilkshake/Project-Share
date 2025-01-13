while True:
    email = input("Enter your email address: ")
    if "@" not in email:
        print("Invalid email format")
    elif ".com" not in email:
        print("Invalid format")
    else:
        print("Valid email")
        break
        
        
            
        
    
 
while True:
     password= input("enter password")
     if len(password)>8:
         password = str(password)
         print ("password length is appropriate")
         break
     else:
         print("password should be 8 letters")
         input("Press Enter to try again...")

input("Press Enter to exit...")