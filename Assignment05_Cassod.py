from cmath import sqrt

class BasicMathOperations:
    
    def greetUser(self):
        first = input("Enter your first name.")
        last = input("Enter your last name.")
        return "Hello, " + first + " " + last + "!"
    
    def addNumbers(self):
        num1 = float(input("Enter the first number."))
        num2 = float(input("Enter the second number."))
        return "Sum: " + str(num1 + num2)
        

    def performOperation(self):
        num1 = float(input("Enter the first number."))
        operator = input("Enter the operation (+, -, *, /)")
        num2 = float(input("Enter the second number."))
        if operator == "+":
            return "Sum: " + str(num1 + num2)
        elif operator == "-":
            return "Difference: " + str(num1 - num2)
        elif operator == "*":
            return "Product: " + str(num1 * num2)
        elif operator == "/":
            if num2 != 0:
                return "Quotient: " + str(num1 / num2)
            else:
                return "Cannot divide by 0."
        else:
            return "Not a valid operator."
        
    def squareRoot(self):
        num1 = float(input("Enter the number."))
        if num1 >= 0:
            return "Square root: " + str(num1**0.5)
        else:
            return "Square root: " + str(sqrt(num1))
          
b = BasicMathOperations()
print(b.squareRoot())