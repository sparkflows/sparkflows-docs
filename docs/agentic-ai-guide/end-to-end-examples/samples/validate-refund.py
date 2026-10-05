def main(items, inputs, outputs):
    request = outputs.get("2", {}).get("response_json")
    if not isinstance(request, dict):
        return [{"valid": False, "validation_error": "No structured request was returned."}]
    checked = {key: request.get(key) for key in ("order_id", "amount", "currency", "reason")}
    errors = []
    for key in ("order_id", "currency", "reason"):
        if not isinstance(checked[key], str) or not checked[key].strip():
            errors.append(key + " must be explicit and non-empty")
    amount = checked["amount"]
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        errors.append("amount must be a number")
    elif not math.isfinite(amount) or amount <= 0:
        errors.append("amount must be positive and finite")
    if checked["currency"] != "USD":
        errors.append("this practice flow accepts only USD")
    checked["valid"] = not errors
    checked["validation_error"] = "; ".join(errors)
    return [checked]
