import numpy as np
import sympy as sym


def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0.0
    L = []

    for i in range(n):
        L_i = 1
        for j in range(n):
            if j != i:
                L_i *= (x_val - x[j]) / (x[i] - x[j])

        result += L_i * y[i]
        L.append(float(L_i))

    return float(result), L


def divided_differences(x, y):
    n = len(x)
    divided_diff = np.zeros((n, n), dtype=object)
    divided_diff[:, 0] = y

    N = []

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (
                divided_diff[i + 1][j - 1] - divided_diff[i][j - 1]
            ) / (x[i + j] - x[i])

    N.append(float(y[0]))

    for i in range(1, n):
        N.append(float(divided_diff[0, i]))

    return N


def main():
    # Read the function from input
    function_input = input()
    func = sym.sympify(function_input)

    # Read the x-points for interpolation, space-separated
    x_points_input = input()
    x_points = np.array(sym.sympify(x_points_input.split()))

    # Read the x-value for evaluation
    x_eval_input = input()
    x_eval = sym.sympify(x_eval_input)

    # Evaluate the function at the x-points
    y_points = [func.subs(sym.symbols("x"), xi) for xi in x_points]

    result, L = lagrange_interpolation(x_points, y_points, x_eval)
    N = divided_differences(x_points, y_points)

    for i in range(len(L)):
        L[i] = np.round(L[i], 3)

    print(" ".join(map(str, L)))

    for i in range(len(N)):
        N[i] = np.round(N[i], 3)

    print(" ".join(map(str, N)))

    print(np.round(result, 3))


if __name__ == "__main__":
    main()
