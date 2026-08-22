state_space = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

print("State Space Representation:\n")

for state, children in state_space.items():
    print(f"{state} --> {children}")