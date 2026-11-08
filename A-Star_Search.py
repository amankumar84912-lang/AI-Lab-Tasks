import heapq

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 4, 'D': 1, 'E': 3},
    'D': {'B': 5, 'C': 1, 'F': 2},
    'E': {'C': 3, 'F': 2},
    'F': {'D': 2, 'E': 2, 'G': 2},
    'G': {'F': 2}
}

h = {
    'A': 10,
    'B': 8,
    'C': 7,
    'D': 5,
    'E': 3,
    'F': 2,
    'G': 0
}


def a_star(start, goal):

    open_list = [(h[start], 0, start, [start])]

    g_cost = {start: 0}

    while open_list:

        f, current_g, current, path = heapq.heappop(open_list)

        print(
            "Visiting:", current,
            "g =", current_g,
            "h =", h[current],
            "f =", f
        )

        if current == goal:
            print("\nGoal Reached!")
            print("Optimal Path:", " -> ".join(path))
            print("Total Cost:", current_g)
            return

        for neighbor, cost in graph[current].items():

            new_g = current_g + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:

                g_cost[neighbor] = new_g

                f_cost = new_g + h[neighbor]

                heapq.heappush(
                    open_list,
                    (f_cost, new_g, neighbor, path + [neighbor])
                )

    print("Goal not reachable.")

a_star('A', 'G')