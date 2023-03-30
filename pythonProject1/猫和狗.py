def read_file(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            contents =f.read()
    except:
        """静默的话，即是我下面这句话改为pass"""
        print(f'Sorry, the file {filename} dost not exist')
    else:
        contents = contents.split()
        contents = ','.join(str(i) for i in contents)
        print(print(contents))
