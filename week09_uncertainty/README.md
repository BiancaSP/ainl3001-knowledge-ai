
# Topic 9 — Reasoning Under Uncertainty

**AINL3001 — Knowledge-Driven AI | TU850 · BSP 2026**

## What will you learn?

In Topics 7 and 8, you represented knowledge using facts, rules and knowledge graphs. You also implemented forward chaining to derive conclusions from known facts.

This week asks: **How can an AI system reason when information is incomplete, uncertain or unreliable?**

By the end of this lab, you should be able to:

- Explain why uncertainty exists in AI systems.
- Distinguish logical reasoning from probabilistic reasoning.
- Understand prior, conditional and posterior probabilities.
- Apply Bayes' Theorem to update a belief using evidence.
- Implement Bayes' Theorem in Python.
- Build a simple probabilistic diagnostic example.
- Classify probabilities into illustrative risk categories.
- Explain the basic structure of a Bayesian network.
- Discuss the limitations of probabilistic models.

This lab is not assessed. The timetabled lab time can be used to work on your group assignment in KDAI. However, I strongly recommend that you complete this exercise regardless of this in your own time.

**Complete the exercise yourself before checking the solution.**

## Getting started

Update your own fork from the lecturer repository:

```bash
git fetch upstream
git merge upstream/main
git push origin main
```

Open `week09_uncertainty/uncertainty_starter.py` in VS Code and run it using **Run Python File**, or run from the repository root:

```bash
python week09_uncertainty/uncertainty_starter.py
```

Only standard Python is needed for this lab. No additional packages are required.

Complete the TODOs in **Tasks 1, 2 and 5**. Tasks 0, 3 and 4 are manual or discussion activities. Task 6 brings everything together.

The lecturer solution will be released later.

## Background

### From logic to uncertainty

In Topics 7 and 8, we used symbolic reasoning.

For example, an expert system might contain the rule:

```text
IF fever AND cough
THEN possible_flu
```

If both conditions are present, the rule fires and the conclusion is added to the knowledge base.

However, real-world information is rarely this straightforward.

Consider the following situations:

- A person may have flu without a fever.
- A person may have a fever without having flu.
- A medical test may produce a false positive.
- A sensor may return inaccurate measurements.
- Some evidence may be missing or unreliable.

A rule-based system can represent possible conclusions, but it does not automatically tell us how likely those conclusions are.

This motivates **probabilistic reasoning**.

### Logic vs probability

Logical reasoning typically deals with statements that are true or false.

For example:

```text
Rainy = True
```

Probabilistic reasoning represents uncertainty:

```text
P(Rainy) = 0.80
```

This means there is an 80% probability of rain according to the model.

The distinction is important:

- **Logic:** Is a statement true or false?
- **Probability:** How likely is a statement to be true?

Probabilistic reasoning allows an AI system to update its beliefs when new evidence becomes available.

### Understanding conditional probability

A conditional probability describes the probability of an event given that another event has occurred.

For example:

```text
P(Fever | Flu)
```

This means:

"The probability of Fever given that Flu is present."

It is not the same as:

```text
P(Flu | Fever)
```

which means:

"The probability of Flu given that Fever is observed."

**These two probabilities are not generally equal.**

Bayes' Theorem allows us to calculate one using the other, provided we have the necessary information.

### Bayes' Theorem

Bayes' Theorem is:

```text
P(A | B) = P(B | A) × P(A) / P(B)
```

Where:

- `P(A)` is the **prior probability** of A.
- `P(B | A)` is the **likelihood** of observing B given A.
- `P(B)` is the **evidence probability**.
- `P(A | B)` is the **posterior probability** of A after observing B.

The posterior represents our updated belief after considering new evidence.

## Task 0 Manual Bayes activity

Suppose we are given the following hypothetical probabilities:

```text
P(Flu) = 0.10

P(Fever | Flu) = 0.80

P(Fever) = 0.20
```

Using Bayes' Theorem:

```text
P(Flu | Fever)

= P(Fever | Flu) × P(Flu) / P(Fever)
```

Calculate `P(Flu | Fever)` manually.

Discuss with a lab neighbour:

1. What is the posterior probability?
2. Is it higher or lower than the prior probability?
3. Why does observing Fever change our belief about Flu?
4. Does the result mean that the person definitely has Flu?

Check your manual calculation before moving on to Python.

**Important:** The probabilities in this exercise are invented for teaching purposes. This is not a medical diagnostic model or medical advice.

## Task 1 Implement Bayes' Theorem

Open `starter.py` and find:

```python
def bayes(prior, likelihood, evidence):
    # TODO
    pass
```

Implement Bayes' Theorem using the three supplied parameters.

Your function should:

1. Multiply the likelihood by the prior probability.
2. Divide the result by the evidence probability.
3. Return the posterior probability.

For this exercise, assume all inputs are valid probabilities and that the evidence probability is greater than zero.

