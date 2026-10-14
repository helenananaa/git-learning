import math


def final_price(total, discount_percent):
    """Calculate price after discount."""
    if not math.isfinite(total) or not math.isfinite(discount_percent):
        raise ValueError("inputs must be finite numbers")

    if total < 0:
        raise ValueError("total must be non-negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("discount must be between 0 and 100")

    return round(total * (1 - discount_percent / 100), 2)
