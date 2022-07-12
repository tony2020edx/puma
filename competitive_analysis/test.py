def cleanup_discount(discount_string):
    discount_string = discount_string.replace("off", "")
    discount_string = discount_string.replace("%", "").strip()

    return discount_string

text = "38% off"

print(cleanup_discount(text))