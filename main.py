from decision_engine import get_recommendation


def ask_choice(question, valid_choices):
    while True:
        answer = input(question).strip().lower()

        if answer in valid_choices:
            return answer

        print(f"Invalid input. Please choose from: {', '.join(valid_choices)}")


def main():
    print("Supply Chain Decision Engine")
    print("----------------------------")

    new_part = ask_choice("Is this a new part? (yes/no): ", ["yes", "no"])
    risk_level = ask_choice("Risk level (A/B/C): ", ["a", "b", "c"]).upper()
    supplier = ask_choice("Predefined supplier available? (yes/no): ", ["yes", "no"])
    advantage = ask_choice("Time/Cost advantage? (yes/no): ", ["yes", "no"])
    strategic_importance = ask_choice(
        "Strategic importance (low/medium/high): ",
        ["low", "medium", "high"],
    )

    score, recommendation, reason = get_recommendation(
        new_part,
        risk_level,
        supplier,
        advantage,
        strategic_importance,
    )

    print("\nDecision Score:")
    print(f"{score}/100")

    print("\nRecommendation:")
    print(recommendation)

    print("\nReason:")
    print(reason)


if __name__ == "__main__":
    main()
