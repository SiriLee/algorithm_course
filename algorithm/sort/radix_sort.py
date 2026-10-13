def radix_sort(arr, max_digits):
    for digit in range(max_digits):
        # Use a stable sort to sort the array on digit
        buckets = [[] for _ in range(10)]
        for num in arr:
            digit_value = (num // (10 ** digit)) % 10
            buckets[digit_value].append(num)
        arr = [num for bucket in buckets for num in bucket]
    
    return arr
