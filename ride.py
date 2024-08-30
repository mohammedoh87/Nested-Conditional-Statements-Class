print("Select your ride: ")
print("1. bike")
print("2. car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike: ")
    print("1. Scooty")
    print("2. Scooter")
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected Scooty")
    else:
        print("You have selected Scooter")

elif choice == 2:
    print("What type of car? ")
    print("1. Sadaan")
    print("2. Xuv")
    choice3 = int(input("Enter your choice:"))
    if choice3 == 1:
        print("You have selected Sadaan")
    else:
        print("You have selected XUV") 

else:
    print("WRONG CHOICE")