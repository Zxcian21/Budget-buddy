"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    report = {}
    for transaction in data["transactions"]:
        category = transaction["category"]
        report[category] = round(report.get(category, 0) + transaction["amount"], 2)
    return report
