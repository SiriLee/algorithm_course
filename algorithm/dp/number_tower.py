def max_path_sum(tower):
    """
    Calculate the maximum path sum in a number tower.

    :param tower: List of lists representing the number tower.
    :return: Maximum path sum from top to bottom.
    """
    n = len(tower)

    dp = [row[:] for row in tower]  # Create a copy of the tower to store maximum path sums

    # Start from the second last row and move upwards
    for i in range(n - 2, -1, -1):
        for j in range(len(tower[i])):
            # Update the current cell with the maximum path sum
            dp[i][j] = tower[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])

    path = [tower[0][0]]
    j = 0
    for i in range(1, n):
        if dp[i][j] >= dp[i][j + 1]:
            path.append(tower[i][j])
        else:
            j += 1
            path.append(tower[i][j])

    # Return the maximum path sum and the path taken
    return dp[0], path

if __name__ == "__main__":
    # Example usage
    number_tower = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    result, path = max_path_sum(number_tower)
    print(f"The maximum path sum is: {result}")
    print(f"The path taken is: {path}")
