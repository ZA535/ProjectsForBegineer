# I made a calculator in python it is my first Project
print("======Welcome To Calculator======\n")
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    number = int(input("Enter a Number to Perform Operation : "))
    if number == 1:
        num1 = int(input("Enter first Number : "))
        num2 = int(input("Enter Second Number : "))
        print("======>>Output : ", num1 + num2,"  <<======")
    elif number == 2:
        num1 = int(input("Enter first Number : "))
        num2 = int(input("Enter Second Number : "))
        print("======>>Output : ", num1 - num2,"  <<======")
    elif number == 3:
        num1 = int(input("Enter first Number : "))
        num2 = int(input("Enter Second Number : "))
        print("======>>Output : ", num1 * num2,"  <<======")
    elif number == 4:
        num1 = int(input("Enter first Number : "))
        num2 = int(input("Enter Second Number : "))
        print("======>>Output : ", num1 / num2,"  <<======")
    break

