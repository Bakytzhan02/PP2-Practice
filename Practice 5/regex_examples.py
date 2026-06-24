import re

text = "Milk 450 Bread 220 Chocolate 780"

x = re.search(r"\d+", text)
print("search:", x.group())

x = re.findall(r"\d+", text)
print("findall:", x)

x = re.split(r"\s+", text)
print("split:", x)

x = re.sub(r"Milk", "Coffee", text)
print("sub:", x)

x = re.match(r"Milk", text)
print("match:", x.group())
