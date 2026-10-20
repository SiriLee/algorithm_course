def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    Returns the maximum value that can be obtained with the given weights and values.
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]

def knapsack_unbounded(weights, values, capacity):
    """
    Solves the Unbounded Knapsack problem using dynamic programming.
    Returns the maximum value that can be obtained with the given weights and values.
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(weights[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return dp[capacity]

def knapsack_01_boolean(weights, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.
    Returns True if a subset of the weights can sum up to the capacity, False otherwise.
    """
    dp = [False] * (capacity + 1)
    dp[0] = True
    for w in weights:
        for j in range(capacity, w - 1, -1):
            dp[j] = dp[j] or dp[j - w]
    return dp[capacity]
