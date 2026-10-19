
# Snake and Ladder Using BFS

## 1. Introduction

This mini-project implements the Snake and Ladder game using the Breadth-First Search (BFS) graph traversal algorithm in Python.

The game board contains 100 squares. Snakes move the player down to a lower square, while ladders move the player up to a higher square.

BFS is used to find the minimum number of dice rolls required to reach square 100 from square 1.

## 2. Objectives

- Understand graph representation.
- Learn the Breadth-First Search (BFS) algorithm.
- Find the shortest path in an unweighted graph.
- Understand how snakes and ladders affect movement.
- Calculate the minimum number of dice rolls required to win.

## 3. Description

The Snake and Ladder board is represented as a graph.

- Each square represents a vertex.
- Each possible dice roll represents an edge.
- Snakes move the player to a lower-numbered square.
- Ladders move the player to a higher-numbered square.
- BFS explores reachable positions level by level.

Each BFS level represents one additional dice roll. Therefore, BFS can find a path requiring the minimum number of rolls.

The program uses a predefined set of snakes and ladders and assumes that a player must land exactly on square 100 to win.

## 4. Technologies Used

- Programming Language: Python
- Algorithm: Breadth-First Search (BFS)
- Data Structure: Queue
- Additional Data Structure: Set for visited positions
- IDE: Visual Studio Code

## 5. Features

- Display the snakes and ladders on the board.
- Find the shortest path from square 1 to square 100.
- Calculate the minimum number of dice rolls.
- Apply snakes and ladders automatically.
- Prevent repeated processing of visited squares.
- Avoid moves beyond square 100.

## 6. Algorithm

1. Start at square 1.
2. Add the starting position to a queue.
3. Remove the front position from the queue.
4. Generate all possible dice rolls from 1 to 6.
5. Ignore moves beyond square 100.
6. Apply a snake or ladder if the destination has one.
7. If the resulting position is unvisited, mark it visited and add it to the queue.
8. Continue until square 100 is reached.
9. Display the path and minimum number of dice rolls.

## 7. How to Run

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Save the code as `snake_ladder.py`.
4. Open the terminal.
5. Execute the following command:

```bash
python snake_ladder.py
```

No external Python libraries are required.

## 8. Sample Output

```text
========== MENU ==========
1. Display Snakes and Ladders
2. Find Shortest Path using BFS
3. Exit

Enter your choice: 2

Shortest path found!
Path: (The program displays the calculated path)
Minimum dice rolls: (Calculated by BFS)
```

The exact path and number of rolls are calculated automatically by the program.

## 9. Time Complexity

Let V be the number of board positions and E be the number of possible transitions.

- Time Complexity: O(V + E)
- Space Complexity: O(V)

For a 100-square board with at most six outgoing dice-roll transitions per square, BFS is efficient.

## 10. Applications

- Shortest-path problems
- Board game simulations
- Graph traversal
- Route planning
- Artificial intelligence search algorithms

## 11. Conclusion

This mini-project demonstrates how BFS can be applied to the Snake and Ladder game to find the minimum number of dice rolls required to reach the final square.

It provides practical experience with queues, visited sets, graph modelling, and shortest-path algorithms.
