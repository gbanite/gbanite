#numbers.py
# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the first integer: "))
num3 = int(input("Enter the first integer: "))

# Calculae and print the required operations
sum_of_numbers = num1 + num2 + num3
difference = num1 - num2
product = num3 * num1
division = (num1 + num2 + num3) / num3

print("Sum of all numbers:", sum_of_numbers)
print("First number minus second number:", difference)
print("Third number multiplied by the first number:", product)
print("Sum of all three numbers divided by the third number:", division)