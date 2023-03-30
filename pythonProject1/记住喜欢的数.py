import  json
def rembmer_number(filename):
    try:
        with open(filename,'r+') as f:
            number = f.read()
    except:
        number = input("你喜欢哪个数字: ")
        json.dump(number,f)
    else:
        number = json.load()
        print(f"你喜欢的数字是{number}")