filename = 'alice.txt'
try:
    with open(filename,encoding='utf-8') as f:
        contents = f.read()
except:
    print(f"The fileanme {filename} dose not in it")