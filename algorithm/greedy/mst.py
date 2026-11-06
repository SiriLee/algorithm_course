def prim(graph, start):
    """
    Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    Parameters:
    graph: A dictionary where keys are node identifiers and values are lists of tuples
           representing adjacent nodes and their edge weights.
    start: The starting node for Prim's algorithm.

    Returns:
    mst: A list of edges in the Minimum Spanning Tree.
    total_weight: The total weight of the Minimum Spanning Tree.
    """
    import heapq

    mst = []
    total_weight = 0
    visited = set()
    min_heap = [(0, start, None)]  # (weight, current_node, previous_node)

    while min_heap:
        weight, current_node, previous_node = heapq.heappop(min_heap)

        if current_node in visited:
            continue

        visited.add(current_node)
        if previous_node is not None:
            mst.append((previous_node, current_node, weight))
            total_weight += weight

        for neighbor, edge_weight in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst, total_weight

def kruskal(graph):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    Parameters:
    graph: A list of edges in the form (weight, node1, node2).

    Returns:
    mst: A list of edges in the Minimum Spanning Tree.
    total_weight: The total weight of the Minimum Spanning Tree.
    """
    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    # Initialize disjoint sets
    for weight, node1, node2 in graph:
        parent[node1] = node1
        parent[node2] = node2
        rank[node1] = 0
        rank[node2] = 0

    mst = []
    total_weight = 0

    # Sort edges by weight
    sorted_edges = sorted(graph)

    for weight, node1, node2 in sorted_edges:
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append((node1, node2, weight))
            total_weight += weight

    return mst, total_weight
