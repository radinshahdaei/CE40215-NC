import numpy as np

def cramer_rule(A, B):
    """
    Solve the system of linear equations Ax = B using Cramer's rule.

    Parameters:
    A (numpy.ndarray): Coefficient matrix.
    B (numpy.ndarray): Constant matrix.

    Returns:
    numpy.ndarray: Solution for the system of equations.
    """
    det_A = np.linalg.det(A)
    if det_A == 0:
        raise ValueError("The coefficient matrix A is singular and the system does not have a unique solution.")
    
    n = A.shape[0]
    x = np.zeros(n)
    
    for i in range(n):
        Ai = np.copy(A)
        Ai[:, i] = B
        x[i] = np.linalg.det(Ai) / det_A
    
    return x

def read_augmented_matrix():
    """
    Read the augmented matrix from user input.

    Returns:
    numpy.ndarray: Coefficient matrix A.
    numpy.ndarray: Constant matrix B.
    """
    n = int(input())
    augmented_matrix = []

    for _ in range(n):
        row = list(map(float, input().split()))
        augmented_matrix.append(row)

    augmented_matrix = np.array(augmented_matrix)
    A = augmented_matrix[:, :-1]
    B = augmented_matrix[:, -1]
    
    return A, B

# Example usage
A, B = read_augmented_matrix()

try:
    solution = cramer_rule(A, B)
    rounded_solution = np.round(solution, 2)
    formatted_solution = " ".join(f"{num:.2f}" for num in rounded_solution)
    print(formatted_solution)
except ValueError as e:
    print(e)
