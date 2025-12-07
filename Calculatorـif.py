# Simple Calculator using if/elif

print("Simple Calculator")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid Input")
