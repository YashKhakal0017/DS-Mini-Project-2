
# Mini Project: Snake and Ladder using BFS
from collections import deque

BOARD_SIZE = 100

# Snakes: key = head, value = tail
SNAKES = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

# Ladders: key = bottom, value = top
LADDERS = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}


def get_next_position(position):
    """Apply a snake or ladder if the position has one."""
    if position in SNAKES:
        return SNAKES[position]
    if position in LADDERS:
        return LADDERS[position]
    return position


def find_shortest_path():
    """Use BFS to find the minimum number of dice rolls."""
    queue = deque([(1, 0, [1])])
    visited = {1}

    while queue:
        position, rolls, path = queue.popleft()

        if position == BOARD_SIZE:
            return rolls, path

        for dice in range(1, 7):
            next_position = position + dice

            # Do not move beyond square 100
            if next_position > BOARD_SIZE:
                continue

            # Apply snake or ladder
            next_position = get_next_position(next_position)

            if next_position not in visited:
                visited.add(next_position)
                queue.append(
                    (next_position, rolls + 1, path + [next_position])
                )

    return -1, []


def display_board_info():
    print("\n========== SNAKE AND LADDER ==========")
    print("Board size:", BOARD_SIZE)
    print("Starting position: 1")
    print("Winning position:", BOARD_SIZE)

    print("\nSnakes:")
    for head, tail in sorted(SNAKES.items()):
        print(f"{head} -> {tail}")

    print("\nLadders:")
    for bottom, top in sorted(LADDERS.items()):
        print(f"{bottom} -> {top}")


def main():
    while True:
        print("\n========== MENU ==========")
        print("1. Display Snakes and Ladders")
        print("2. Find Shortest Path using BFS")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_board_info()

        elif choice == "2":
            rolls, path = find_shortest_path()

            if rolls == -1:
                print("No path to the winning position exists.")
            else:
                print("\nShortest path found!")
                print("Path:", " -> ".join(map(str, path)))
                print("Minimum dice rolls:", rolls)

        elif choice == "3":
            print("Thank you for using Snake and Ladder!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
