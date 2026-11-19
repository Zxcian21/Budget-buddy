"""Core BudgetBuddy logic: transactions, balance, and small helpers."""


def get_transactions(data):
    return data["transactions"]


def add_transaction(data, description, amount, category="general"):
    new_id = max((t["id"] for t in data["transactions"]), default=0) + 1
    tx = {"id": new_id, "description": description, "amount": amount, "category": category}
    data["transactions"].append(tx)
    return tx


def balance(data):
    return round(data["starting_balance"] + sum(t["amount"] for t in data["transactions"]), 2)


def list_transactions(transactions, show=print):
    for t in transactions:
        show(str(t["id"]) + ". " + t["description"] + " (" + str(t["amount"]) + ")")


def transactions_by_category(transactions, category):
    return [t for t in transactions if t["category"] == category]


def count_by_category(transactions):
    counts = {}
    for t in transactions:
        name = t["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def last_transaction(transactions):
    return transactions[len(transactions) - 1]


def total_spent(transactions):
    return round(sum(-t["amount"] for t in transactions if t["amount"] < 0), 2)


def average_transaction(transactions):
    if not transactions:
        return 0
    return round(sum(t["amount"] for t in transactions) / len(transactions), 2)


def set_category_budget(data, category, limit):
    """Store a positive finite category limit."""
    if not isinstance(category, str) or not category.strip():
        raise ValueError("category is required")
    if isinstance(limit, bool) or not isinstance(limit, (int, float)) or not (0 < limit < float("inf")):
        raise ValueError("limit must be positive and finite")
    data.setdefault("budgets", {})[category.strip()] = round(limit, 2)


def category_budget_status(data, category):
    if category not in data.get("budgets", {}):
        raise ValueError(f"No budget set for category: {category}")
    spent = total_spent(transactions_by_category(data["transactions"], category))
    limit = data["budgets"][category]
    return {"limit": limit, "spent": spent, "over_budget": spent > limit}


def over_budget_categories(data):
    return {category: category_budget_status(data, category)
            for category in data.get("budgets", {})
            if category_budget_status(data, category)["over_budget"]}
