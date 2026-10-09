# Week 5 Constraint Satisfaction Problems (CSPs)

**AINL3001 Knowledge-Driven AI**  
TU850 BSc in Data Science and Artificial Intelligence  
BSP 2026

## Learning objectives

By the end of this lab, you should be able to:

- Explain what a Constraint Satisfaction Problem (CSP) is.
- Identify the variables, domains and constraints of a CSP.
- Represent a CSP using Python.
- Implement constraint checking for partial assignments.
- Implement recursive backtracking search.
- Explain why backtracking can be more efficient than brute force.
- Implement the Minimum Remaining Values (MRV) heuristic.
- Describe how CSPs can be applied to scheduling and timetabling problems.

## 1. Background

In Week 4, we explored local search, where we tried to improve a candidate solution.

This week, we investigate a different type of problem: a **Constraint Satisfaction Problem (CSP)**.

Rather than searching for a solution with the lowest cost, our goal is to find an assignment that satisfies all the given constraints.

Examples of CSPs include:

- Timetabling and scheduling,
- Sudoku,
- Map colouring,
- Resource allocation,
- Exam scheduling.

A CSP has three main components:

| Component | Meaning | Example |
|---|---|---|
| Variables | Things we need to assign values to | Australian regions |
| Domains | Possible values for each variable | Red, Green, Blue |
| Constraints | Rules that assignments must satisfy | Neighbouring regions must have different colours |

Review the Week 5 lecture notes before starting the exercises.

This lab needs to be demoed. The demo is worth 2% of your module mark.

## 2. Getting started

Open your fork of the AINL3001 GitHub repository in VS Code.

If you have not already done so, follow the setup instructions in the [main repository README](../README.md), including setting up your Python virtual environment.

If you are continuing work from an earlier week, make sure your fork has the latest changes from the lecturer repository:

```bash
git fetch upstream
git merge upstream/main
git push origin main
```

Open the folder:

```text
week05_csp/
├── README.md
└── csp_starter.py
```

The solution file, `csp_solution.py`, will be released later.

Open `csp_starter.py` and run Python file in VS Code.

You can run the file before completing the TODO sections. Some results will initially show `None` because the functions have not yet been implemented.

Complete the exercises in order and rerun the file after each task.

## 3. The map-colouring problem

We will solve a simplified Australian map-colouring problem.

The six regions are:

| Abbreviation | Region |
|---|---|
| WA | Western Australia |
| NT | Northern Territory |
| SA | South Australia |
| Q | Queensland |
| NSW | New South Wales |
| V | Victoria |

Each region can be assigned one of three colours:

```python
["Red", "Green", "Blue"]
```

**Constraint:** Two neighbouring regions must not have the same colour.

For example, WA and NT are neighbours, so they must be assigned different colours.

The exercise uses the following neighbouring pairs:

```python
constraints = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V")
]
```

## Task 0: Manual CSP exploration

The starter contains this assignment:

```python
example_assignment = {
    "WA": "Red",
    "NT": "Red",
    "SA": "Green",
    "Q": "Blue",
    "NSW": "Red",
    "V": "Green"
}
```

Before writing any code, answer these questions:

1. Is this assignment valid?
2. Which neighbouring pairs violate a constraint?
3. How could you correct the assignment?
4. Why is it useful to detect violations early?

Check your answers against the constraints list.

## Task 1: Understand the CSP representation

Examine these three structures in `csp_starter.py`:

```python
variables = ["WA", "NT", "SA", "Q", "NSW", "V"]
```

```python
domains = {
    var: ["Red", "Green", "Blue"]
    for var in variables
}
```

```python
constraints = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V")
]
```

Make sure you understand what each structure represents.

Consider:

- Why is a list appropriate for the variables?
- Why is a dictionary useful for the domains?
- What does a pair such as `("WA", "NT")` represent?
- How would you add a new region to this CSP?

