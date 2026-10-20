def cut_rod(prices, n):
    """
    Function to determine the maximum revenue obtainable by cutting up a rod of length n and selling the pieces.

    :param prices: List of prices where prices[i] is the price of a rod of length i+1.
    :param n: Length of the rod.
    :return: Maximum revenue obtainable.
    """
    # Create a list to store the maximum revenue for each length
    max_revenue = [0] * (n + 1)

    # Build the max_revenue list in a bottom-up manner
    for i in range(1, n + 1):
        max_rev = float('-inf')
        for j in range(i):
            max_rev = max(max_rev, prices[j] + max_revenue[i - j - 1])
        max_revenue[i] = max_rev

    return max_revenue[n]
