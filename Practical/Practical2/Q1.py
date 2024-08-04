from sympy import symbols, diff, degree


def lagrange_polynomial(x, y, xi):
    n = len(x)
    result = 0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        result += term

    return result


# Input xi and yi
n = int(input())
xi_input = input().split()
yi_input = input().split()
x = [float(xi_input[i]) for i in range(0, n)]
y = [float(yi_input[i]) for i in range(0, n)]

# Define the symbol
xi = symbols("xi")

# Get the Lagrange polynomial
L = lagrange_polynomial(x, y, xi)

degree = 0

for i in range(len(x)):
    counter = 0
    L = diff(L, xi)
    for x_i in x:
        if abs(L.subs("xi", x_i)) < 1e-6:
            counter = counter + 1
    if counter == len(x):
        break
    degree = degree + 1

print(degree)
