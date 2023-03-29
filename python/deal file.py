filename = 'learing_python.txt'
f = open(filename)
with open(filename) as file:
    contents = file.read()
print(contents)
with open(filename) as file:
    lines = file.readlines()
for line in lines:
    print(line.rstrip())

