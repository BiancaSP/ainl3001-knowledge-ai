"""AINL3001 — Topic 8: Knowledge Graphs and Expert Systems.
BSP 2026

Complete the TODOs in Tasks 1, 2, 4 and 5.
Run this file directly from VS Code or the command line.
"""

# TASK 0 — MANUAL KNOWLEDGE GRAPH
# Doctor --works_at--> Hospital
# Hospital --located_in--> Dublin
# Doctor --specialises_in--> Cardiology
# Identify the entities and relationships, then draw the graph.

# TASK 1 — BUILD A KNOWLEDGE GRAPH
# Use a nested dictionary: entity -> relationship -> related entity.
# Represent:
# Alice works_at TU_Dublin
# TU_Dublin located_in Dublin
# Alice teaches AI
knowledge_graph = {
    # TODO: add the entities and relationships
}


def query_graph(graph, entity, relationship):
    """TASK 2: Return the related entity, or None if not found."""
    # TODO: Look up entity and then relationship safely.
    pass


# TASK 3 — EXPERT SYSTEM KNOWLEDGE BASE (provided)
# These are simplified teaching rules, NOT medical advice.
facts = {"fever", "cough"}
rules = [
    (["fever", "cough"], "possible_flu"),
    (["possible_flu"], "advise_rest"),
]


def forward_chaining(known_facts, rules):
    """TASK 4: Return (inferred_facts, explanations).

    inferred_facts: a new set with initial and derived facts.
    explanations: dict mapping each NEW conclusion to its conditions.

    TODO:
    1. Copy known_facts; create an empty explanations dictionary.
    2. Repeatedly inspect all rules.
    3. When every condition is known and a conclusion is new,
       add it and record the conditions that justified it.
    4. Stop when a full pass produces no new facts.
    """
    # TODO
    pass


def explain(conclusion, initial_facts, explanations):
    """TASK 5: Return a one-step explanation of a conclusion.

    If it is an initial fact, return '<fact> was given as an initial fact'.
    If inferred, return '<fact> inferred from <conditions>'.
    Otherwise return '<fact> is not established'.
    """
    # TODO
    pass


if __name__ == "__main__":
    print("=" * 55)
    print("TASK 0 — MANUAL KNOWLEDGE GRAPH")
    print("=" * 55)
    print("Doctor --works_at--> Hospital")
    print("Hospital --located_in--> Dublin")
    print("Doctor --specialises_in--> Cardiology")
    print("Questions: Which are entities? Which are relationships?")

    print("\nTASKS 1–2 — KNOWLEDGE GRAPH QUERIES")
    for entity, relation in [
        ("Alice", "works_at"),
        ("Alice", "teaches"),
        ("TU_Dublin", "located_in"),
    ]:
        print(f"{entity} --{relation}--> {query_graph(knowledge_graph, entity, relation)}")

    print("\nTASKS 3–6 — EXPERT SYSTEM")
    result = forward_chaining(facts, rules)
    if result is None:
        print("Complete forward_chaining() to see the results.")
    else:
        inferred, explanations = result
        print("Input facts:", sorted(facts))
        print("Derived facts:", sorted(inferred - facts))
        print("Final advice (toy example):", "advise_rest" if "advise_rest" in inferred else "none")
        for conclusion in ("possible_flu", "advise_rest"):
            print("Explanation:", explain(conclusion, facts, explanations))
