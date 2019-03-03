from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:\n")

print(txt.read())





#output = txt.read()
#print(f"\t {output}")
