from collections import deque


def build_adjacency_list(n, edges):
    """Build an adjacency list for an undirected graph."""
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    return adjacency


def valid_path(n, edges, source, destination):
    """Return True when destination is reachable from source using BFS."""
    adjacency = build_adjacency_list(n, edges)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)
        if node == destination:
            return True, traversal

        for neighbour in adjacency[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)

    return False, traversal


def read_graph_input():
    n = int(input("Number of nodes: "))
    edge_count = int(input("Number of edges: "))
    if n <= 0 or edge_count < 0:
        raise ValueError("Node count must be positive and edge count cannot be negative.")

    edges = []
    for index in range(edge_count):
        values = input(f"Edge {index + 1} (u v): ").split()
        if len(values) != 2:
            raise ValueError("Each edge must contain exactly two node numbers.")
        u, v = map(int, values)
        if not (0 <= u < n and 0 <= v < n):
            raise ValueError(f"Edge endpoints must be between 0 and {n - 1}.")
        edges.append((u, v))

    source = int(input("Source node: "))
    destination = int(input("Destination node: "))
    if not (0 <= source < n and 0 <= destination < n):
        raise ValueError(f"Source and destination must be between 0 and {n - 1}.")
    return n, edges, source, destination


if __name__ == "__main__":
    try:
        n, edges, source, destination = read_graph_input()
        found, traversal = valid_path(n, edges, source, destination)
        print(f"BFS result: {'Path exists' if found else 'No path'}")
        print(f"BFS traversal: {traversal}")
    except ValueError as error:
        print(f"Invalid input: {error}")
