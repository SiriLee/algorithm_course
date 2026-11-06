def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding the shortest path in a graph.

    :param graph: A dictionary representing the graph where keys are node identifiers
                  and values are dictionaries of neighboring nodes and their edge weights.
    :param start: The starting node identifier.
    :return: A dictionary containing the shortest distance from the start node to each node.
    """
    import heapq

    # Initialize distances with infinity and set the distance to the start node to 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to hold nodes to explore
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the distance is greater than the recorded distance, skip processing
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
