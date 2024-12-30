def simple_calculator(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"

print(simple_calculator(10, 5, "add"))
print(simple_calculator(10, 5, "subtract"))
print(simple_calculator(10, 5, "multiply"))
print(simple_calculator(10, 5, "divide"))
print(simple_calculator(10, 0, "divide"))     
print(simple_calculator(10, 5, "modulus"))   