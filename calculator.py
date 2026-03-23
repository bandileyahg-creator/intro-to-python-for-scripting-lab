print("Welcome to the calculator script!")
num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
oper = input("Please enter the operation (+, -, *, /)")

num1 = float(num1)
num2 = float(num2)

if oper == "+":
    print("You've chosen to add")
    sum =num1 + num2
    print(sum)
elif oper == "-":
    print("You've chosen to subtract")
    diff = num1 - num2
    print(diff)
elif oper == "*":
    print("you've chosen to multiply")
    prod = num1 * num2
    print(prod)
elif oper == "/":
    print("Ypu've chosen to divide")  
    quot = num1 / num2
    print(quot) 
else:
    print("You've made an invalid")   