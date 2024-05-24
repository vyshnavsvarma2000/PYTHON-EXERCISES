class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b


calc = Calculator()

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice in [1, 2, 3, 4, 5]:
        if choice == 5:
            break

        a = int(input("Enter the first number "))
        b = int(input("Enter the second number "))

        if choice == 1:
            print("Addition value is ", calc.addition(a, b))

        elif choice == 2:
            print("Subtraction value is ", calc.subtraction(a, b))

        elif choice == 3:
            print("Multiplication value is ", calc.multiplication(a, b))

        elif choice == 4:
            if not b == 0:
                print("Division value is ", calc.division(a, b))
            else:
                print("Division by zero is not possible ")

    else:
        print("Wrong input")
