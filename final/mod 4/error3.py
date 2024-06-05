a = True
while a:
    try:
        x = int(input("Please enter a number: "))
    except ValueError:
        print("The input was not a valid integer. Please try again...")
    else:
        print("Dividing 50 by", x,"will give you :", 50 / x)