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

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure for Kruskal's algorithm.
    """

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

    def make_set(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0

def kruskal(graph):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST) of a graph.

    Parameters:
    graph: A list of edges in the form (weight, node1, node2).

    Returns:
    mst: A list of edges in the Minimum Spanning Tree.
    total_weight: The total weight of the Minimum Spanning Tree.
    """
    ds = DisjointSet()

    for weight, node1, node2 in graph:
        ds.make_set(node1)
        ds.make_set(node2)

    mst = []
    total_weight = 0

    # Sort edges by weight
    sorted_edges = sorted(graph)

    for weight, node1, node2 in sorted_edges:
        if ds.find(node1) != ds.find(node2):
            ds.union(node1, node2)
            mst.append((node1, node2, weight))
            total_weight += weight

    return mst, total_weight
