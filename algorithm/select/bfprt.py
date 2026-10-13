def median_of_medians(arr, low, high):
    n = high - low + 1
    if n < 5:
        return sorted(arr[low:high + 1])[n // 2]

    medians = []
    for i in range(low, high + 1, 5):
        sub_high = min(i + 4, high)
        median = sorted(arr[i:sub_high + 1])[(sub_high - i) // 2]
        medians.append(median)

    return median_of_medians(medians, 0, len(medians) - 1)

def partition(arr, low, high, pivot_value):
    pivot_index = low
    while pivot_index <= high and arr[pivot_index] != pivot_value:
        pivot_index += 1
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def bfprt_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_value = median_of_medians(arr, low, high)
    pivot_index = partition(arr, low, high, pivot_value)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return bfprt_select(arr, low, pivot_index - 1, k)
    else:
        return bfprt_select(arr, pivot_index + 1, high, k)
