"""
AINL3001 — Knowledge-Driven AI
Week 4 — Local Search and Optimisation
BSP 2026

This solution demonstrates the tasks from the Week 4 lab.

Topics
------

1. Understanding the N-Queens state representation
2. Cost functions
3. Neighbour generation
4. Hill Climbing
5. Local minima and plateaus
6. Simulated Annealing
7. Comparing local search approaches

The solution uses the QueensProblem class and the common
Problem interface introduced this week.
"""

import math
import random

from queens_problem import QueensProblem

N = 8


# --------------------------------------------------
# TASK 0 — UNDERSTANDING THE STATE
# --------------------------------------------------

example_board = [0, 1, 2, 3]

print("Manual Exploration Board:")
print(example_board)

print(
    "\nEach list position represents a column."
)

print(
    "Each value represents the row containing the queen."
)

print(
    "\nQuestion: How many conflicts exist on this board?"
)


# --------------------------------------------------
# TASK 1 — EVALUATE A STATE
# --------------------------------------------------

def count_conflicts(board):
    """
    Return the number of pairs of queens
    that attack each other.

    Lower values are better.

    A solution has:

        conflict count = 0
    """

    conflicts = 0

    # Compare each queen with every queen
    # that comes after it.
    #
    # i and j represent columns.
    # board[i] and board[j] represent rows.

    for i in range(len(board)):

        for j in range(i + 1, len(board)):

            # Queens attack each other if
            # they are in the same row.

            same_row = (
                board[i] == board[j]
            )

            # Queens attack each other diagonally
            # when the difference between their
            # rows equals the difference between
            # their columns.

            same_diagonal = (
                abs(board[i] - board[j])
                ==
                abs(i - j)
            )

            if same_row or same_diagonal:
                conflicts += 1

    return conflicts


print("\nConflicts in Manual Exploration Board:")
print(count_conflicts(example_board))


# --------------------------------------------------
# TASK 2 — EXPLORE THE PROBLEM
# --------------------------------------------------

def generate_neighbours(problem, board):
    """
    Generate all neighbouring boards.

    Use the Problem interface introduced this week:

        problem.actions(state)
        problem.result(state, action)
    """

    neighbours = []

    # Ask the problem which actions are
    # possible from the current state.

    actions = problem.actions(board)

    # Apply each action to create a
    # neighbouring state.

    for action in actions:

        neighbour = problem.result(
            board,
            action
        )

        neighbours.append(neighbour)

    return neighbours


# --------------------------------------------------
# TASK 3 — HILL CLIMBING
# --------------------------------------------------

def hill_climbing(problem, start_board):
    """
    Use Hill Climbing to reduce the number
    of conflicts.

    Algorithm:

        current = start state

        repeat:

            generate neighbours

            find the neighbour with the
            lowest conflict count

            if the neighbour is not better:
                stop

            otherwise:
                move to the neighbour

        return current
    """

    current = start_board

    while True:

        neighbours = generate_neighbours(
            problem,
            current
        )

        # Find the neighbour with the
        # lowest conflict count.

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

        # Stop if the best neighbour is
        # not better than the current state.
        #
        # This may mean we have reached a
        # solution, a local minimum, or
        # a plateau.

        if best_score >= current_score:
            return current

        current = best


# --------------------------------------------------
# TASK 4 — HILL CLIMBING EXPERIMENT
# --------------------------------------------------

def run_hill_climbing_experiments():
    """
    Run Hill Climbing five times from
    different random starting boards.

    This demonstrates that Hill Climbing
    does not always reach the same result.
    """

    print("\n" + "=" * 60)
    print("HILL CLIMBING EXPERIMENTS")
    print("=" * 60)

    results = []

    for run in range(1, 6):

        start = [
            random.randint(0, N - 1)
            for _ in range(N)
        ]

        problem = QueensProblem(start)

        solution = hill_climbing(
            problem,
            start
        )

        cost = count_conflicts(
            solution
        )

        results.append(cost)

        print(
            f"Attempt {run}: "
            f"Start = {start}, "
            f"Final Cost = {cost}"
        )

    return results


# --------------------------------------------------
# TASK 5 — SIMULATED ANNEALING
# --------------------------------------------------

def simulated_annealing(problem, start_board):
    """
    Use Simulated Annealing to search for
    a solution.

    Unlike Hill Climbing, Simulated Annealing
    can sometimes accept a worse state.

    This can help escape local minima.
    """

    current = start_board

    temperature = 10.0
    cooling_rate = 0.95

    while temperature > 0.1:

        # If we already have a perfect solution,
        # there is no reason to continue.

        if count_conflicts(current) == 0:
            return current

        neighbours = generate_neighbours(
            problem,
            current
        )

        # Simulated Annealing selects one
        # random neighbour rather than always
        # selecting the best neighbour.

        candidate = random.choice(
            neighbours
        )

        current_cost = count_conflicts(
            current
        )

        candidate_cost = count_conflicts(
            candidate
        )

        # A negative delta means that the
        # candidate is better.

        delta = (
            candidate_cost
            -
            current_cost
        )

        if delta < 0:

            # Always accept a better state.

            current = candidate

        else:

            # Sometimes accept a worse state.
            #
            # At high temperatures this is
            # more likely.
            #
            # As the temperature decreases,
            # worse moves become less likely.

            probability = math.exp(
                -delta / temperature
            )

            if random.random() < probability:
                current = candidate

        # Cool the system.

        temperature *= cooling_rate

    return current


