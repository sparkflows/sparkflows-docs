def main(items, inputs, outputs):
    if len(items) != 1:
        raise ValueError("This exercise requires exactly one sales total")
    item = dict(items[0])
    expected = {
        "sales_date": "2026-09-28",
        "rate_date": "2026-09-28",
        "currency": "GBP",
        "rate_base": "GBP",
        "target_currency": "USD",
        "rate_quote": "USD",
        "rate_source": "Fictional training fixture",
    }
    for field, value in expected.items():
        if item.get(field) != value:
            raise ValueError("Missing or unexpected " + field)
    for field in ("amount", "rate"):
        value = item.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float, str)):
            raise ValueError(field + " must be numeric")
        number = float(value)
        if not math.isfinite(number) or number <= 0:
            raise ValueError(field + " must be positive and finite")
        item[field] = number
    converted = item["amount"] * item["rate"]
    if not math.isfinite(converted):
        raise ValueError("The converted amount is outside the supported range")
    item["converted_amount"] = round(converted, 2)
    return [item]
