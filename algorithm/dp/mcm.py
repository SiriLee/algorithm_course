def matrix_chain_order(p):
    """
    Given a list of dimensions p, where the i-th matrix has dimensions p[i-1] x p[i],
    this function computes the minimum number of scalar multiplications needed to multiply
    the chain of matrices and returns the dp table and the s table for optimal parenthesization.
    :param p: List of dimensions of matrices.
    :return: A tuple (dp, s) where dp[i][j] is the minimum number of multiplications needed to compute the product of matrices A_i through A_j,
             and s[i][j] is the index of the matrix after which the product is split in an optimal parenthesization.
    """
    n = len(p) - 1

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                # Calculate the cost of multiplying matrices A_i to A_k and A_(k+1) to A_j
                q = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k

    return dp, s

def print_optimal_parens(s, i, j):
    """
    Print the optimal parenthesization of the matrix chain product.
    :param s: The s table from matrix_chain_order function.
    :param i: Starting index of the matrix chain.
    :param j: Ending index of the matrix chain.
    """
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

if __name__ == "__main__":
    # Example usage
    dimensions = [30, 35, 15, 5, 10, 20, 25]
    dp_table, s_table = matrix_chain_order(dimensions)
    print(f"Minimum number of multiplications: {dp_table[1][len(dimensions) - 1]}")
    print("Optimal parenthesization: ", end="")
    print_optimal_parens(s_table, 1, len(dimensions) - 1)
    print()
