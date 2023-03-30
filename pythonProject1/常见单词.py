def count_words(filename,word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except:
        print('no')
    else:
        contents = contents.split()
        contents = ','.join(str(i) for i in contents)
        print(contents.lower().count(word))
count_words('count_words','the')
