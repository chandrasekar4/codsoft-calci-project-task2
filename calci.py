# user input1
num1 = float(input("Enter the first number: "))

# user input2
num2 = float(input("Enter the second number: "))

#  operations
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# choice of 4 basic operator
choice = input("Enter choice (1/2/3/4): ")

# choose a oprator 
if choice == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")

elif choice == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")

elif choice == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")

elif choice == '4':
    # division method
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of division is: {result}")

else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