# --------------------------------------------------
# EXTENSION 1 — DISPLAY THE BOARD
# --------------------------------------------------

def display_board(board):
    """
    Display an N-Queens board using:

        Q = queen
        . = empty square
    """

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
# EXTENSION 2 — RANDOM RESTART HILL CLIMBING
# --------------------------------------------------

def random_restart_hill_climbing(restarts=20):
    """
    Run Hill Climbing several times using
    different random starting states.

    Return the best solution found.
    """

    best_solution = None
    best_cost = float("inf")

    for _ in range(restarts):

        board = [
            random.randint(0, N - 1)
            for _ in range(N)
        ]

        problem = QueensProblem(board)

        solution = hill_climbing(
            problem,
            board
        )

        cost = count_conflicts(
            solution
        )

        if cost < best_cost:

            best_cost = cost
            best_solution = solution

        # We cannot improve on zero conflicts.

        if best_cost == 0:
            break

    return best_solution


# --------------------------------------------------
# MAIN DEMONSTRATION
# --------------------------------------------------

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("WEEK 4 — LOCAL SEARCH AND OPTIMISATION")
    print("=" * 60)

    # ----------------------------------------------
    # Create a random starting board
    # ----------------------------------------------

    board = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    problem = QueensProblem(board)

    print("\nRandom Board")
    print(board)

    print("\nConflicts")
    print(
        count_conflicts(board)
    )

    display_board(board)

    # ----------------------------------------------
    # Explore the Problem representation
    # ----------------------------------------------

    print("\n" + "=" * 60)
    print("PROBLEM REPRESENTATION")
    print("=" * 60)

    actions = problem.actions(board)

    print(
        f"\n{len(actions)} actions available"
    )

    print(
        "Example action:",
        actions[0]
    )

    example_result = problem.result(
        board,
        actions[0]
    )

    print(
        "Result of example action:",
        example_result
    )

    # ----------------------------------------------
    # Generate neighbours
    # ----------------------------------------------

    neighbours = generate_neighbours(
        problem,
        board
    )

    print(
        f"\n{len(neighbours)} neighbours generated"
    )

    # For N = 8 we expect:
    #
    # 8 queens × 7 alternative rows
    # = 56 neighbours

    # ----------------------------------------------
    # Hill Climbing
    # ----------------------------------------------

    hill_solution = hill_climbing(
        problem,
        board
    )

    print("\n" + "=" * 60)
    print("HILL CLIMBING")
    print("=" * 60)

    print("\nStarting Board:")
    print(board)

    print(
        "Starting Conflicts:",
        count_conflicts(board)
    )

    print("\nFinal Board:")
    print(hill_solution)

    hill_cost = count_conflicts(
        hill_solution
    )

    print(
        "Final Conflicts:",
        hill_cost
    )

    display_board(hill_solution)

    if hill_cost == 0:
        print(
            "Hill Climbing found a solution."
        )
    else:
        print(
            "Hill Climbing stopped before "
            "reaching a solution."
        )

    # ----------------------------------------------
    # Five Hill Climbing runs
    # ----------------------------------------------

    run_hill_climbing_experiments()

    # ----------------------------------------------
    # Simulated Annealing
    # ----------------------------------------------

    anneal_solution = simulated_annealing(
        problem,
        board
    )

    print("\n" + "=" * 60)
    print("SIMULATED ANNEALING")
    print("=" * 60)

    print("\nStarting Board:")
    print(board)

    print(
        "Starting Conflicts:",
        count_conflicts(board)
    )

    print("\nFinal Board:")
    print(anneal_solution)

    anneal_cost = count_conflicts(
        anneal_solution
    )

    print(
        "Final Conflicts:",
        anneal_cost
    )

    display_board(anneal_solution)

    if anneal_cost == 0:
        print(
            "Simulated Annealing found a solution."
        )
    else:
        print(
            "Simulated Annealing stopped before "
            "reaching a solution."
        )

    # ----------------------------------------------
    # Compare the algorithms
    # ----------------------------------------------

    print("\n" + "=" * 60)
    print("COMPARISON")
    print("=" * 60)

    print(
        f"\nHill Climbing Cost: {hill_cost}"
    )

    print(
        f"Simulated Annealing Cost: {anneal_cost}"
    )

    if hill_cost < anneal_cost:

        print(
            "\nFor this run, Hill Climbing "
            "produced the lower-cost state."
        )

    elif anneal_cost < hill_cost:

        print(
            "\nFor this run, Simulated Annealing "
            "produced the lower-cost state."
        )

    else:

        print(
            "\nFor this run, both algorithms "
            "produced states with the same cost."
        )

    # ----------------------------------------------
    # Random Restart Extension
    # ----------------------------------------------

    print("\n" + "=" * 60)
    print("RANDOM RESTART HILL CLIMBING")
    print("=" * 60)

    restart_solution = (
        random_restart_hill_climbing()
    )

    print("\nBest Board:")
    print(restart_solution)

    print(
        "Conflicts:",
        count_conflicts(restart_solution)
    )

    display_board(restart_solution)

    print("\nFinished.")
