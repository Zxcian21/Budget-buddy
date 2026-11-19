"""Reporting helpers for BudgetBuddy.

Heads up: this module is half-built on purpose. `account_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""


def account_summary(data):
    return data["account_name"] + ": " + str(len(data["transactions"])) + " transactions"


def category_report(data):
    # TODO(ticket): tally each transaction into a {category: total amount} dict and return it.
    # For now this returns an empty report so the menu never crashes.
    report = {}
    return report

def monthly_summary(data):
    """Dated monthly income/spending; legacy undated transactions are skipped."""
    from datetime import date

    months = {}
    for transaction in data["transactions"]:
        stamp = transaction.get("date")
        if not isinstance(stamp, str):
            continue
        try:
            month = date.fromisoformat(stamp).strftime("%Y-%m")
        except ValueError:
            continue
        totals = months.setdefault(month, {"income": 0, "spending": 0})
        amount = transaction["amount"]
        key = "income" if amount >= 0 else "spending"
        totals[key] = round(totals[key] + abs(amount), 2)
    return dict(sorted(months.items()))
