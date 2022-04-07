num = -1

while num != 6:
    print("Enter two numbers:")
    num1 = int(input())
    num2 = int(input())
    
    print("----OPERATIONS-----")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Muliplication")
    print("4 - Division")
    print("5 - Remainder")
    print("6 - Exit")
    
    num = int(input("Choose any operation:"))
    
    if num == 1:
        print("Addition of {0} and {1}: {2}".format(num1, num2, num1 + num2))
    elif num == 2:
        print("Subtraction of {0} and {1}: {2}".format(num1, num2, num1 - num2))
    elif num == 3:
        print("Muliplication of {0} and {1}: {2}".format(num1, num2, num1 * num2))
    elif num == 4:
        if num2 == 0:
            print("Number cannot be divided by zero.")
            continue
        print("Division of {0} and {1}: {2}".format(num1, num2, num1 / num2))
    elif num == 5:
        if num2 == 0:
            print("Number cannot be divided by zero.")
            continue
        print("Remainder of {0} and {1}: {2}".format(num1, num2, num1 % num2))
    elif num == 6:
        print("Exiting...")
        break
    else:
        print("Enter correct choice")
