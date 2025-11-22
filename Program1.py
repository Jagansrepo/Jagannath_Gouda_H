class Calculator:
    def calculate(self,a:float,b:float,op:str):
        if op == "add":
            return a+b
        elif op == "sub":
            return a-b
        elif op == "mul":
            return a*b
        elif op == "div":
            return a/b
        

a=float(input("Enter a: "))
b=float(input("Enter b: "))
op=input("Enter operation (add, sub, mul, div): ")

cal=Calculator()

print("Result: ",cal.calculate(a,b,op))
        