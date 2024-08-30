medical_cause = input("Enter your medical cause: Y or N")
attendance = int(input("Enter your Attedndance"))

if medical_cause == "Y" or medical_cause == "y":
    print("You are allowed")

else:
    if attendance >= 75:
        print("You are allowed")
        
    else:
        print("You are not allowed")
            


