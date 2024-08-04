import sympy as sp
import numpy as np

def monte_carlo_integration_sympy(func, num_samples, interval):
    # Parse the interval
    a, b = map(float, interval.split())

    # Generate random points within the interval
    t_samples = np.random.uniform(a, b, num_samples)

    # Lambdify the function for faster evaluation
    func_lambda = sp.lambdify('t', func, 'numpy')

    # Evaluate the function at the sampled points
    func_values = func_lambda(t_samples)

    # Calculate the maximum absolute function value within the interval
    y_max = max(abs(func_lambda(val)) for val in np.linspace(a, b, 1000))

    # Generate random y values
    y_samples = np.random.uniform(0, y_max, num_samples)

    # Count the number of points under the curve
    count = np.sum(y_samples < func_values)

    # Estimate the integral
    integral_approx = (count / num_samples) * (b - a) * y_max
    return integral_approx

# Read inputs
function_str = input().strip()
num_samples = int(input().strip())
interval = input().strip()

# Parse the function
t = sp.Symbol('t')
function = sp.sympify(function_str)

# Perform Monte Carlo integration
approximate_integral = monte_carlo_integration_sympy(function, num_samples, interval)
print(np.round(float(approximate_integral), 2))

