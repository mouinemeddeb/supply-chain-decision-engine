def main():
    print("Supply Chain Decision Engine")
    print("----------------------------")

    new_part = input("Is this a new part? (yes/no): ").strip().lower()
    risk_level = input("Risk level (A/B/C): ").strip().upper()
    supplier = input("Predefined supplier available? (yes/no): ").strip().lower()
    advantage = input("Time/Cost advantage? (yes/no): ").strip().lower()

    if (
        new_part == "no"
        and risk_level in ["B", "C"]
        and supplier == "yes"
        and advantage == "yes"
    ):
        recommendation = "Use Modified PMQ Process"
        reason = "Existing supplier, manageable risk, and expected efficiency gains."
    else:
        recommendation = "Use Standard PMQ Process"
        reason = "One or more conditions for the modified process are not satisfied."

    print("\nRecommendation:")
    print(recommendation)

    print("\nReason:")
    print(reason)


if __name__ == "__main__":
    main()
