filename = 'alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except:
    print(f"The file {filename} dose not in it")
else:
    words = contents.split()
    print(words)
    print(len(words))