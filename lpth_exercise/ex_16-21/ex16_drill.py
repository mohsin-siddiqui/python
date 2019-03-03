from sys import argv

script, filename = argv

txt = open(filename)

print(f"Your file {filename}:")

print(txt.read())
