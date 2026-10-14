def final_price(total, discount_percent):
    """Calculate price after discount."""
    if total < 0:
        raise ValueError("total must be non-negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")

    return round(total * (1 - discount_percent / 100), 2)
