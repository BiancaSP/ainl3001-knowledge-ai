# Week 7 — Knowledge Representation and Logical Reasoning

**AINL3001 — Knowledge-Driven AI | TU850 · BSP 2026**

## What will you learn?

So far, we have explored *how to search*: through states, assignments, and game trees. This week asks a different question: **What does an AI system know, and what can it infer from that knowledge?**

By the end of this lab, you should be able to:

- distinguish facts from rules;
- represent a small propositional knowledge base in Python;
- explain how `IF ... THEN ...` rules support inference;
- implement forward chaining and query inferred facts;
- explain backward chaining, logical entailment, and the limitations of this representation.

## Getting started

Open your own fork of the course repository and update it from the module's repository, following the workflow used in earlier labs:

```bash
git fetch upstream
git merge upstream/main
git push origin main
```

Open `week07_knowledge_representation/knowledge_representation_starter.py` in VS Code. You can run it with **Run Python File** or from the repository root:

```bash
python week07_knowledge_representation/knowledge_representation_starter.py
```

This exercise uses only Python's standard library. Complete the **starter** file, and the solution will be released later.

## The knowledge base

A **fact** is a statement treated as true within our example, such as `rainy`.

A **rule** describes when another fact can be inferred. For example:

> IF rainy THEN take_umbrella

Our knowledge base starts with:

```python
facts = {"rainy", "weekday"}
```

The rules are:

```python
rules = [
    (["rainy"], "take_umbrella"),
    (["rainy", "cold"], "wear_coat"),
    (["take_umbrella"], "stay_dry"),
]
```

Each tuple contains a **list of conditions** and a **conclusion**. Every condition must hold before its conclusion can be added. The names are *propositional symbols*: the program treats them as indivisible statements, not as natural-language instructions.

## Task 0 — Manual reasoning

Before coding, discuss these questions with a peer:

1. Can we infer `take_umbrella`? Why?
2. Can we infer `stay_dry`? Why?
3. Can we infer `wear_coat`? Why or why not?
4. In which order might new facts be discovered?

Think about whether a conclusion from one rule can activate another rule.

## Task 1 — Represent facts

Inspect the provided `facts` set. Why is a Python **set** suitable for storing known facts? What happens if you try to add the same fact twice?

Experiment by adding `cold` later, after you have implemented forward chaining. What changes?

## Task 2 — Represent rules

Inspect the provided `rules` list. Each rule has the form:

```python
(["condition_1", "condition_2"], "conclusion")
```

The conditions mean **AND**: both must be established before the conclusion follows. Identify which of the three rules has two conditions.

## Task 3 — Implement forward chaining

Complete `forward_chaining(known_facts, rules)`.

The function should:

1. Copy the initial facts into a new set, so the original set is not modified.
2. Examine each rule. If **all** its conditions are in the current set, add its conclusion.
3. Repeat the process until a complete pass adds no new facts.
4. Return the completed set of known and inferred facts.

You may find these Python features useful:

```python
set(known_facts)
all(condition in inferred_facts for condition in conditions)
inferred_facts.add(conclusion)
```

**Why repeat the rules?** A fact inferred by one rule may allow another rule to fire. Stopping after one pass is not a reliable general solution.

## Task 4 — Query the knowledge base

Complete `query(inferred_facts, statement)` so it returns `True` if the statement is present in the completed fact set and `False` otherwise.

Test these queries:

| Statement | Expected result |
| --- | --- |
| `take_umbrella` | `True` |
| `stay_dry` | `True` |
| `wear_coat` | `False` |

**Important:** Here `False` means *the statement cannot be established from the available facts and rules*. It does **not** prove that the statement is false in the real world. We have not been told whether `cold` is true.

Check that `facts` still contains only the original two facts after forward chaining. Then add `cold` to the initial facts and run the program again. Can you now infer `wear_coat`?

## Task 5 — Backward chaining (manual exercise)

Forward chaining starts from known facts and asks **what else follows?** Backward chaining starts from a goal and asks **what would need to be true?**

Start with the goal `stay_dry`:

1. Which rule has `stay_dry` as its conclusion?
2. What condition does that rule require?
3. Which rule could establish that condition?
4. Does the chain ultimately reach an initial fact?

Draw the chain of reasoning. **No backward-chaining implementation is required** for the core lab.

## Task 6 — Logic discussion

Consider the rule `IF rainy THEN take_umbrella`.

Discuss:

1. Does this rule have to be true in the real world?
2. What assumptions are we making when we include it in the knowledge base?
3. How is logical inference from an accepted rule different from statistical reasoning under uncertainty?

A useful distinction: **logical entailment** means a conclusion follows from the knowledge base under the logic's rules. It does not guarantee that the knowledge base accurately describes reality.

## GitHub task

Commit your work progressively to your own fork. For example:

```bash
git add week07_knowledge_representation/knowledge_representation_starter.py
git commit -m "Implement Week 7 forward chaining"
git push origin main
```

You can make earlier commits after inspecting the facts and rules, and another after implementing queries and testing extensions.

## Reflection questions

1. What is logical entailment?
2. How does forward chaining work?
3. How does backward chaining differ from forward chaining?
4. What are the limitations of propositional logic?

## Optional extensions

### Extension 1 — Family relationships

Consider `parent(alice, bob)` and `parent(bob, charlie)`. How could a rule express that Alice is Charlie's grandparent?

These expressions involve **predicates and individuals**, so they go beyond the simple propositional strings used in the main exercise. First describe the rule on paper. For an optional Python experiment, you may use concrete strings such as `"parent_alice_bob"`, but that does **not** implement general first-order logic or variables.

### Extension 2 — Technical support expert system

Create facts and rules about a computer that will not start, a flat battery, and a recommendation to replace the battery. Test which conclusions follow from different initial facts.

### Extension 3 — Medical reasoning example

Model a *toy* example with `fever`, `cough`, and `possible_flu`. Explain why an inferred `possible_flu` statement is **not** a medical diagnosis and why real diagnosis involves uncertainty and additional evidence.

## Check your work

Before finishing, verify that:

- the starter file runs without errors;
- forward chaining returns a **new set** containing both initial and inferred facts;
- chained rules work (including `rainy` → `take_umbrella` → `stay_dry`);
- a rule requiring `cold` does not fire unless `cold` is known;
- the queries produce the expected results;
- you can explain the difference between forward and backward chaining.
- demo your work to your lab TA.

**Summary:** Search explores possibilities. Knowledge representation stores statements and rules; logical inference derives conclusions from them.