import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

h = {
    'A': 10,
    'B': 6,
    'C': 4,
    'D': 7,
    'E': 2,
    'F': 3,
    'G': 0
}

def best_first_search(start, goal):
    pq = [(h[start], start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        print("Visiting:", node)

        if node == goal:
            print("Goal Reached!")
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq, (h[neighbor], neighbor, path + [neighbor])
                )

    print("Goal not found.")


best_first_search('A', 'G')