# Quadratic solution with hard-coded variables
def quadratic_solution(a, b, c, x):
    return a * x**2 + b * x + c

# Hard-coded coefficients and value
a, b, c = 1, -3, 2  # Example: y = x^2 - 3x + 2
x = 5  # Example input value for x (e.g., time)

# Calculate and display the result
result = quadratic_solution(a, b, c, x)
print(f"The predicted weather condition for x={x} is {result}.")
