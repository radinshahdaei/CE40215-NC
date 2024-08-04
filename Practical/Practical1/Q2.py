import math
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


def newton_interpolation(x, y, x_eval):
    N = divided_differences(x, y)
    n = len(x)
    result = y[0]
    for i in range(1, n):
        buffer = 1
        for j in range(i):
            buffer *= x_eval - x[j]
        result += N[i] * buffer
    return float(result)


def create_uniform(a, b, n):
    return [float(a + (b - a) * (i / (n - 1))) for i in range(n)]


def create_chebyshev(a, b, n):
    return [
        0.5 * (a + b) + 0.5 * (b - a) * math.cos((2 * i + 1) * math.pi / (2 * n))
        for i in range(n)
    ]


def main():
    function_input = input()
    func = sym.sympify(function_input)

    input_str = input()
    a, b = map(float, input_str.split())
    x_eval = float(input())
    n = int(input())

    U = create_uniform(a, b, n)
    C = create_chebyshev(a, b, n)

    U_y = [func.subs(sym.symbols("x"), xi) for xi in U]
    C_y = [func.subs(sym.symbols("x"), xi) for xi in C]

    U_res = newton_interpolation(U, U_y, x_eval)
    C_res = newton_interpolation(C, C_y, x_eval)
    print(np.round(C_res, 3))
    print(np.round(U_res, 3))
    print(np.round(abs(U_res - C_res), 3))


if __name__ == "__main__":
    main()
