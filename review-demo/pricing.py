def final_price(total, discount_percent):
    """Calculate price after discount."""
    return round(total * (1 - discount_percent / 100), 2)