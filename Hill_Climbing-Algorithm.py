def hill_climbing(start):
    current = start

    while True:
        current_value = -(current - 3) ** 2 + 9

        neighbors = [current - 1, current + 1]

        best = max(
            neighbors,
            key=lambda x: -(x - 3) ** 2 + 9
        )

        best_value = -(best - 3) ** 2 + 9

        print("Current:", current,
              "Value:", current_value)

        if best_value <= current_value:
            break

        current = best

    print("\nMaximum value:", current_value)
    print("Optimal state:", current)


hill_climbing(0)