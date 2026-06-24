import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

prices = re.findall(r"\d+", text)

date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)
time = re.search(r"\d{2}:\d{2}", text)

payment = re.search(r"(CARD|CASH)", text, re.IGNORECASE)

total = re.search(r"TOTAL\s+(\d+)", text)

products = re.findall(r"[A-Za-z]+", text)

data = {
    "date": date.group() if date else "Not found",
    "time": time.group() if time else "Not found",
    "prices": prices,
    "payment_method": payment.group() if payment else "Not found",
    "total": total.group(1) if total else "Not found",
    "products": products
}

print(json.dumps(data, indent=4))
