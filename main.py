from decision_engine import get_recommendation


def main():
    print("Supply Chain Decision Engine")
    print("----------------------------")

    new_part = input("Is this a new part? (yes/no): ").strip().lower()
    risk_level = input("Risk level (A/B/C): ").strip().upper()
    supplier = input("Predefined supplier available? (yes/no): ").strip().lower()
    advantage = input("Time/Cost advantage? (yes/no): ").strip().lower()

    recommendation, reason = get_recommendation(
        new_part,
        risk_level,
        supplier,
        advantage,
    )

    print("\nRecommendation:")
    print(recommendation)

    print("\nReason:")
    print(reason)


if __name__ == "__main__":
    main()
