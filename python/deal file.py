filename = 'learing_python.txt'
with open(filename,'r') as file:
    contents = file.read()
    lines = file.readlines()
print(contents)
for line in lines:
    print(line.rstrip())