You should be able to call:

```python
bayes(0.10, 0.80, 0.20)
```

Expected result:

```text
0.4
```

Think about what each argument represents. Why is the order of the arguments important?

## Task 2 Diagnostic example

Complete the function:

```python
def diagnostic_example():
    # TODO
    pass
```

Use the following values:

```python
prior = 0.10
likelihood = 0.80
evidence = 0.20
```

Your function should:

1. Define the three probabilities.
2. Call your `bayes()` function.
3. Store the returned posterior probability.
4. Return the posterior probability.

Do not repeat the Bayes calculation inside `diagnostic_example()`. Reuse the function you implemented in Task 1.

When completed, the following should work:

```python
posterior = diagnostic_example()
print(posterior)
```

Expected output:

```text
0.4
```

### Interpreting the result

Before observing Fever:

```text
P(Flu) = 0.10
```

After observing Fever:

```text
P(Flu | Fever) = 0.40
```

The probability has increased from 10% to 40%.

This demonstrates **Bayesian updating**: evidence changes our belief about a hypothesis.

Discuss:

- Why has the probability increased?
- Why is the posterior still below 50%?
- Why would it be incorrect to conclude that Flu is definitely present?

## Task 3 Additional evidence

So far, we have considered only one observation: Fever.

Suppose we also observe:

- Cough
- Fatigue

We might now be interested in:

```text
P(Flu | Fever, Cough, Fatigue)
```

Discuss the following questions:

1. How could we represent multiple symptoms in a probabilistic model?
2. Would observing more symptoms always increase the probability of Flu?
3. Can we simply multiply the probabilities of individual symptoms?
4. What problems arise if symptoms are related to one another?

For example, Fever and Fatigue might not be independent.

This matters because multiplying conditional probabilities is only valid under appropriate independence assumptions.

**No additional Python code is required for this task.**

The aim is to understand why reasoning with multiple observations can become more complicated.

## Task 4 Simple Bayesian network

A **Bayesian network** represents variables and their probabilistic dependencies using a directed graph.

Consider the following simplified network:

```text
       Flu
      /   \
     v     v
   Fever  Cough
```

The nodes represent variables.

The directed edges represent probabilistic dependencies.

In this example:

- Flu is a possible cause.
- Fever is an observable symptom.
- Cough is another observable symptom.

The network represents a model in which Flu influences the probabilities of Fever and Cough.

### Questions

1. Which variable represents a possible cause?
2. Which variables represent observations?
3. What happens to our belief about Flu when Fever is observed?
4. Does observing Fever prove that Flu is present?
5. Why might this representation be useful when working with many variables?

A Bayesian network can be used to reason about uncertain relationships between variables.

However, the graph alone does not provide numerical probabilities. A complete Bayesian network also requires conditional probability tables.

**No Python implementation is required for this task.**

## Task 5 Risk classification

In Task 2, you calculated a posterior probability.

We will now convert a probability into a simple category.

Complete:

```python
def classify_risk(probability):
    # TODO
    pass
```

Use these illustrative thresholds:

| Probability | Category |
| --- | --- |
| Below 0.30 | Low Risk |
| 0.30 to below 0.70 | Medium Risk |
| 0.70 and above | High Risk |

Your function should return one of these strings:

```python
"Low Risk"
"Medium Risk"
"High Risk"
```

Use `if`, `elif` and `else`.

### Test your function

| Function call | Expected result |
| --- | --- |
| `classify_risk(0.10)` | Low Risk |
| `classify_risk(0.29)` | Low Risk |
| `classify_risk(0.30)` | Medium Risk |
| `classify_risk(0.40)` | Medium Risk |
| `classify_risk(0.70)` | High Risk |
| `classify_risk(0.90)` | High Risk |

Think about the boundary values.

For example, why should `classify_risk(0.30)` return `"Medium Risk"` rather than `"Low Risk"`?

**Important:** These categories are arbitrary teaching examples. Real-world risk categories require domain knowledge, validation and careful consideration of consequences.

## Task 6 Diagnostic system walkthrough

Run your completed program:

```bash
python week09_uncertainty/starter.py
```

Your program should calculate the posterior probability and classify the result.

Compare your output with the following:

| Category | Expected content |
| --- | --- |
| Prior probability | `0.10` |
| Posterior probability | `0.40` |
| Risk category | `Medium Risk` |

The program should display:

```text
TASKS 1–2 — BAYES AND DIAGNOSTIC EXAMPLE
Posterior probability: 0.40
Risk category: Medium Risk
```

### Explain the reasoning

Consider the following sequence:

```text
Prior belief:
P(Flu) = 0.10
       |
       v
Observe evidence:
Fever
       |
       v
Apply Bayes' Theorem
       |
       v
Updated belief:
P(Flu | Fever) = 0.40
       |
       v
Illustrative classification:
Medium Risk
```

