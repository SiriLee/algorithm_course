def min_max(arr):
    min_value = arr[0]
    max_value = arr[0]
    # Read two elements (if available) at a time to reduce the number of comparisons
    for i in range(1, len(arr) - 1, 2):
        if arr[i] < arr[i + 1]:
            min_value = min(min_value, arr[i])
            max_value = max(max_value, arr[i + 1])
        else:
            min_value = min(min_value, arr[i + 1])
            max_value = max(max_value, arr[i])
    # If there's an odd number of elements, compare the last element separately
    if len(arr) % 2 == 1:
        min_value = min(min_value, arr[-1])
        max_value = max(max_value, arr[-1])
    return (min_value, max_value)
