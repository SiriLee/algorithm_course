def getMaxSubArray(arr):
    if not arr:
        return (-1, -1, 0)

    max_current = max_global = arr[0]
    left = right = 0
    best_left = best_right = 0

    for i in range(1, len(arr)):
        if max_current < 0:
            max_current = arr[i]
            left = right = i
        else:
            max_current += arr[i]
            right = i
        if max_current > max_global:
            max_global = max_current
            best_left = left
            best_right = right

    return (best_left, best_right, max_global)

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(getMaxSubArray(arr))

