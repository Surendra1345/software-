# Quadratic solution with file input (single set)
def quadratic_solution(a, b, c, x):
    return a * x**2 + b * x + c

# Read coefficients and value from a file
with open("input.txt", "r") as file:
    data = file.readline().strip().split()
    a, b, c, x = map(float, data)

# Calculate and display the result
result = quadratic_solution(a, b, c, x)
print(f"The predicted weather condition for x={x} is {result}.")