Be able to explain each step.

Discuss:

- What role does the prior probability play?
- How does evidence influence the posterior?
- Why is the posterior not a certainty?
- What limitations does this simplified system have?

## Comparing logic and probability

Recall the expert system from Topic 8.

A rule might state:

```text
IF fever AND cough
THEN possible_flu
```

The inference engine applies the rule when the conditions are satisfied.

A probabilistic model instead asks:

```text
Given the observed symptoms,
how likely is Flu?
```

These approaches represent different ways of reasoning.

| Symbolic reasoning | Probabilistic reasoning |
| --- | --- |
| Uses facts and rules | Uses probabilities and evidence |
| Derives conclusions from conditions | Updates beliefs using observations |
| Often uses true/false statements | Represents degrees of uncertainty |
| Depends on logical rules | Depends on probabilistic assumptions |
| Can explain which rules fired | Can explain how evidence affects probabilities |

Neither approach is universally better.

Symbolic reasoning can be useful when rules are clearly defined. Probabilistic reasoning can be useful when evidence is incomplete, noisy or uncertain.

Some AI systems combine both approaches.

## GitHub task

Commit your progress to **your own fork** of the repository.

Suggested milestones:

- Implement Bayes' Theorem.
- Complete the diagnostic example.
- Implement risk classification.
- Test the completed system.

For example:

```bash
git add week09_uncertainty/starter.py
git commit -m "Implement Week 9 Bayesian reasoning"
git push origin main
```

You can make several smaller commits as you complete the tasks.

Remember that GitHub is not just for submitting finished code. It is also useful for recording how your work develops.

## Reflection questions

1. Why does uncertainty exist in real-world AI systems?
2. What is the difference between prior and posterior probability?
3. What does conditional probability mean?
4. Why is `P(Flu | Fever)` different from `P(Fever | Flu)`?
5. Why does observing evidence not necessarily prove a hypothesis?
6. How does probabilistic reasoning differ from logical reasoning?
7. Why is probabilistic reasoning important in Data Science?
8. What are the limitations of a simple Bayesian diagnostic system?

## Optional extensions

These extensions are not required for the core lab.

### Extension 1 COVID scenario

Create a new hypothetical Bayesian example involving:

- COVID
- Fever
- Loss of smell

Investigate how prior probabilities and likelihoods might be estimated from reliable data.

Use Bayes' Theorem to calculate an updated probability.

Consider:

- How might the prior probability change over time?
- Why might probabilities differ between populations?
- Why is reliable data important?

Do not treat the output as a medical diagnosis.

### Extension 2 Spam detection

Apply Bayesian reasoning to a different problem.

Suppose an email may be Spam or Not Spam.

Consider observations such as:

```text
Contains "Free"
Contains "Prize"
```

Start with a single observation.

For example:

```text
P(Spam) = 0.20

P(Free | Spam) = 0.70

P(Free) = 0.30
```

Calculate:

```text
P(Spam | Free)
```

Then investigate how a second observation might affect the result.

Think about whether the observations are independent.

### Extension 3 Multiple hypotheses

Extend the diagnostic example to consider several possible hypotheses:

- Flu
- Common Cold
- COVID

Use hypothetical probabilities to explore how the same observation might affect different hypotheses.

Discuss:

- Can different hypotheses have different likelihoods?
- Why might one observation support several hypotheses?
- Why must probabilities be interpreted in the context of the model?

For a complete multi-hypothesis model, ensure that the hypotheses are defined consistently and that their probabilities form a valid distribution.

### Extension 4 Sensitivity to the prior

Keep the likelihood and evidence fixed:

```python
likelihood = 0.80
evidence = 0.20
```

Investigate different prior probabilities using valid combinations of inputs.

For example, compare:

```python
bayes(0.05, 0.80, 0.20)
bayes(0.10, 0.80, 0.20)
bayes(0.20, 0.80, 0.20)
```

Questions:

1. How does the posterior change?
2. Why does the prior matter?
3. What happens when the prior is very small?

Note that changing the prior while holding the evidence probability fixed is a sensitivity exercise, not necessarily a single coherent probabilistic model. In a fully specified model, the evidence probability must remain consistent with the prior and likelihoods.

## Before you finish

Check that:

- You can calculate Bayes' Theorem manually.
- Your `bayes()` function returns the expected posterior.
- Your `diagnostic_example()` function reuses `bayes()`.
- Your `classify_risk()` function handles the threshold boundaries correctly.
- Your program runs without errors.
- You can explain the difference between a prior and posterior probability.
- You understand what a Bayesian network represents.
- You can explain why probabilistic reasoning is useful when information is uncertain.

**Takeaway:** Logical reasoning derives conclusions from facts and rules. Probabilistic reasoning updates beliefs using evidence. Bayes' Theorem provides a mathematical way to perform this update, but the reliability of the result depends on the assumptions and probabilities used by the model.
