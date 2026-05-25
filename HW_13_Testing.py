def loan_decision(age, income, credit_score, employment):
    # Validate input
    if not isinstance(age, int):
        return "Invalid Input"

    if age < 18 or age > 65:
        return "Invalid Input"

    if income < 5.0 or income > 500.0:
        return "Invalid Input"

    if not isinstance(credit_score, int):
        return "Invalid Input"

    if credit_score < 300 or credit_score > 850:
        return "Invalid Input"

    if employment not in ["C", "F"]:
        return "Invalid Input"

    # Risk classification
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # Business rules
    if risk == "High":
        return "REJECT"

    if income < 15.0:
        if employment == "F" or risk == "Medium":
            return "REJECT"
        return "MANUAL REVIEW"

    if income >= 15.0:
        if employment == "C":
            return "APPROVE"
        return "MANUAL REVIEW"


test_cases = [
    (17, 20.0, 700, "C", "Invalid Input"),
    (66, 20.0, 700, "C", "Invalid Input"),
    (30, 4.9, 700, "C", "Invalid Input"),
    (30, 500.1, 700, "C", "Invalid Input"),
    (30, 20.0, 299, "C", "Invalid Input"),
    (30, 20.0, 851, "C", "Invalid Input"),
    (30, 20.0, 700, "X", "Invalid Input"),

    (30, 10.0, 400, "C", "REJECT"),
    (30, 20.0, 400, "F", "REJECT"),
    (30, 14.9, 600, "C", "REJECT"),
    (30, 14.9, 750, "F", "REJECT"),
    (30, 14.9, 750, "C", "MANUAL REVIEW"),
    (30, 15.0, 600, "C", "APPROVE"),
    (30, 15.0, 750, "C", "APPROVE"),
    (30, 15.0, 600, "F", "MANUAL REVIEW"),
    (30, 15.0, 750, "F", "MANUAL REVIEW"),
]

for i, tc in enumerate(test_cases, start=1):
    age, income, credit_score, employment, expected = tc
    result = loan_decision(age, income, credit_score, employment)

    assert result == expected, f"TC{i} Failed: expected {expected}, got {result}"

print("All test cases passed!")