import sympy as sp
import numpy as np

# Define the function symbol
x = sp.symbols('x')

# Define the function to integrate
def f(x):
    return 100 * sp.sin(x) + 12 * (x ** 2) * sp.cos(x)

# Rectangle method
def rectangle_integration(func, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_val = a + i * h
        integral += func.subs(x, x_val)
    integral *= h
    return integral

# Midpoint method
def midpoint_integration(func, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_val = a + (i + 0.5) * h
        integral += func.subs(x, x_val)
    integral *= h
    return integral

# Trapezoidal method
def trapezoidal_integration(func, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (func.subs(x, a) + func.subs(x, b))
    for i in range(1, n):
        x_val = a + i * h
        integral += func.subs(x, x_val)
    integral *= h
    return integral

# Simpson's rule with integral in each interval
def simpsons_integration(func, a, b, n):
    h = (b - a) / n
    integral = 0
    x = sp.symbols('x')
    for i in range(n):
        x0 = a + i * h
        x1 = a + (i + 1) * h
        integral += (h / 6) * (func.subs(x, x0) + 4 * func.subs(x, (x0 + x1) / 2) + func.subs(x, x1))
        
    return integral



# Main function
if __name__ == "__main__":
    # Read input
    function_str = input().strip()
    n = int(input().strip())
    a, b = map(float, input().strip().split())

    

    # Convert the function string into a SymPy expression
    function = sp.sympify(function_str)

    definite_integral = sp.integrate(function, (x, a, b))

    # Perform integration using each method
    methods = [rectangle_integration, midpoint_integration, trapezoidal_integration, simpsons_integration]

    for method in methods:
        integral = method(function, a, b, n)
        error = abs(integral - definite_integral)
        print(str(np.round(float(integral), 3)) + " " + str(np.round(float(error), 3)))


