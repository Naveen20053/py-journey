print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >=120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:          
        bill = 5
        print("Child tickets are 5$.")
    elif age > 18:
        bill = 12
        print("Adult tickets are 12$.")
    else:
        bill = 7
        print("Youth tickets are 7$.")
    photo_taken = input("Do you want to have a photo taken? Y or N: ")
    if photo_taken == "Y":
        
        bill +=3
        print(f"Your total bill is {bill}$")
            
else:
    print("Sorry you need to grow taller before you can ride this.")
