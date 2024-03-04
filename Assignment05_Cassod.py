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
    
    def calculateHypotenuse(self):
        num1 = float(input("Enter the first number."))
        num2 = float(input("Enter the second number."))
        if num1 > 0 and num2 > 0:
            return "Hypotenuse: " + str(((num1**2) + (num2**2))**.5)
        else:
            return "The legs cannot have negative length."
        
    def calculateRectangleArea(self):
        num1 = float(input("Enter the first number."))
        num2 = float(input("Enter the second number."))
        if num1 > 0 and num2 > 0:
            return "Area: " + str(num1*num2)
        else:
            return "The sides cannot have negative length."
        
    def power(self):
        num1 = float(input("Enter the first number."))
        num2 = float(input("Enter the second number."))
        return "Result: " + str(num1**num2)
    
    def findType(self):
        input1 = input("Enter the input.")
        return str(type(input1))
        
def main():
    b = BasicMathOperations()
    
    s = ("\nType a number to choose an operation:"
          + "\n1: Greeting"
          + "\n2: Add Numbers"
          + "\n3: Perform Operation"
          + "\n4: Calculate Square Root"
          + "\n5: Calculate Factorial"
          + "\n6: Count"
          + "\n7: Calculate Square"
          + "\n8: Calculate Hypotenuse"
          + "\n9: Calculate Rectangle Area"
          + "\n10: Calculate Power"
          + "\n11: Find Type"
          + "\n12: Close Program\n\n")
    
    userInput = "0"
    
    while(userInput != "12"):
        userInput = input(s)
        if userInput == "1":
            print(b.greetUser())
        elif userInput == "2":
            print(b.addNumbers())
        elif userInput == "3":
            print(b.performOperation())
        elif userInput == "4":
            print(b.calculateSquareRoot())
        elif userInput == "5":
            print(b.calculateFactorial())
        elif userInput == "6":
            print(b.count())
        elif userInput == "7":
            print(b.calculateSquare())
        elif userInput == "8":
            print(b.calculateHypotenuse())
        elif userInput == "9":
            print(b.calculateRectangleArea())
        elif userInput == "10":
            print(b.power())
        elif userInput == "11":
            print(b.findType())
        elif userInput == "12":
            print("Goodbye!")
        else:
            print("Please enter one of the options.")
            
    
main()