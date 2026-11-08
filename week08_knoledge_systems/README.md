# Week 8 — Knowledge Graphs and Expert Systems

**AINL3001 — Knowledge-Driven AI | TU850 · BSP 2026**

## What will you learn?

In topic 7, you represented facts and rules and implemented forward chaining. This week asks: **How can we organise related knowledge, query it, and explain conclusions made by an expert system?**

By the end of the lab, you should be able to represent entities and relationships as a graph, query that graph, describe what an ontology does, reuse forward chaining in an expert system, explain an inference, and discuss strengths and limitations of symbolic systems.

This lab is not assessed. The timetabled lab time can be used to work on your group assignment in KDAI. However, I strongly recommend that you complete this exercise regardless of this in your own time. Complete the exercise yourself before checking the solution.

## Getting started

Update your own fork from the lecturer repository:

```bash
git fetch upstream
git merge upstream/main
git push origin main
```

Open `week08_knowledge_graphs/knowledge_graphs_starter.py` in VS Code and run it using **Run Python File**, or run from the repository root:

```bash
python week08_knowledge_graphs/knowledge_graphs_starter.py
```

Only standard Python is needed for the core lab. Complete the starter file; the lecturer solution will be released later.

## Background

A **knowledge graph** stores **entities** (nodes) and **relationships** (labelled edges). For example, `Alice --works_at--> TU_Dublin`.

An **ontology** defines the kinds of entities and relationships a knowledge system uses, and can specify constraints on their meaning. In this lab we build a simple graph, **not** a formal ontology.

An **expert system** combines a knowledge base with an inference engine. Our simple inference engine uses the forward-chaining algorithm from Week 7. We also record *why* a rule fired, which helps explain conclusions.

## Task 0 — Manual knowledge graph

Draw this graph on paper:

```text
Doctor --works_at--> Hospital
Hospital --located_in--> Dublin
Doctor --specialises_in--> Cardiology
```

Discuss with a lab neighbour: Which words are entities? Which are relationships? Why might a diagram help when a knowledge base becomes large?

## Task 1 — Build a knowledge graph

Complete the supplied `knowledge_graph` dictionary to represent:

- `Alice --works_at--> TU_Dublin`
- `TU_Dublin --located_in--> Dublin`
- `Alice --teaches--> AI`

Use a nested dictionary where the outer key is an entity and the inner dictionary maps relationship names to related entities:

```python
knowledge_graph = {
    "Alice": {
        # TODO: add relationships
    }
}
```

This simple representation assumes one target per relationship per entity. A larger knowledge graph may need several targets for the same relationship.

## Task 2 — Query the graph

Implement `query_graph(graph, entity, relationship)`.

It should return the related entity, or `None` if the entity or relationship is missing. Test:

| Query | Expected answer |
| --- | --- |
| `query_graph(knowledge_graph, "Alice", "works_at")` | `TU_Dublin` |
| `query_graph(knowledge_graph, "Alice", "teaches")` | `AI` |
| `query_graph(knowledge_graph, "TU_Dublin", "located_in")` | `Dublin` |

Think about the difference between **retrieving an explicitly stored relationship** and **inferring a new relationship**. This function only retrieves stored information.

## Task 3 — Inspect the expert system

The starter provides these initial facts and rules:

```python
facts = {"fever", "cough"}
rules = [
    (["fever", "cough"], "possible_flu"),
    (["possible_flu"], "advise_rest"),
]
```

Identify the **knowledge base** (facts and rules) and the **inference engine** (the function you will implement). Predict which conclusions can be inferred.

**Important:** This is a deliberately simplified teaching example, not a diagnostic system or medical advice. Real symptoms are uncertain and can have many causes.

## Task 4 — Implement forward chaining

Complete `forward_chaining(known_facts, rules)` using your Week 7 experience.

1. Copy the initial facts into a new set.
2. Repeatedly examine the rules.
3. If every condition is known and the conclusion is new, add it.
4. Also record the rule's conditions in an `explanations` dictionary.
5. Stop when no new facts are added.
6. Return **both** the inferred facts and the explanation dictionary:

```python
return inferred_facts, explanations
```

For example, the explanation dictionary might include:

```python
{"possible_flu": ["fever", "cough"]}
```

Do not modify the original `facts` set.

## Task 5 — Explain your reasoning

Implement `explain(conclusion, initial_facts, explanations)`.

The function should return a short message:

- If the conclusion was supplied initially: `fever was given as an initial fact`.
- If it was inferred: `possible_flu inferred from fever and cough`.
- If it cannot be established: `unknown_fact is not established`.

This is a **one-step explanation**. For example, explaining `advise_rest` should identify `possible_flu` as its immediate reason. The optional trace extension asks you to follow that reason back to the original facts.

## Task 6 — Expert system walkthrough

Run your completed program and compare:

| Category | Expected content |
| --- | --- |
| Input facts | `cough`, `fever` |
| Derived facts | `advise_rest`, `possible_flu` |
| Final advice (toy example) | `advise_rest` |

Explain the reasoning chain:

```text
fever AND cough
       ↓
   possible_flu
       ↓
    advise_rest
```

Discuss: How does this make the system's conclusion easier to inspect? What could go wrong if the rules were incomplete or inaccurate?

## GitHub task

Commit your progress to **your own fork**. Suggested milestones: knowledge graph, graph queries, forward chaining, explanation functionality.

For example:

```bash
git add week08_knowledge_graphs/knowledge_graphs_starter.py
git commit -m "Implement Week 8 knowledge graph queries"
git push origin main
```

## Reflection questions

1. Why can symbolic systems be explainable?
2. Why can expert systems become brittle?
3. How are knowledge graphs used in industry?
4. What advantages can symbolic systems provide over less interpretable models?

## Optional extensions

### Extension 1 — Student knowledge graph

Represent students, modules and lecturers, with relationships such as `enrolled_in` and `teaches`. Query the relationships you added.

### Extension 2 — Full explanation trace

Extend the explanation function to trace dependencies recursively, for example:

```text
advise_rest because possible_flu
possible_flu because fever and cough
fever and cough were initial facts
```

Think about how you would prevent repeated explanations if rules form a cycle.

### Extension 3 — Expanded expert system

Add these toy rules:

```python
(["fever", "rash"], "possible_measles")
(["fever", "sore_throat"], "possible_infection")
```

Test different initial facts. Can more than one possible condition be inferred? Why would a real system need evidence, uncertainty handling and human review rather than treating these outputs as diagnoses?

### Extension 4 — Graph visualisation (optional dependency)

Investigate **NetworkX** and Matplotlib to draw your graph. If you choose this extension, install NetworkX in your activated virtual environment:

```bash
python -m pip install networkx
```

NetworkX is **not required** for the core lab. Do not add it to the course-wide requirements unless agreed with the lecturer.

## Before you finish

Check that the graph contains all three relationships, queries return the expected values, forward chaining infers both new facts, and explanations identify the conditions that led to each conclusion. Be able to distinguish a knowledge graph from an ontology and an expert system.

**Takeaway:** Knowledge graphs organise connected facts. Expert systems apply rules to infer conclusions. Recording which rules fired helps explain those conclusions, but the quality of the results still depends on the quality of the knowledge base.