You do not need to rewrite the provided representation.

## Task 2: Implement constraint checking

Complete:

```python
def is_valid_assignment(assignment):
    # TODO
    pass
```

The function should return:

- `True` if no constraint is violated.
- `False` if at least one constraint is violated.

Your function must also support **partial assignments**.

For example:

```python
{"WA": "Red", "NT": "Green"}
```

is valid because WA and NT have different colours.

However:

```python
{"WA": "Red", "NT": "Red"}
```

is invalid because WA and NT are neighbours.

### Suggested approach

1. Loop through the neighbouring pairs in `constraints`.
2. Check whether both regions in the pair have been assigned a colour.
3. If both are assigned, compare their colours.
4. Return `False` if the colours are the same.
5. Return `True` if no violations are found.

**Important:** An unassigned region does not automatically make a partial assignment invalid.

Run the file and check that the example assignment is rejected and the valid partial assignment is accepted.

## Task 3: Implement backtracking search

Complete:

```python
def backtracking_search(assignment):
    # TODO
    pass
```

Backtracking builds a solution one assignment at a time.

At each stage, the algorithm:

1. Selects an unassigned variable.
2. Tries a value from its domain.
3. Checks whether the partial assignment is valid.
4. Continues recursively if it is valid.
5. Removes the assignment and tries another value if the search fails.

### Pseudocode

```text
BACKTRACK(assignment):

    if all variables are assigned:
        return assignment

    variable = SELECT-UNASSIGNED-VARIABLE(assignment)

    for each value in domain of variable:

        assign value to variable

        if assignment satisfies constraints:

            result = BACKTRACK(assignment)

            if result is a solution:
                return result

        remove assignment for variable

    return None
```

### Start with simple variable selection

Before implementing MRV, complete the first part of:

```python
def select_unassigned_variable(assignment):
    # TODO
    pass
```

For now, select the first variable that has not yet been assigned.

Use this function inside `backtracking_search()`.

Once backtracking works, running the program should produce a complete colour assignment.

The exact colours may vary depending on the variable-selection strategy, but the assignment must satisfy all constraints.

**Check:** Does `is_valid_assignment(solution)` return `True`?

## Task 4: Compare backtracking with brute force

There are six regions, and each has three possible colours.

The number of possible complete assignments is:

\[
3^6 = 729
\]

In Python:

```python
total_assignments = 3 ** len(variables)
```

The `**` operator means *raised to the power of*.

**Note:** 729 is the number of possible complete assignments, not the number of valid solutions and not necessarily the number of assignments explored by backtracking.

Think about these questions:

1. Would brute force need to consider many invalid complete assignments?
2. What happens when backtracking detects a constraint violation in a partial assignment?
3. Why can rejecting partial assignments early save work?
4. Does finding one valid solution mean that all valid solutions have been found?

## Task 5: Implement Minimum Remaining Values (MRV)

Once your backtracking algorithm works with simple variable selection, improve:

```python
def select_unassigned_variable(assignment):
    # TODO
    pass
```

MRV stands for **Minimum Remaining Values**.

Instead of selecting the first unassigned variable, MRV selects the variable with the fewest currently legal values remaining.

For example, suppose a region has three available colours, but its assigned neighbours already use Red and Green.

Only Blue remains legal.

MRV prioritises variables with fewer legal choices.

### Suggested approach

1. Find the variables that have not yet been assigned.
2. For each unassigned variable, consider the colours in its domain.
3. Temporarily assign each colour.
4. Use `is_valid_assignment()` to determine whether that colour is legal.
5. Remove the temporary assignment.
6. Count the legal colours for each variable.
7. Return the variable with the smallest count.

If two variables have the same number of legal colours, selecting the first is acceptable.

### Questions

- Why might selecting a highly restricted variable help?
- What happens if a variable has no legal values remaining?
- Does MRV guarantee that backtracking will always be faster?

