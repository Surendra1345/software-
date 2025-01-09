# Quadratic solution with keyboard input
def quadratic_solution(a, b, c, x):
    return a * x**2 + b * x + c

# Get coefficients and value from the user
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
x = float(input("Enter the value of x: "))

# Calculate and display the result
result = quadratic_solution(a, b, c, x)
print(f"The predicted weather condition for x={x} is {result}.")
