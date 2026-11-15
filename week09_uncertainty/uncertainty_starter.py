
"""
AINL3001 — Topic 9: Reasoning Under Uncertainty
BSP 2026

Complete the TODOs in Tasks 1, 2 and 5.
Tasks 0, 3 and 4 include manual and discussion activities.
Task 6 brings everything together.

Run this file directly from VS Code or the command line.

This is a simplified teaching example, NOT medical advice.
"""


# TASK 0 MANUAL BAYES ACTIVITY
#
# Given:
# P(Flu) = 0.10
# P(Fever | Flu) = 0.80
# P(Fever) = 0.20
#
# Calculate:
# P(Flu | Fever)
#
# Bayes' Theorem:
#
# P(A | B) = P(B | A) * P(A) / P(B)
#
# Questions:
# 1. What is the posterior probability?
# 2. Why is it larger than the prior probability?
# 3. What does this tell us about uncertain evidence?


# TASK 1 IMPLEMENT BAYES' THEOREM

def bayes(prior, likelihood, evidence):
    """Return the posterior probability using Bayes' Theorem.

    TODO:
    1. Multiply likelihood by prior.
    2. Divide by evidence.
    3. Return the posterior probability.

    Assume valid probabilities and evidence > 0.
    """
    # TODO
    pass


# TASK 2 DIAGNOSTIC EXAMPLE

def diagnostic_example():
    """Calculate P(Flu | Fever) using the supplied probabilities.

    TODO:
    1. Set the prior probability to 0.10.
    2. Set the likelihood to 0.80.
    3. Set the evidence probability to 0.20.
    4. Call bayes() with these values.
    5. Return the posterior probability.
    """
    # TODO
    pass


# TASK 3 ADDITIONAL EVIDENCE
#
# Suppose we observe:
# - Fever
# - Cough
# - Fatigue
#
# Discuss:
# 1. How could multiple symptoms be represented?
# 2. Can we simply multiply their probabilities?
# 3. What assumptions would be needed?
# 4. What happens if symptoms are related?
#
# No code required for this task.


# TASK 4 — SIMPLE BAYESIAN NETWORK
#
# Consider the following network:
#
#        Flu
#       /   \
#      v     v
#    Fever  Cough
#
# Questions:
# 1. Which variable represents a possible cause?
# 2. Which variables represent observations?
# 3. What happens to our belief about Flu if Fever is observed?
# 4. Does observing Fever prove that Flu is present?
#
# No code required for this task.


# TASK 5 RISK CLASSIFICATION

def classify_risk(probability):
    """Return a risk category based on a probability.

    Use these illustrative thresholds:

    probability < 0.30          -> "Low Risk"
    0.30 <= probability < 0.70  -> "Medium Risk"
    probability >= 0.70         -> "High Risk"

    TODO:
    1. Check whether probability is below 0.30.
    2. Otherwise, check whether it is below 0.70.
    3. Otherwise, return High Risk.

    Assume probability is between 0 and 1.

    These thresholds are for teaching purposes only.
    """
    # TODO
    pass


# TASK 6 DIAGNOSTIC SYSTEM WALKTHROUGH

if __name__ == "__main__":

    print("=" * 55)
    print("TASK 0 — MANUAL BAYES ACTIVITY")
    print("=" * 55)

    print("P(Flu) = 0.10")
    print("P(Fever | Flu) = 0.80")
    print("P(Fever) = 0.20")
    print("\nCalculate P(Flu | Fever) manually.")

    print("\nTASKS 1–2 — BAYES AND DIAGNOSTIC EXAMPLE")

    posterior = diagnostic_example()

    if posterior is None:
        print("Complete bayes() and diagnostic_example().")
    else:
        print(f"Posterior probability: {posterior:.2f}")

        risk = classify_risk(posterior)

        if risk is None:
            print("Complete classify_risk() to see the category.")
        else:
            print(f"Risk category: {risk}")

    print("\nTASK 3 — ADDITIONAL EVIDENCE")
    print("Consider Fever, Cough and Fatigue.")
    print("How might multiple observations affect our belief?")

    print("\nTASK 4 — SIMPLE BAYESIAN NETWORK")
    print("""
       Flu
      /   \\
     v     v
   Fever  Cough
""")
    print("Identify the cause and observations.")

    print("\nTASK 6 — REFLECTION")
    print("How does probability differ from logical reasoning?")
    print("Does a probability of 0.40 mean Flu is certain?")
