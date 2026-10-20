def longest_increasing_subsequence(sequence):
    """
    Find a longest strictly increasing subsequence using dynamic programming.

    :param sequence: A sequence of comparable values.
    :return: A tuple containing the length and one longest increasing subsequence.
    """
    n = len(sequence)
    if n == 0:
        return 0, []

    lengths = [1] * n
    predecessors = [-1] * n

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                predecessors[i] = j

    end = max(range(n), key=lengths.__getitem__)
    longest_length = lengths[end]
    subsequence = []
    while end != -1:
        subsequence.append(sequence[end])
        end = predecessors[end]
    subsequence.reverse()

    return longest_length, subsequence


if __name__ == "__main__":
    numbers = [10, 22, 9, 33, 21, 50, 41, 60]
    length, subsequence = longest_increasing_subsequence(numbers)
    print(f"The length of the longest increasing subsequence is: {length}")
    print(f"The subsequence is: {subsequence}")
