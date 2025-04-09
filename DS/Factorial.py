number = input("Enter a number: ")
number = int(number)

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print("The factorial of", number, "is", factorial)  # Output: The factorial of 5 is 120

f = 1
while number > 0:
    f *= number
    number -= 1

print("The factorial of", number, "is", f)  # Output: The factorial of 0 is 1
