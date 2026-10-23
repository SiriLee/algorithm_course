def optimal_bst(keys, freq):
    n = len(keys)
    # Create a table to store the cost of optimal BST
    cost = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the diagonal with frequencies (base case)
    for i in range(n):
        cost[i][i] = freq[i]

    # l is the chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            cost[i][j] = float('inf')

            # Try making each key in keys[i..j] the root
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + (cost[r + 1][j] if r < j else 0) + sum(freq[i:j + 1])
                if c < cost[i][j]:
                    cost[i][j] = c
    return cost[0][n - 1]
