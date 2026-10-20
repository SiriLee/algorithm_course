def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    # 01 Knapsack problem: Determine if a subset of nums can sum up to target
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]

if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(canPartition(nums))  # Output: True

    nums = [1, 2, 3, 5]
    print(canPartition(nums))  # Output: False
