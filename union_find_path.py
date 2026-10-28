def valid_path(n, edges, source, destination):
    """Return reachability and a dry run of Union-Find edge processing."""
    parent = list(range(n))
    rank = [0] * n
    dry_run = []

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(first, second):
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return False

        if rank[first_root] < rank[second_root]:
            parent[first_root] = second_root
        elif rank[first_root] > rank[second_root]:
            parent[second_root] = first_root
        else:
            parent[second_root] = first_root
            rank[first_root] += 1
        return True

    for first, second in edges:
        merged = union(first, second)
        status = "merged components" if merged else "already connected"
        dry_run.append(f"union({first}, {second}): {status}")

    return find(source) == find(destination), dry_run


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
        found, dry_run = valid_path(n, edges, source, destination)
        print(f"Union-Find result: {'Path exists' if found else 'No path'}")
        print("Union-Find dry run:")
        for operation in dry_run:
            print(f"  {operation}")
    except ValueError as error:
        print(f"Invalid input: {error}")