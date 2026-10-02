"""
AINL3001
Topic 4 Solution
BSP 2026

Local Search and Optimisation

Topics:
1. Cost Functions
2. Neighbour Generation
3. Hill Climbing
4. Local Maxima
5. Simulated Annealing
6. Optimisation vs Search

This solution demonstrates all tasks from the lab.
"""

import random
import math


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

N = 8


# --------------------------------------------------
# TASK 0
# MANUAL EXPLORATION
# --------------------------------------------------

print("=" * 60)
print("TASK 0 - MANUAL EXPLORATION")
print("=" * 60)

example_board = [0, 1, 2, 3]

print("\nBoard:")
print(example_board)

print(
    """
Interpretation:

Column 0 -> Row 0
Column 1 -> Row 1
Column 2 -> Row 2
Column 3 -> Row 3

All queens lie on the same diagonal.
"""
)


# --------------------------------------------------
# TASK 1
# CONFLICT FUNCTION
# --------------------------------------------------

def count_conflicts(board):
    """
    Counts attacking queen pairs.

    Lower is better.

    Perfect solution:
        0 conflicts
    """

    conflicts = 0

    for i in range(len(board)):

        for j in range(i + 1, len(board)):

            same_row = (
                board[i] == board[j]
            )

            same_diagonal = (
                abs(board[i] - board[j])
                ==
                abs(i - j)
            )

            if same_row or same_diagonal:
                conflicts += 1

    return conflicts


print("\nConflicts in Example Board:")
print(count_conflicts(example_board))


# --------------------------------------------------
# TASK 2
# GENERATE NEIGHBOURS
# --------------------------------------------------

def generate_neighbours(board):
    """
    Generates neighbouring solutions.

    A neighbour is created by
    moving one queen to another row.
    """

    neighbours = []

    for col in range(N):

        current_row = board[col]

        for row in range(N):

            if row != current_row:

                neighbour = board.copy()

                neighbour[col] = row

                neighbours.append(neighbour)

    return neighbours


# --------------------------------------------------
# BOARD DISPLAY
# EXTENSION 1
# --------------------------------------------------

def display_board(board):

    print()

    for row in range(N):

        line = []

        for col in range(N):

            if board[col] == row:
                line.append("Q")
            else:
                line.append(".")

        print(" ".join(line))

    print()


# --------------------------------------------------
# TASK 3
# HILL CLIMBING
# --------------------------------------------------

def hill_climbing(start_board):

    current = start_board

    while True:

        neighbours = generate_neighbours(
            current
        )

        best = min(
            neighbours,
            key=count_conflicts
        )

        current_score = count_conflicts(
            current
        )

        best_score = count_conflicts(
            best
        )

        if best_score >= current_score:
            return current

        current = best


# --------------------------------------------------
# TASK 4
# MULTIPLE HILL CLIMBING RUNS
# --------------------------------------------------

def run_hill_climbing_experiments():

    print("=" * 60)
    print("TASK 4 - HILL CLIMBING EXPERIMENTS")
    print("=" * 60)

    results = []

    for run in range(1, 6):

        start = [
            random.randint(
                0,
                N - 1
            )
            for _ in range(N)
        ]

        solution = hill_climbing(start)

        cost = count_conflicts(solution)

        results.append(cost)

        print(
            f"Attempt {run}: Final Cost = {cost}"
        )

    return results


# --------------------------------------------------
# TASK 5
# SIMULATED ANNEALING
# --------------------------------------------------

def simulated_annealing(
    start_board,
    temperature=100,
    cooling_rate=0.95
):

    current = start_board

    while temperature > 0.1:

        neighbours = generate_neighbours(
            current
        )

        candidate = random.choice(
            neighbours
        )

        current_cost = count_conflicts(
            current
        )

        candidate_cost = count_conflicts(
            candidate
        )

        delta = (
            candidate_cost
            -
            current_cost
        )

        if delta < 0:

            current = candidate

        else:

            probability = math.exp(
                -delta / temperature
            )

            if random.random() < probability:
                current = candidate

        temperature *= cooling_rate

    return current


# --------------------------------------------------
# EXTENSION 2
# RANDOM RESTART HILL CLIMBING
# --------------------------------------------------

def random_restart_hill_climbing(
    restarts=20
):

    best_solution = None
    best_cost = float("inf")

    for _ in range(restarts):

        board = [
            random.randint(
                0,
                N - 1
            )
            for _ in range(N)
        ]

        solution = hill_climbing(board)

        cost = count_conflicts(solution)

        if cost < best_cost:

            best_cost = cost

            best_solution = solution

    return best_solution


# --------------------------------------------------
# MAIN DEMONSTRATION
# --------------------------------------------------

if __name__ == "__main__":

    print("\nGenerating Random Board...")

    start_board = [
        random.randint(
            0,
            N - 1
        )
        for _ in range(N)
    ]

    print("\nStarting Board:")
    print(start_board)

    print(
        "\nStarting Conflicts:",
        count_conflicts(start_board)
    )

    display_board(start_board)

    # ---------------------------------
    # Neighbours
    # ---------------------------------

    neighbours = generate_neighbours(
        start_board
    )

    print(
        f"Generated {len(neighbours)} neighbours"
    )

    # ---------------------------------
    # Hill Climbing
    # ---------------------------------

    hill_solution = hill_climbing(
        start_board
    )

    print("\n" + "=" * 60)
    print("HILL CLIMBING")
    print("=" * 60)

    print(
        "Final Solution:"
    )

    print(hill_solution)

    print(
        "\nConflicts:",
        count_conflicts(hill_solution)
    )

    display_board(hill_solution)

    # ---------------------------------
    # Experiments
    # ---------------------------------

    run_hill_climbing_experiments()

    # ---------------------------------
    # Simulated Annealing
    # ---------------------------------

    anneal_solution = simulated_annealing(
        start_board
    )

    print("\n" + "=" * 60)
    print("SIMULATED ANNEALING")
    print("=" * 60)

    print(
        "Final Solution:"
    )

    print(anneal_solution)

    print(
        "\nConflicts:",
        count_conflicts(anneal_solution)
    )

    display_board(anneal_solution)

    # ---------------------------------
    # Comparison
    # ---------------------------------

    print("\n" + "=" * 60)
    print("COMPARISON")
    print("=" * 60)

    hill_cost = count_conflicts(
        hill_solution
    )

    anneal_cost = count_conflicts(
        anneal_solution
    )

    print(
        f"\nHill Climbing Cost: {hill_cost}"
    )

    print(
        f"Simulated Annealing Cost: {anneal_cost}"
    )

    if hill_cost < anneal_cost:

        print(
            "\nHill Climbing found the better solution."
        )

    elif anneal_cost < hill_cost:

        print(
            "\nSimulated Annealing found the better solution."
        )

    else:

        print(
            "\nBoth algorithms found solutions of equal quality."
        )

    # ---------------------------------
    # Random Restart Extension
    # ---------------------------------

    print("\n" + "=" * 60)
    print("RANDOM RESTART HILL CLIMBING")
    print("=" * 60)

    restart_solution = random_restart_hill_climbing()

    print(restart_solution)

    print(
        "\nConflicts:",
        count_conflicts(restart_solution)
    )

    display_board(restart_solution)

    print("\nFinished.")