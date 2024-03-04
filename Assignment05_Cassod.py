class BasicMathOperations:
    
    def greetUser(self):
        first = input("Enter your first name.")
        last = input("Enter your last name.")
        return "Hello, " + first + " " + last + "!"
    
b = BasicMathOperations()
print(b.greetUser())


    