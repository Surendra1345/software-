# Quadratic solution with multiple inputs from a file
def quadratic_solution(a, b, c, x):
    return a * x**2 + b * x + c

# Read multiple sets of coefficients and values from a file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Process each set and display results
for line in lines:
    a, b, c, x = map(float, line.strip().split())
    result = quadratic_solution(a, b, c, x)
    print(f"For a={a}, b={b}, c={c}, x={x}, the predicted weather condition is {result}.")
