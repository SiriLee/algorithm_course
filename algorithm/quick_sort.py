def partition(arr, low, high):
    pivot = arr[high]  # Choose the rightmost element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap if element is smaller than or equal to pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot in the correct position
    return i + 1  # Return the index of the pivot

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Partition the array
        quick_sort(arr, low, pi - 1)  # Recursively sort elements before partition
        quick_sort(arr, pi + 1, high)  # Recursively sort elements after partition