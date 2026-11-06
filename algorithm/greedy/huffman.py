def huffman_coding(frequencies):
    """
    Generate Huffman codes for given character frequencies.

    :param frequencies: A dictionary where keys are characters and values are their frequencies.
    :return: A dictionary mapping characters to their corresponding Huffman codes.
    """
    import heapq

    # Create a priority queue (min-heap) from the frequencies
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)
        for pair in low1[1:]:
            pair[1] = '0' + pair[1]
        for pair in low2[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low1[0] + low2[0]] + low1[1:] + low2[1:])

    # Extract the codes from the heap
    huffman_codes = {}
    for char, code in heap[0][1:]:
        huffman_codes[char] = code

    return huffman_codes
