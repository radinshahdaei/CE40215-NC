import sympy as sp
import numpy as np
import math


def derivative(f, x, y, i, j):
    # Define symbols
    x_sym = sp.Symbol("x")
    y_sym = sp.Symbol("y")

    f_sym = sp.sympify(f)

    df_dx = f_sym.diff(x_sym, i)
    df_dy = df_dx.diff(y_sym, j)

    return float(df_dy.subs({'x': x, 'y': y}))


def binomial_expansion(n):
    coefficients = []

    for k in range(n + 1):
        coefficient = sp.binomial(n, k)
        power_a = n - k
        power_b = k
        coefficients.append((coefficient, power_a, power_b))

    return coefficients


def taylor(f, x, y, a, b, n):
    result = 0
    for i in range(0, n + 1):
        result_i = 1 / math.factorial(i)
        buffer = 0
        C_i = binomial_expansion(i)
        for _ in C_i:
            buffer += (
                _[0]
                * pow(x - a, _[1])
                * pow(y - b, _[2])
                * derivative(f, a, b, _[1], _[2])
            )
        result_i *= buffer
        result += result_i
    return result


def main():
    function_input = input()
    func = sp.sympify(function_input)

    input_str = input()
    a, b = map(float, input_str.split())
    input_str = input()
    x, y = map(float, input_str.split())
    n = int(input())

    taylor_num = float(taylor(func, x, y, a, b, n))
    real = float(func.subs({"x": x, "y": y}))

    print(np.round(taylor_num, 4))
    print(np.round(real, 4))


if __name__ == "__main__":
    main()
