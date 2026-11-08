"""AINL3001 — Topic 8: Knowledge Graphs and Expert Systems.
BSP 2026

Lecturer solution. This is a toy rule system, NOT medical advice.
"""

# TASK 0 — MANUAL KNOWLEDGE GRAPH
# Entities: Doctor, Hospital, Dublin, Cardiology.
# Relationships: works_at, located_in, specialises_in.

# TASK 1 — BUILD A KNOWLEDGE GRAPH
knowledge_graph = {
    "Alice": {
        "works_at": "TU_Dublin",
        "teaches": "AI",
    },
    "TU_Dublin": {
        "located_in": "Dublin",
    },
}


def query_graph(graph, entity, relationship):
    """TASK 2: Return the related entity, or None if not found."""
    return graph.get(entity, {}).get(relationship)


# TASK 3 — EXPERT SYSTEM KNOWLEDGE BASE
facts = {"fever", "cough"}
rules = [
    (["fever", "cough"], "possible_flu"),
    (["possible_flu"], "advise_rest"),
]


def forward_chaining(known_facts, rules):
    """TASK 4: Infer facts and record which conditions supported them."""
    inferred_facts = set(known_facts)
    explanations = {}
    changed = True

    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in inferred_facts for condition in conditions):
                if conclusion not in inferred_facts:
                    inferred_facts.add(conclusion)
                    explanations[conclusion] = list(conditions)
                    changed = True

    return inferred_facts, explanations


def explain(conclusion, initial_facts, explanations):
    """TASK 5: Explain one inference step (or identify an initial fact)."""
    if conclusion in initial_facts:
        return f"{conclusion} was given as an initial fact"
    if conclusion in explanations:
        conditions = explanations[conclusion]
        return f"{conclusion} inferred from {' and '.join(conditions)}"
    return f"{conclusion} is not established"


if __name__ == "__main__":
    print("=" * 55)
    print("TASK 0 — MANUAL KNOWLEDGE GRAPH")
    print("=" * 55)
    print("Doctor --works_at--> Hospital")
    print("Hospital --located_in--> Dublin")
    print("Doctor --specialises_in--> Cardiology")
    print("Entities: Doctor, Hospital, Dublin, Cardiology")
    print("Relationships: works_at, located_in, specialises_in")

    print("\nTASKS 1–2 — KNOWLEDGE GRAPH QUERIES")
    for entity, relation in [
        ("Alice", "works_at"),
        ("Alice", "teaches"),
        ("TU_Dublin", "located_in"),
    ]:
        print(f"{entity} --{relation}--> {query_graph(knowledge_graph, entity, relation)}")

    print("\nTASKS 3–6 — EXPERT SYSTEM")
    inferred, explanations = forward_chaining(facts, rules)
    print("Input facts:", sorted(facts))
    print("Derived facts:", sorted(inferred - facts))
    print("Final advice (toy example):", "advise_rest" if "advise_rest" in inferred else "none")
    for conclusion in ("possible_flu", "advise_rest"):
        print("Explanation:", explain(conclusion, facts, explanations))
