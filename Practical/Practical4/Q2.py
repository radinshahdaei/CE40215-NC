import numpy as np

def polynomial_regression_vandermonde(x, y, degree):
    """
    Perform polynomial regression using the Vandermonde matrix.

    Parameters:
    x (numpy.ndarray): Input feature values.
    y (numpy.ndarray): Output target values.
    degree (int): Degree of the polynomial.

    Returns:
    numpy.ndarray: Coefficients of the polynomial.
    """
    # Create the Vandermonde matrix
    X_vander = np.vander(x, degree + 1)
    
    # Solve the linear system to find the polynomial coefficients
    coeffs = np.linalg.lstsq(X_vander, y, rcond=None)[0]
    
    return coeffs

def read_input():
    """
    Read input for polynomial regression.

    Returns:
    int: Degree of the polynomial.
    numpy.ndarray: Input feature values.
    numpy.ndarray: Output target values.
    """
    degree = int(input())
    n_points = int(input())
    x = []
    y = []

    for _ in range(n_points):
        xi, yi = map(float, input().split())
        x.append(xi)
        y.append(yi)
    
    return degree, np.array(x), np.array(y)

# Read input
degree, x, y = read_input()

# Perform polynomial regression
coeffs = polynomial_regression_vandermonde(x, y, degree)

# Output coefficients
coeffs = np.round(coeffs, 2)
formatted_coeffs = " ".join(f"{num:.2f}" for num in coeffs)
print(formatted_coeffs)
