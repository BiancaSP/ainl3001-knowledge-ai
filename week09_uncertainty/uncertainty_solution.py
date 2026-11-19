
"""
AINL3001 — Topic 9: Reasoning Under Uncertainty
BSP 2026

Lecturer solution. You may have implemented a different solution,
which is also perfectly valid. This solution is just a suggestion.

This is a simplified probabilistic reasoning exercise,
NOT a medical diagnostic system or medical advice.
"""


# TASK 0 — MANUAL BAYES ACTIVITY
#
# Given:
# P(Flu) = 0.10
# P(Fever | Flu) = 0.80
# P(Fever) = 0.20
#
# Bayes' Theorem:
#
# P(Flu | Fever)
# = P(Fever | Flu) * P(Flu) / P(Fever)
# = (0.80 * 0.10) / 0.20
# = 0.08 / 0.20
# = 0.40
#
# Interpretation:
# Before observing fever, the probability of flu is 10%.
# After observing fever, it increases to 40%.
#
# Fever provides evidence that increases our belief in Flu,
# but it does not prove that Flu is present.


# TASK 1 IMPLEMENT BAYES' THEOREM

def bayes(prior, likelihood, evidence):
    """Return the posterior probability using Bayes' Theorem."""
    return (likelihood * prior) / evidence


# TASK 2 DIAGNOSTIC EXAMPLE

def diagnostic_example():
    """Calculate P(Flu | Fever) using the supplied probabilities."""

    prior = 0.10
    likelihood = 0.80
    evidence = 0.20

    posterior = bayes(prior, likelihood, evidence)

    return posterior


# TASK 3 ADDITIONAL EVIDENCE
#
# Suppose we observe Fever, Cough and Fatigue.
#
# Multiple observations can be represented using
# conditional probabilities or a Bayesian network.
#
# For example:
#
# P(Flu | Fever, Cough, Fatigue)
#
# We cannot generally multiply individual symptom
# probabilities without making assumptions about
# conditional independence.
#
# Symptoms may be related to one another.
# A Bayesian network can represent dependencies.


# TASK 4 SIMPLE BAYESIAN NETWORK
#
#        Flu
#       /   \
#      v     v
#    Fever  Cough
#
# Flu is a possible cause.
# Fever and Cough are observations.
#
# Observing Fever changes our belief about Flu.
# It does not prove Flu is present.
#
# The arrows represent probabilistic dependencies,
# not deterministic logical rules.


# TASK 5 RISK CLASSIFICATION

def classify_risk(probability):
    """Return an illustrative risk category."""

    if probability < 0.30:
        return "Low Risk"

    elif probability < 0.70:
        return "Medium Risk"

    else:
        return "High Risk"


# TASK 6 DIAGNOSTIC SYSTEM WALKTHROUGH

if __name__ == "__main__":
    """
    The 40% posterior is valid under the supplied hypothetical probabilities, 
    but the risk labels are arbitrary teaching thresholds. 
    Neither constitutes a clinically meaningful diagnosis.
    """
    

    print("=" * 55)
    print("TASK 0 — MANUAL BAYES ACTIVITY")
    print("=" * 55)

    print("P(Flu) = 0.10")
    print("P(Fever | Flu) = 0.80")
    print("P(Fever) = 0.20")

    print("\nBayes' Theorem:")
    print("P(Flu | Fever) = (0.80 * 0.10) / 0.20")
    print("P(Flu | Fever) = 0.40")

    print("\nTASKS 1–2 — BAYES AND DIAGNOSTIC EXAMPLE")

    posterior = diagnostic_example()

    print(f"Prior probability: {0.10:.2f}")
    print(f"Posterior probability: {posterior:.2f}")
    print(f"Risk category: {classify_risk(posterior)}")

    print("\nInterpretation:")
    print("Before observing fever, the probability of flu was 10%.")
    print("After observing fever, the probability rises to 40%.")
    print("Evidence updates our belief but does not establish certainty.")

    print("\nTASK 3 — ADDITIONAL EVIDENCE")
    print("Consider Fever, Cough and Fatigue.")
    print("Multiple observations may provide more information.")
    print("However, symptoms may not be independent.")

    print("\nTASK 4 — SIMPLE BAYESIAN NETWORK")
    print("""
       Flu
      /   \\
     v     v
   Fever  Cough
""")

    print("Flu is a possible cause.")
    print("Fever and Cough are observations.")
    print("Observing Fever updates our belief about Flu.")

    print("\nTASK 6 — REFLECTION")

    print("Logic vs Probability")
    print("Logic asks: Is a statement true or false?")
    print("Probability asks: How likely is a statement?")

    print("\nA posterior probability of 0.40 means")
    print("a 40% probability under the assumed model.")
    print("It does not mean Flu is certain.")
