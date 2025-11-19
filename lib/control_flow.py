# 1. admin_login returns "Access granted" for correct credentials
def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


# 2. hows_the_weather returns a string based on temperature
def hows_the_weather(temp):
    if temp < 40:
        return "It's brisk out there!"
    elif temp < 65:
        return "It's a little chilly out there!"
    elif temp > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


# 3. fizzbuzz returns Fizz/Buzz/FizzBuzz or num
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


# 4. calculator performs +, -, *, /, or prints invalid
def calculator(operation, a, b):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        print("Invalid operation!")
        return None
