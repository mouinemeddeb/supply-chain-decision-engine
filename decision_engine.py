def get_recommendation(new_part, risk_level, supplier, advantage):
    if (
        new_part == "no"
        and risk_level in ["B", "C"]
        and supplier == "yes"
        and advantage == "yes"
    ):
        return (
            "Use Modified PMQ Process",
            "Existing supplier, manageable risk, and expected efficiency gains."
        )

    return (
        "Use Standard PMQ Process",
        "One or more conditions for the modified process are not satisfied."
    )
