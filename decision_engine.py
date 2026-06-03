def calculate_score(new_part, risk_level, supplier, advantage, strategic_importance):
    score = 0

    if new_part == "no":
        score += 20

    if risk_level == "C":
        score += 30
    elif risk_level == "B":
        score += 20
    elif risk_level == "A":
        score += 0

    if supplier == "yes":
        score += 25

    if advantage == "yes":
        score += 15

    if strategic_importance == "low":
        score += 10
    elif strategic_importance == "medium":
        score += 5
    elif strategic_importance == "high":
        score += 0

    return score


def get_recommendation(new_part, risk_level, supplier, advantage, strategic_importance):
    score = calculate_score(
        new_part,
        risk_level,
        supplier,
        advantage,
        strategic_importance,
    )

    if score >= 70:
        recommendation = "Use Modified PMQ Process"
        reason = "The project has manageable risk, supplier readiness, and expected efficiency gains."
    elif score >= 50:
        recommendation = "Review Required"
        reason = "The project may be suitable for the modified process, but management review is recommended."
    else:
        recommendation = "Use Standard PMQ Process"
        reason = "The project does not meet enough conditions for the modified process."

    return score, recommendation, reason
