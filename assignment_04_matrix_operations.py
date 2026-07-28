# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read matrix(rows, cols, matrix_name=""):
matrix = []
prefix = f"for {matrix_name} " if matrix_name else""
for i in range(rows):
    row_input= input(f"Enter {prefix}row{i+1}").split()
    row = [int(val) forr val in row input]
matrix.append(row)
return matrix


def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:4d}", end=" ")
            print()


            # PART A

            def transpose_matrix(matrix):
                rows = len(matrix)
                cols = len(matrix[0])
                transposed=[]
                for j in range(cols):
                    new_row = []
                    for i in range(rows):
                        new_row.append(matrix[i][j])
                        transposed.append(new_row)
                        return transposed

                    #PART B

                    def add_matrices(matrix_a, matrix_b):
                    rows = len(matrix_a)
                    cols = len(matrix_a[0])

                    result = []
                    for i in range(rows):
                        row = []
                        for j in range(cols):
                            row.append(matrix_a[i][j]+ matrix_b[i][j])

                            result.append(row)

                            return result


                        #Part C
                        def multiply_matrices(matrix_a, matrx_b):
                            rows_a = len(matrix_a)
                            cols_a = len(matrix_a[0])
                            cols_b = len(matrix_b[0])
                            cols_b = len(matrix_b[0])
                            result = []
                            for i in range(rows_a):
                                row = []
                                for j in range(cols_b):
                                    sum_product = 0
                                    for k in range(cols_a):
                                        sum_product += matrix_a[i][k] * matrix_b[k][j]
                                        row.append(sum_product)
                                        result.append(row)
                                        return result


                                    def main():
                                        # Part A
                                        print("Part A: Transpose a Matrix")
                                        rows = int(input("Enter number of rows: "))
                                        cols = int(input("Enter number of columns: "))
                                        matrix = read_matrix(rows, cols, "A")
                                        transposed = transpose_matrix(matrix)
                                        print("Original Matrix:")
                                        print_matrix(matrix)
                                        print("Transposed Matrix:")
                                        print_matrix(transposed)
                                        print("Part B: Add Two Matrices")
                                        rows = int(input("Enter number of rows: "))
                                        cols = int(input("Enter number of columns: "))
                                        matrix_a = read_matrix(rows, cols, "A")
                                        matrix_b = read_matrix(rows, cols, "B")
                                        result = add_matrices(matrix_a, matrix_b)
                                        print("Matrix A:")
                                        print_matrix(matrix_a)
                                        print("Matrix B:")
                                        print_matrix(matrix_b)
                                        print("Sum of Matrices:")
                                        print_matrix(result)
                                        print("Part C: Multiply Two Matrices")
                                        rows_a = int(input("Enter number of rows for Matrix A: "))
                                        cols_a = int(input("Enter number of columns for Matrix A: "))
                                        cols_b = int(input("Enter number of columns for Matrix B: "))
                                        matrix_a = read_matrix(rows_a, cols_a, "A")
                                        matrix_b = read_matrix(cols_a, cols_b, "B")
                                        result = multiply_matrices(matrix_a, matrix_b)
                                        print("Matrix A:")
                                        print_matrix(matrix_a)
                                        print("Matrix B:")
                                        print_matrix(matrix_b)
                                        print("Product of Matrices:")
                                        print_matrix(result)
                                        print("Program completed successfully.")
                                        if __name__ == "__main__":
                                            main()