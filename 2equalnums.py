def checkIfSame(num1, num2):
    if (num1 ^ num2) != 0:
        print("numbers are not equal")
    else:
        print("numbers are equal")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
checkIfSame(num1, num2)
