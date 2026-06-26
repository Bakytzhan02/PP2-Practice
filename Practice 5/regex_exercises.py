import re

# 1. Match string that has 'a' followed by zero or more 'b'
text1 = "a ab abb abbb ac"
print("1:", re.findall(r"ab*", text1))

# 2. Match string that has 'a' followed by two to three 'b'
text2 = "ab abb abbb abbbb"
print("2:", re.findall(r"ab{2,3}", text2))

# 3. Find sequences of lowercase letters joined with underscore
text3 = "hello_world one_two Hello_World test_example"
print("3:", re.findall(r"\b[a-z]+_[a-z]+\b", text3))

# 4. Find sequences of one upper case letter followed by lower case letters
text4 = "Hello World test Python KBTU"
print("4:", re.findall(r"\b[A-Z][a-z]+\b", text4))

# 5. Match string that has 'a' followed by anything, ending in 'b'
text5 = "acccb axxxb ab hello"
print("5:", re.findall(r"a.*?b", text5))

# 6. Replace all occurrences of space, comma, or dot with colon
text6 = "Python, Java. C++"
print("6:", re.sub(r"[ ,.]", ":", text6))

# 7. Convert snake case string to camel case string
snake_text = "snake_case_string"
parts = snake_text.split("_")
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print("7:", camel)

# 8. Split a string at uppercase letters
text8 = "HelloWorldPython"
print("8:", re.split(r"(?=[A-Z])", text8))

# 9. Insert spaces between words starting with capital letters
text9 = "HelloWorldPython"
print("9:", re.sub(r"([A-Z])", r" \1", text9).strip())

# 10. Convert camel case string to snake case
camel_text = "HelloWorldPython"
snake = re.sub(r"([A-Z])", r"_\1", camel_text).lower().lstrip("_")
print("10:", snake)