## 4. GitHub task

Commit your progress to your own fork as you work through the lab.

Suggested commit messages:

```bash
git add week05_csp/csp_starter.py
git commit -m "Implement CSP constraint checking"
```

```bash
git add week05_csp/csp_starter.py
git commit -m "Implement CSP backtracking search"
```

```bash
git add week05_csp/csp_starter.py
git commit -m "Add MRV variable selection"
```

When ready, push your work:

```bash
git push origin main
```

Do not push your changes to the lecturer repository. Your work belongs in your own fork.

## 5. Reflection questions

Answer these questions in your lab notes or be prepared to discuss them:

1. What causes backtracking?
2. Why can backtracking be faster than brute force?
3. Why might MRV reduce search?
4. How could this model represent timetabling?

Try to use examples from the map-colouring exercise in your explanations.

## 6. Extensions

These exercises are optional. Complete the core tasks first.

### Extension 1: Count attempted assignments

We calculated that there are **729 possible complete assignments**, but how many assignments does backtracking actually try before finding a solution?

Modify your code to count the number of attempted colour assignments.

For example, introduce a counter:

```python
attempts = 0
```

Increase the counter whenever backtracking tries assigning a colour to a region.

At the end of the search, print:

```text
Possible complete assignments: 729
Attempted colour assignments: ...
```

The second number should be calculated by your program.

**Be precise about what you count:** An attempted colour assignment is one trial of a colour for a variable. It is not the same as examining one complete assignment.

#### Further investigation

1. Run the search using simple variable selection.
2. Record the number of attempted colour assignments.
3. Run the search again using MRV.
4. Compare the results.

| Strategy | Attempted colour assignments | Valid solution found? |
|---|---|---|
| Simple variable selection | Record your result | |
| MRV | Record your result | |

Consider:

- Did MRV reduce the number of attempts?
- Did both strategies find a valid solution?
- Why might the results differ?
- Is this small problem sufficient to demonstrate the benefits of MRV?

You may find that both strategies perform similarly on this small example. That is a useful result too.

### Extension 2: Sudoku CSP

Model a small Sudoku problem as a CSP.

Identify:

- Variables,
- Domains,
- Constraints.

You do not need to implement a Sudoku solver.

Focus on representing the problem correctly.

### Extension 3: Timetabling CSP

Design a CSP involving:

- THREE(3) lectures,
- TWO(2) rooms,
- TWO(2) time slots.

Identify the variables, domains and constraints.

Consider rules such as:

- A room cannot host two lectures at the same time.
- A lecturer cannot teach two lectures simultaneously.
- Lectures attended by the same students cannot overlap.

You do not need to implement a full timetabling system.

### Extension 4: Degree Heuristic

Research the **Degree Heuristic**.

This heuristic prioritises variables that are involved in the largest number of constraints with other unassigned variables.

Consider:

- How does it differ from MRV?
- Which region in our map has the most neighbours?
- Could it be useful when MRV produces a tie?

If you have time, implement the heuristic and compare its behaviour with simple selection and MRV.

### Extension 5: Constraint graph

Draw the map-colouring CSP as a graph.

- Each region is a node.
- Each neighbouring pair is an edge.

Use the nine pairs in the `constraints` list.

Answer:

1. Which region has the most neighbours?
2. Which regions have fewer neighbours?
3. How does the graph help explain the constraints?
4. How might the graph support variable-selection heuristics?

## 7. Lab checklist

Before finishing, make sure you can:

- [ ] Explain variables, domains and constraints.
- [ ] Identify both violations in the manual example.
- [ ] Check complete and partial assignments.
- [ ] Implement recursive backtracking.
- [ ] Produce a valid map colouring.
- [ ] Explain why there are 729 possible complete assignments.
- [ ] Implement and explain MRV.
- [ ] Commit and push your work to your own GitHub fork.
- [ ] Answer the reflection questions.
