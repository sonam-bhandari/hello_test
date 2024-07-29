# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Main program
if __name__ == "__main__":
    # Input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Perform addition and subtraction
    sum_result = add_numbers(num1, num2)
    difference_result = subtract_numbers(num1, num2)
    
    # Display the results
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference between {num1} and {num2} is: {difference_result}")
