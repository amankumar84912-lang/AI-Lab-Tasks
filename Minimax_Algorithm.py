def minimax(depth, node, maximizing_player, values):

    if depth == 3:
        return values[node]

    if maximizing_player:
        best = float('-inf')

        for i in range(2):
            value = minimax(
                depth + 1,
                node * 2 + i,
                False,
                values
            )
            best = max(best, value)

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = minimax(
                depth + 1,
                node * 2 + i,
                True,
                values
            )
            best = min(best, value)

        return best


values = [3, 5, 2, 9, 12, 5, 23, 23]

result = minimax(0, 0, True, values)

print("Optimal value using Minimax:", result)