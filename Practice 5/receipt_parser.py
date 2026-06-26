import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Extract all prices from receipt
prices = re.findall(r"\d+\s?\d*,\d{2}", text)

# Extract product names
products = re.findall(
    r"\d+\.\s*\n(.*?)\n\d+,\d+\s*x",
    text,
    re.DOTALL
)

products = [product.replace("\n", " ").strip() for product in products]

# Extract date
date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)

# Extract time
time = re.search(r"\d{2}:\d{2}:\d{2}", text)

# Extract payment method
payment = re.search(r"Банковская карта|Наличные", text)

# Extract total amount
total = re.search(r"ИТОГО:\s*\n([\d\s]+,\d{2})", text)

data = {
    "date": date.group() if date else "Not found",
    "time": time.group() if time else "Not found",
    "payment_method": payment.group() if payment else "Not found",
    "total": total.group(1).strip() if total else "Not found",
    "products": products,
    "prices": prices
}

print(json.dumps(data, indent=4, ensure_ascii=False))
