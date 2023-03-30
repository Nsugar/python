import json
number = input('请输入您喜欢的数：')
try:
    number = int(number)
except:
    pass
else:
    filename = 'number.json'
    with open(filename,'w') as f:
        json.dump(number,f)