filename = input("> ")
txt = open(filename)

print(f"Here's your file {filename}:")

print(txt.read())
