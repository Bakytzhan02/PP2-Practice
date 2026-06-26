with open("sample.txt","w") as f:
    f.write("Hello\nPython")
with open("sample.txt","a") as f:
    f.write("\nAppended line")
