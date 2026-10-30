def coins_amount(coins, amount):
    """
    Calculate the way using the least number of coins to make change for a given amount.

    :param coins: List of coin denominations (integers).
    :param amount: The target amount to make change for (integer).
    :return: The minimum number of coins. If it's not possible to make change, return -1.`
    """
    n = len(coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make change for amount 0
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 10, 25]
    amount = 30
    print(f"Minimum number of coins to make change for {amount}: {coins_amount(coins, amount)}")
