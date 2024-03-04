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
        
    def calculateSquareRoot(self):
        num1 = float(input("Enter the number."))
        if num1 >= 0:
            return "Square root: " + str(num1**0.5)
        else:
            return "Square root: " + str(sqrt(num1))
        
    def calculateFactorial(self):
        num1 = int(input("Enter the number."))
        
        if num1 > 0:
            f = num1
            while f > 1:
                f -= 1
                num1 *= f
            return "Factorial: " + str(num1)
        elif num1 < 0:
            num1 *= -1
            f = num1
            while f > 1:
                f -= 1
                num1 *= f
            return "Factorial: " + str(-1 * num1)
        else:
            return "Factorial: 1"
        
    def counting(self):
        num1 = int(input("Enter the start number."))
        num2 = int(input("Enter the end number."))
        
        s = ""
        
        if num1 < num2 :
            while num1 <= num2:
                s+= str(num1) + " "
                num1 +=1
        elif num1 > num2:
            while num1 >= num2:
                s+= str(num1) + " "
                num1 -=1
        else:
            s = "The numbers are equal."
        
        return s
            
    def calculateSquare(self):
        num1 = float(input("Enter the number."))
        return "Sum: " + str(num1**2)
    
    def calculateSquare(self):
        num1 = int(input("Enter the start number."))
        num2 = int(input("Enter the end number."))
        if num1 > 0 and num2 > 0:
            return "Hypotenuse: " + str(((num1**2) + (num2**2))**.5)
        else:
            return "The legs cannot have negative length."
        
    def calculateRectangleArea(self):
        num1 = int(input("Enter the start number."))
        num2 = int(input("Enter the end number."))
        if num1 > 0 and num2 > 0:
            return "Area: " + str(num1*num2)
        else:
            return "The sides cannot have negative length."
        
b = BasicMathOperations()
print(b.calculateRectangleArea())