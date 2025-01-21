# Function of Addition
def addition(m,n):
    return m + n

# Function of Subtration
def subtraction(m,n):
    return m - n

# Function of Multiplication
def multiplication(m,n):
    return m * n

# Function of Division
def division(m,n):
    if n == 0:
        return "Division by 0 is not allowed"
    else:
        return m / n

# Supported Operators
operators = ["+","-","*","/"]

# main program
while True:
    print("Supported Operators (+,-,*,/)")
    operator = input("Enter Your Operator: ").strip()

    if operator not in operators:
        print("Invalid Operator")
    else:
        try:
            m = int(input("Enter First Number: "))
            n = int(input("Enter Second Number: "))

            if operator == "+":
                result = addition(m,n)
            elif operator == "-":
                result = subtraction(m,n)
            elif operator == "*":
                result = multiplication(m,n)
            elif operator == "/":
                result = division(m,n)

            print(result)

            choice = input("Do you want to use again? (y/n): ").strip().lower()
            if choice != "y":
                print("Goodbye! Thanks For Using")
                break
        except ValueError:
            print("Please Enter Valid Number")
            continue
    
