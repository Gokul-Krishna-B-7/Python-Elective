a = True
while a:
    try:
        x = int(input("Please enter a number:"))
        print("Dividing 50 by", x,"will give you: ",50/x)
    except ValueError:
        print("The input is not an integer.Please try again.")