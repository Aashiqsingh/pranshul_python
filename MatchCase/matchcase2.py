no1 = int(input("Enter a number"))
no2 = int(input("Enter another number"))

choice = input("1 for Add \n2 for Sub \n3 for Mul \n4 for Div \n\n Enter your choice :- ")

match choice:
    case "1":
        print("Addition = ",no1+no2)
    case "2":
        print("Subtract = ",no1-no2)
    case "3":
        print("Multiply = ",no1*no2)
    case "4":
        print("Division = ",no1//no2)

