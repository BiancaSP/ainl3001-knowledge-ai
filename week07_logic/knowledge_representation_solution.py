"""AINL3001 — Topic 7: Knowledge Representation and Logical Reasoning.

A lab solution: a small propositional rule-based expert system.
If you have found a different solution that also works that is great.
This is just a proposed solution.

BSP 2026
"""

# TASK 1 — Represent facts.
facts = {"rainy", "weekday"}

# TASK 2 — Represent rules.
rules = [
    (["rainy"], "take_umbrella"),
    (["rainy", "cold"], "wear_coat"),
    (["take_umbrella"], "stay_dry"),
]


def forward_chaining(known_facts, rules):
    """Return the closure of known_facts under these positive IF/THEN rules."""
    inferred_facts = set(known_facts)
    changed = True

    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in inferred_facts for condition in conditions):
                if conclusion not in inferred_facts:
                    inferred_facts.add(conclusion)
                    changed = True

    return inferred_facts


def query(inferred_facts, statement):
    """Check whether the statement is established by forward chaining."""
    return statement in inferred_facts


if __name__ == "__main__":
    print("=" * 55)
    print("TASK 0 — MANUAL REASONING")
    print("=" * 55)
    print("Initial facts:", sorted(facts))
    print("Rules:")
    for conditions, conclusion in rules:
        print(f"  IF {' AND '.join(conditions)} THEN {conclusion}")
    print("\nPredictions:")
    print("  take_umbrella: yes (rainy is known)")
    print("  stay_dry: yes (take_umbrella can be inferred)")
    print("  wear_coat: not established (cold is not known)")

    print("\n" + "=" * 55)
    print("TASKS 3–4 — FORWARD CHAINING AND QUERIES")
    print("=" * 55)
    inferred = forward_chaining(facts, rules)
    print("Initial facts:", sorted(facts))
    print("All known facts:", sorted(inferred))
    for statement in ("take_umbrella", "stay_dry", "wear_coat"):
        print(f"Can infer {statement}? {query(inferred, statement)}")

    print("\nTASK 5 — BACKWARD CHAINING (discussion)")
    print("Goal stay_dry requires take_umbrella; take_umbrella requires rainy.")
    print("Since rainy is an initial fact, stay_dry can be established.")
    print("\nTASK 6 — LOGIC DISCUSSION")
    print("The rule is an assumption in this knowledge base, not a universal")
    print("real-world guarantee. Logical inference follows the stated rules;")
    print("statistical reasoning instead deals with uncertainty and likelihood.")