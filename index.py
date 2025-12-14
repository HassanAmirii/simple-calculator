def input_func(): 
    first_number = int(input("Enter first digit: "))
    operator = input("Enter operator: ")
    second_number = int(input("Enter second digit: "))
    return first_number, operator, second_number

def add(a,b):
    result = a + b 
    print(result) 

def minus(a,b):
    result = a - b
    print(result) 

def multiply(a,b):
    result = a * b
    print(result)

def divide(a,b):
    if b != 0:
        result = a /b
        print(result)
    else:
        print("undefine: cannot divide by zero")


first_number, operator, second_number = input_func()

if operator == "+":
    add(first_number, second_number)
elif operator == "-":
    minus(first_number, second_number)
elif operator == "*":
    multiply(first_number, second_number)
elif operator == "/":
    divide(first_number, second_number)
else:
    print("error in 'operator-input' use either : +, -, /, *. ")
    input_func()






     

