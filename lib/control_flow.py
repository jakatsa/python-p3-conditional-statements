#!/usr/bin/env python3
def admin_login(username, password):
    if (username.lower() == "admin" or username.lower() == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"



def hows_the_weather(temperature):
    response=""
    if temperature < 40:
        response="brisk"
    elif   temperature >= 40 and temperature <= 65 :
        response = "a little chilly"
    elif   temperature > 85:
        response = "too dang hot"

    else:
         response = "perfect"
    return f"It's {response} out there!"     


# Example usage:
temperature = 75
result = hows_the_weather(temperature)
print(result)



def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# Example usage:
for i in range(1, 21):
    print(fizzbuzz(i))



 

def calculator(operation, num1, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    # Get the corresponding function for the operation, or None if invalid
    func = operations.get(operation)

    if func:
        return func(num1, num2)
    else:
        print("Invalid operation!")

# Example usage:
result = calculator('+', 5, 3)
print(result)

result = calculator('-', 7, 2)
print(result)

result = calculator('*', 4, 6)
print(result)

result = calculator('/', 8, 2)
print(result)
